# <------------- Librerias ------------- >
# Generar numeros o selecciones de manera random.
import random
from Motifs import Motifs as MTFS
from Hongos import Hongos as HNS

class Genetico(object):

	"""
		Inicializamos la clase
		Los parametros que se pueden manupular 
		desde la creacion de la clase son los sigueintes, 
		donde se les asigno un valor por default:
		
		* tamPoblacion = 100
		* tamProteina = 2654
		* tamMotivo = 20
		* numHongos = 1245
		* proMutacion = 0.01
		* canMutacion = 2
		* numElitismo = 10
		* tamTorneo = 4
		* umbral = 50
		* proCruce = 60
		* w = [1/3, 1/3, 1/3]
	"""

	""" Es utilizado para ubicar la posicion del aminoacido en las matrices de evaluacion. """	
	index = { 'A':0, 'C':1, 'D':2, 'E':3, 'F':4, 'G':5, 'H':6, 'I':7, 'K':8, 'L':9, 'M':10, 'N':11, 'P':12, 'Q':13, 'R':14, 'S':15, 'T':16, 'V':17, 'W':18, 'Y':19 }
	
	SCIM, CCIM, HCIM = MTFS().SCICCIHCI()
	Hongos = HNS().matrizHongos()
		
	"""Funcion que inicializa la poblacion"""
	def __init__(self, tamPoblacion = 100, tamProteina = 2654,
		tamMotivo = 20,numHongos = 1245,proMutacion = 0.01,
		canMutacion = 2,numElitismo = 10,tamTorneo = 4, 
		umbral = 50, proCruce = 60, w = [1/3, 1/3, 1/3]):
		self.tamPoblacion = tamPoblacion
		self.tamProteina = tamProteina
		self.tamMotivo = tamMotivo
		self.numHongos = numHongos
		self.proMutacion = proMutacion
		self.canMutacion = canMutacion
		self.numElitismo = numElitismo
		self.tamTorneo = tamTorneo
		self.umbral = umbral
		self.proCruce = proCruce
		self.w = w
		self.ind = []
		self.poblacion = []
		self.nuevapoblacion = []
		self.fit = [0.0 for i in range(tamPoblacion)]

		for _ in range(self.tamPoblacion):
			self.ind = []
			for _ in range(self.numHongos):
				self.ind.append(random.randrange( 1 + self.tamProteina - self.tamMotivo))
				pass
			self.poblacion.append(self.ind)
			self.ind = []
			pass
		pass

	# Funcion para evaluacion de la poblacion.
	def fits(self, motif):
		# Comenzamos un ciclo para cada individuo.
		for i in range(self.tamPoblacion):
			con = 0.0
			for j in self.poblacion[i]:
				for k in range(self.tamMotivo):
					if self.Hongos[i][j+k] == '-':
						continue
					else:
						con = self.w[0]*(self.SCIM[self.index[self.Hongos[i][j+k]]][self.index[motif[k]]]) + self.w[1]*(self.CCIM[self.index[self.Hongos[i][j+k]]][self.index[motif[k]]]) + self.w[2]*(self.HCIM[self.index[self.Hongos[i][j+k]]][self.index[motif[k]]]) + con 
						pass
					pass
				pass
			self.fit[i] = con
			pass
		pass

	#### Funciones Auxiliares
	def calculoTotal(self):
		total = 0.0		
		for fi in self.fit:
			total = fi + total
			pass
		return total

	###### Metodos de seleccion. ######

	#### Ruleta simple
	def ruletaSimple(self):
		
		total = self.calculoTotal()	

		# Toma la seleccion por ruleta.
		top = random.random()
		i = 0
		contador = 0.0
		while contador < top and i < self.tamPoblacion-1:
			contador = contador + self.fit[i]/float(total)
			i = i +1
			pass
		return self.poblacion[i]

	#### Ruleta.
	def ruleta(self):

		# Toma la seleccion por ruleta.
		for _ in range((self.tamPoblacion)-(self.numElitismo)):
			self.nuevapoblacion.append(self.ruletaSimple())
			pass

	### Muestreo Estocastico Universal Simple.
	def estocasticoUniversalSimple(self,k=4):
		total = self.calculoTotal()	
		ind = []

		# Toma la seleccion Estocastico Universal con base a la matriz con indice indMatriz
		top = random.random()
		for i in range(k):
			a = (top + i) / k
			ii = 0
			contador = 0.0
			while contador < a and ii < self.tamPoblacion-1:
				contador = contador + abs(self.fit[ii])/float(total)
				ii = ii +1
				pass
			ind.append(self.poblacion[ii])
			pass
		return ind

	### Muestreo Estocastico Universal.
	def estocasticoUniversal(self, k=4):

		# Toma la seleccion Estocastico Universal
		for _ in range(((self.tamPoblacion)-(self.numElitismo))//k):
			ind = self.estocasticoUniversalSimple(k)
			for i in ind:
				self.nuevapoblacion.append(i)
				pass
			pass

		# Toma la seleccion Estocastico Universal
		resK = (((self.tamPoblacion)-(self.numElitismo))%k)
		ind = self.estocasticoUniversalSimple(resK)
		for i in ind:
			self.nuevapoblacion.append(i)
			pass

	### Torneo Simple
	def torneoSimple(self, tamTorneo=4):
		
		num = []

		# Toma la seleccion por toneo con base a la matriz con indice indMatriz
		while len(num) < tamTorneo:
			tem = random.randrange(self.tamPoblacion)
			if not (tem in num):
				num.append(tem)
				pass
			pass
		tor = self.fit[num[0]]
		ind = num[0]
		for i in num:
			if tor < self.fit[i]:
				tor = self.fit[i]
				ind = i
				pass
			pass
		return self.poblacion[ind]

	### Torneo.
	def torneo(self):

		# Toma la seleccion por toneo con base a la matriz de SCIM
		for _ in range((self.tamPoblacion)-(self.numElitismo)):
			self.nuevapoblacion.append(self.torneoSimple(self.tamTorneo))
			pass

		pass

	### Muestreo por Restos Simple.
	def restosSimple(self, numRestos = 1, umbral = 50):

		total = self.calculoTotal()

		media = total / float(self.tamPoblacion)

		# Toma la seleccion por restos
		contador = 0
		for i in range(self.tamPoblacion):
			if self.fit[i] > (media+(media*umbral/100)):
				contador = contador + 1
				pass
			pass
		
		ind = self.elitismoSimple(contador)

		if contador <= numRestos:

			fun = [
					lambda x: self.estocasticoUniversalSimple(1),
					lambda x: self.ruletaSimple(),
					lambda x: self.torneoSimple(self.tamTorneo)
					]

			for _ in range(contador,numRestos):
				tem = random.randrange(3)
				ind.append(fun[tem])
				pass
			pass
		
		return ind[:numRestos]

	### Muestreo por Restos. 
	def restos(self, umbral = 50):

		# Toma la seleccion por restos con base a la matriz de SCIM
		ind = self.restosSimple((self.tamPoblacion)-(self.numElitismo),self.umbral)
		for i in ind:
			self.nuevapoblacion.append(i)
			pass
		pass

	### Elitismo Simple.
	def elitismoSimple(self,numElitismo=10):
		mayorMenor = self.poblacion[:]
		mayorMenorFits = self.fit[:]

		for i in range(1,self.tamPoblacion):
			for j in range(0,self.tamPoblacion - i):
				if(mayorMenorFits[j+1] > mayorMenorFits[j]):
					mayorMenor[j], mayorMenor[j+1] = mayorMenor[j+1], mayorMenor[j]
					mayorMenorFits[j], mayorMenorFits[j+1] = mayorMenorFits[j+1], mayorMenorFits[j] 
					pass
				pass
			pass
		return mayorMenor[:numElitismo]

	def elitismo(self):
		el = self.elitismoSimple(self.numElitismo)
		for x in el:
			self.nuevapoblacion.append(x)
		pass
	###### Metodos de seleccion. Fin ######

	###### Metodos de reproduccion. ######

	# Por Punto fijo.
	def puntoFijo(self):
		for i in range(0,len(self.nuevapoblacion),2):#self.tamPoblacion,2):
			if self.proCruce > random.randrange(100):
				punto = random.randrange(self.numHongos)
				self.nuevapoblacion[i][:punto], self.nuevapoblacion[i+1][:punto] = self.nuevapoblacion[i+1][:punto], self.nuevapoblacion[i][:punto]
				pass
			pass
		pass

	# Por multi-Punto.
	def multiPunto(self):
		for i in range(0,len(self.nuevapoblacion),2):#self.tamPoblacion,2):
			if self.proCruce > random.randrange(100):
				punto = []
				punto.append(random.randrange(50))
				punto.append(random.randrange(50,self.numHongos))
				self.nuevapoblacion[i][:punto[0]], self.nuevapoblacion[i+1][:punto[0]] = self.nuevapoblacion[i+1][:punto[0]], self.nuevapoblacion[i][:punto[0]]
				self.nuevapoblacion[i][punto[1]:], self.nuevapoblacion[i+1][punto[1]:] = self.nuevapoblacion[i+1][punto[1]:], self.nuevapoblacion[i][punto[1]:]
				pass
			pass
		pass
	
	###### Metodos de reproduccion. Fin ######

	###### Mutación ######
	def mutacion(self):
		for i in range(self.tamPoblacion):
			for _ in range(self.canMutacion):
				if self.proMutacion > random.random():
					punto = random.randrange(self.tamProteina)
					self.nuevapoblacion[i][punto] = random.randrange( 1 + self.tamProteina - self.tamMotivo)
					pass
				pass
			pass
		pass
	
	###### Mutación Fin ######

	###### Metodos de Remplazo ######


    # Remplazo aleatorio
	def remplazoPadres(self):
		self.poblacion[:] = self.nuevapoblacion[:]
		self.nuevapoblacion = []
		pass

    # Remplazo de individuos peor adaptados.

    # Remplazo de individuos de adaptación similar

	###### Metodos de Remplazo Fin ######