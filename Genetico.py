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
		
	"""

	""" Es utilizado para ubicar la posicion del aminoacido en las matrices de evaluacion. """	
	index = { 'A':0, 'C':1, 'D':2, 'E':3, 'F':4, 'G':5, 'H':6, 'I':7, 'K':8, 'L':9, 'M':10, 'N':11, 'P':12, 'Q':13, 'R':14, 'S':15, 'T':16, 'V':17, 'W':18, 'Y':19 }
	
	SCIM, CCIM, HCIM = MTFS().SCICCIHCI()
	Hongos = HNS().matrizHongos()
		
	"""Funcion que inicializa la poblacion"""
	def __init__(self, tamPoblacion = 100, tamProteina = 2654,
		tamMotivo = 20,numHongos = 1245,proMutacion = 0.01,
		canMutacion = 2,numElitismo = 10,tamTorneo = 4):
		self.tamPoblacion = tamPoblacion
		self.tamProteina = tamProteina
		self.tamMotivo = tamMotivo
		self.numHongos = numHongos
		self.proMutacion = proMutacion
		self.canMutacion = canMutacion
		self.numElitismo = numElitismo
		self.tamTorneo = tamTorneo
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
			con = [0.0, 0.0, 0.0]
			for j in self.poblacion[i]:
				for k in range(self.tamMotivo):
					if self.Hongos[i][j+k] == '-':
						continue
					else:
						con[0] = self.SCIM[self.index[self.Hongos[i][j+k]]][self.index[motif[k]]] + con[0] 
						con[1] = self.CCIM[self.index[self.Hongos[i][j+k]]][self.index[motif[k]]] + con[1] 
						con[2] = self.HCIM[self.index[self.Hongos[i][j+k]]][self.index[motif[k]]] + con[2] 
						pass
					pass
				pass
			self.fit[i] = con
			pass
		pass

	#### Funciones Auxiliares
	def calculoTotal(self):
		total = [0.0, 0.0, 0.0]		
		for fi in self.fit:
			total[0] = abs(fi[0]) + total[0] 	
			total[1] = abs(fi[1]) + total[1] 
			total[2] = abs(fi[2]) + total[2] 
			pass
		return total

	###### Algoritmos de seleccion. ######

	#### Ruleta simple
	def ruletaSimple(self,indMatriz):
		total = self.calculoTotal()	

		# Toma la seleccion por ruleta con base a la matriz de indMatriz
		top = random.random()
		i = 0
		contador = 0.0
		while contador < top and i < self.tamPoblacion-1:
			contador = contador + abs(self.fit[i][indMatriz])/float(total[indMatriz])
			i = i +1
			pass
		return self.poblacion[i]

	#### Ruleta.
	def ruleta(self):

		total = self.calculoTotal()

		# Toma la seleccion por ruleta con base a la matriz de SCIM
		for _ in range((self.tamPoblacion//3)-(self.numElitismo//3)):
			top = random.random()
			i = 0
			contador = 0.0
			while contador < top and i < self.tamPoblacion-1:
				contador = contador + abs(self.fit[i][0])/float(total[0])
				i = i +1
				pass
			self.nuevapoblacion.append(self.poblacion[i])
			pass
		
		# Toma la seleccion por ruleta con base a la matriz de CCIM
		for _ in range((self.tamPoblacion//3)-(self.numElitismo//3)):
			top = random.random()
			i = 0
			contador = 0.0
			while contador < top and i < self.tamPoblacion-1:
				contador = contador + abs(self.fit[i][1])/float(total[1])
				i = i +1
				pass
			self.nuevapoblacion.append(self.poblacion[i])
			pass

		# Toma la seleccion por ruleta con base a la matriz de HCIM
		for _ in range((self.tamPoblacion//3)-(self.numElitismo//3)):
			top = random.random()
			i = 0
			contador = 0.0
			while contador < top and i < self.tamPoblacion-1:
				contador = contador + abs(self.fit[i][2])/float(total[2])
				i = i +1
				pass
			self.nuevapoblacion.append(self.poblacion[i])
			pass
		pass

	def estocasticoUniversalSimple(self,indMatriz,k=4):
		total = self.calculoTotal()	
		ind = []

		# Toma la seleccion Estocastico Universal con base a la matriz con indice indMatriz
		top = random.random()
		for i in range(k):
			a = (top + i) / k
			ii = 0
			contador = 0.0
			while contador < a and ii < self.tamPoblacion-1:
				contador = contador + abs(self.fit[ii][indMatriz])/float(total[indMatriz])
				ii = ii +1
				pass
			ind.append(self.poblacion[ii])
			pass
		return ind

	### Muestreo Estocastico Universal.
	def estocasticoUniversal(self, k=4):
		
		total = self.calculoTotal()

		# Toma la seleccion Estocastico Universal con base a la matriz de SCIM
		for x in range(((self.tamPoblacion//3)-(self.numElitismo//3))//k):
			top = random.random()	
			for i in range(k):
				a = (top + i) / k
				ii = 0
				contador = 0.0
				while contador < a and ii < self.tamPoblacion-1:
					contador = contador + abs(self.fit[ii][0])/float(total[0])
					ii = ii +1
					pass
				self.nuevapoblacion.append(self.poblacion[ii])
				pass
			pass

		# Toma la seleccion Estocastico Universal con base a la matriz de SCIM
		for x in range(((self.tamPoblacion//3)-(self.numElitismo//3))%k):
			top = random.random()
			a = (top + x) / k
			ii = 0
			contador = 0.0
			while contador < a and ii < self.tamPoblacion-1:
				contador = contador + abs(self.fit[ii][0])/float(total[0])
				ii = ii +1
				pass
			self.nuevapoblacion.append(self.poblacion[ii])
			pass

		# Toma la seleccion Estocastico Universal con base a la matriz de CCIM
		for x in range(((self.tamPoblacion//3)-(self.numElitismo//3))//k):
			top = random.random()
			for i in range(k):
				a = (top + i) / k
				ii = 0
				contador = 0.0
				while contador < a and ii < self.tamPoblacion-1:
					contador = contador + abs(self.fit[ii][1])/float(total[1])
					ii = ii +1
					pass
				self.nuevapoblacion.append(self.poblacion[ii])
				pass
			pass

		# Toma la seleccion Estocastico Universal con base a la matriz de CCIM
		for x in range(((self.tamPoblacion//3)-(self.numElitismo//3))%k):
			top = random.random()
			a = (top + x) / k
			ii = 0
			contador = 0.0
			while contador < a and ii < self.tamPoblacion-1:
				contador = contador + abs(self.fit[ii][1])/float(total[1])
				ii = ii +1
				pass
			self.nuevapoblacion.append(self.poblacion[ii])
			pass

		# Toma la seleccion Estocastico Universal con base a la matriz de HCIM
		for x in range(((self.tamPoblacion//3)-(self.numElitismo//3))//k):
			top = random.random()
			for i in range(k):
				a = (top + i) / k
				ii = 0
				contador = 0.0
				while contador < a and ii < self.tamPoblacion-1:
					contador = contador + abs(self.fit[ii][2])/float(total[2])
					ii = ii +1
					pass
				self.nuevapoblacion.append(self.poblacion[ii])
				pass
			pass
		
		# Toma la seleccion Estocastico Universal con base a la matriz de HCIM
		for x in range(((self.tamPoblacion//3)-(self.numElitismo//3))%k):
			top = random.random()
			a = (top + i) / k
			ii = 0
			contador = 0.0
			while contador < a and ii < self.tamPoblacion-1:
				contador = contador + abs(self.fit[ii][2])/float(total[2])
				ii = ii +1
				pass
			self.nuevapoblacion.append(self.poblacion[ii])
			pass

		pass

	### Torneo Simple
	def torneoSimple(self,indMatriz, tamTorneo=4):
		num = []

		# Toma la seleccion por toneo con base a la matriz con indice indMatriz
		while len(num) < tamTorneo:
			tem = random.randrange(self.tamPoblacion)
			if not (tem in num):
				num.append(tem)
				pass
			pass
		tor = self.fit[num[0]][indMatriz]
		ind = num[0]
		for i in num:
			if tor < self.fit[i][indMatriz]:
				tor = self.fit[i][indMatriz]
				ind = i
				pass
			pass
		return self.poblacion[ind]

	### Torneo.
	def torneo(self):
		num = []

		# Toma la seleccion por toneo con base a la matriz de SCIM
		for _ in range((self.tamPoblacion//3)-(self.numElitismo//3)):
			while len(num) < self.tamTorneo:
				tem = random.randrange(self.tamPoblacion)
				if not (tem in num):
					num.append(tem)
					pass
				pass
			tor = self.fit[num[0]][0]
			ind = num[0]
			for i in num:
				if tor < self.fit[i][0]:
					tor = self.fit[i][0]
					ind = i
					pass
				pass
			self.nuevapoblacion.append(self.poblacion[ind])
			num = []
			pass

		# Toma la seleccion por torneo con base a la matriz de CCIM
		for _ in range((self.tamPoblacion//3)-(self.numElitismo//3)):
			while len(num) < self.tamTorneo:
				tem = random.randrange(self.tamPoblacion)
				if not (tem in num):
					num.append(tem)
					pass
				pass
			tor = self.fit[num[0]][1]
			ind = num[0]
			for i in num:
				if tor < self.fit[i][1]:
					tor = self.fit[i][1]
					ind = i
					pass
				pass
			self.nuevapoblacion.append(self.poblacion[ind])
			num = []
			pass

		# Toma la seleccion por torneo con base a la matriz de HCIM
		for _ in range((self.tamPoblacion//3)-(self.numElitismo//3)):
			while len(num) < self.tamTorneo:
				tem = random.randrange(self.tamPoblacion)
				if not (tem in num):
					num.append(tem)
					pass
				pass
			tor = self.fit[num[0]][2]
			ind = num[0]
			for i in num:
				if tor < self.fit[i][2]:
					tor = self.fit[i][2]
					ind = i
					pass
				pass
			self.nuevapoblacion.append(self.poblacion[ind])
			num = []
			pass
		pass

	### Muestreo por Restos Simple.
	def restosSimple(self,indMatriz, umbral = 50):

		total = self.calculoTotal()

		media = total[indMatriz] / self.tamPoblacion

		# Toma la seleccion por restos con base a la matriz con indice indMatriz
		contador = 0
		for i in range(self.tamPoblacion):
			if abs(self.fit[i][0]) > (media+(media*umbral/100)):
				contador = contador + 1
				pass
			pass
		
		ind = self.elitismo(indMatriz,contador)

		if contador >= 1:
			return ind[0]
		else:
			fun = [
					lambda x: self.estocasticoUniversalSimple(x,1),
					lambda x: self.ruletaSimple(x),
					lambda x: self.torneoSimple(x,self.tamTorneo)
					]
			tem = random.randrange(3)
			return fun[tem](indMatriz)

	### Muestreo por Restos. 
	def restos(self, umbral = 50):

		total = self.calculoTotal()

		media = [total[i]/self.tamPoblacion for i in range(3)]

		# Toma la seleccion por restos con base a la matriz de SCIM
		contador = 0
		for i in range(self.tamPoblacion):
			if abs(self.fit[i][0]) > (media[0]+(media[0]*umbral/100)):
				contador = contador + 1
				pass
			pass
		
		ind = self.elitismo(0,contador)

		if contador >= ((self.tamPoblacion//3)-(self.numElitismo//3)):
			for i in range((self.tamPoblacion//3)-(self.numElitismo//3)):
				self.nuevapoblacion.append(ind[i])
				pass
			pass
		else:
			for x in ind:
				self.nuevapoblacion.append(x)
				pass
			fun = [
					lambda x: self.estocasticoUniversalSimple(x,1),
					lambda x: self.ruletaSimple(x),
					lambda x: self.torneoSimple(x,self.tamTorneo)
					]
			for x in range(contador,((self.tamPoblacion//3)-(self.numElitismo//3))):
				tem = random.randrange(3)
				self.nuevapoblacion.append(fun[tem](0))
				pass
			pass

		# Toma la seleccion por Restos con base a la matriz de CCIM
		contador = 0
		for i in range(self.tamPoblacion):
			if abs(self.fit[i][1]) > (media[1]+(media[1]*umbral/100)):
				contador = contador + 1
				pass
			pass
		
		ind = self.elitismo(1,contador)

		if contador >= ((self.tamPoblacion//3)-(self.numElitismo//3)):
			for i in range((self.tamPoblacion//3)-(self.numElitismo//3)):
				self.nuevapoblacion.append(ind[i])
				pass
			pass
		else:
			for x in ind:
				self.nuevapoblacion.append(x)
				pass
			fun = [
					lambda x: self.estocasticoUniversalSimple(x,1),
					lambda x: self.ruletaSimple(x),
					lambda x: self.torneoSimple(x,self.tamTorneo)
					]
			for x in range(contador,((self.tamPoblacion//3)-(self.numElitismo//3))):
				tem = random.randrange(3)
				self.nuevapoblacion.append(fun[tem](1))
				pass
			pass

		# Toma la seleccion por Restos con base a la matriz de HCIM
		contador = 0
		for i in range(self.tamPoblacion):
			if abs(self.fit[i][2]) > (media[2]+(media[2]*umbral/100)):
				contador = contador + 1
				pass
			pass
		
		ind = self.elitismo(2,contador)

		if contador >= ((self.tamPoblacion//3)-(self.numElitismo//3)):
			for i in range((self.tamPoblacion//3)-(self.numElitismo//3)):
				self.nuevapoblacion.append(ind[i])
				pass
			pass
		else:
			for x in ind:
				self.nuevapoblacion.append(x)
				pass
			fun = [
					lambda x: self.estocasticoUniversalSimple(x,1),
					lambda x: self.ruletaSimple(x),
					lambda x: self.torneoSimple(x,self.tamTorneo)
					]
			for x in range(contador,((self.tamPoblacion//3)-(self.numElitismo//3))):
				tem = random.randrange(3)
				self.nuevapoblacion.append(fun[tem](2))
				pass
			pass
		pass

	def elitismo(self,indMatriz,numElitismo=10):
		mayorMenor = self.poblacion[:]
		mayorMenorFits = self.fit[:]

		for i in range(1,self.tamPoblacion):
			for j in range(0,self.tamPoblacion - i):
				if(abs(mayorMenorFits[j+1][indMatriz]) > abs(mayorMenorFits[j][indMatriz])):
					mayorMenor[j], mayorMenor[j+1] = mayorMenor[j+1], mayorMenor[j]
					mayorMenorFits[j][indMatriz], mayorMenorFits[j+1][indMatriz] = mayorMenorFits[j+1][indMatriz], mayorMenorFits[j][indMatriz] 
					pass
				pass
			pass
		return mayorMenor[:numElitismo]
