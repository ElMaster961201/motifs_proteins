# <------------- Librerias ------------- >
# Generar numeros o selecciones de manera random.
import random
from Motifs import Motifs as MTFS

class Genetico(object):

	"""
		Inicializamos la clase los parametros que se pueden manupular desde la creacion de la 
		clase son los sigueintes, donde se les asigno un valor por default:
		
		* tamPoblacion = 100
		* k = 27
		* proMutacion = 0.1
		* canMutacion = 2
		* numElitismo = 1
		* tamTorneo = 4
		* umbral = 10
		* proCruce = 0.6
		* w = [1/3, 1/3, 1/3]
		* secuencia = []

		Metodos Que pueden ser utilizados por nuestra clase:


		__init__
		control
		fits
		fitsNuevaPoblacion

		##### Metodos de Seleccion. ##############################
		ruletaSimple
		ruleta
		estocasticoUniversalSimple
		estocasticoUniversal
		torneoSimple
		torneo
		restosSimple
		restos
		elitismoSimple
		elitismoSimpleNuevaPoblacion
		elitismo

		##### Metodos de Cruzamiento (Reproduccion). ##############################
		puntoFijo
		multiPunto

		##### Metodos de Mutacion. ##############################
		mutacionUniforme
		mutacionEstandar

		##### Metodos de Paso de Generacion. ##############################
		remplazoPadres
		remplazoAleatorio
		remplazoPeorAdaptados
		remplazoAdaptacionSimilar
	"""

	""" Es utilizado para ubicar la posicion del aminoacido en las matrices de evaluacion. """	
	index = { 'A':0, 'C':1, 'D':2, 'E':3, 'F':4, 'G':5, 'H':6, 'I':7, 'K':8, 'L':9, 'M':10, 'N':11, 'P':12, 'Q':13, 'R':14, 'S':15, 'T':16, 'V':17, 'W':18, 'Y':19 }
	amoniacido = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
	SCIM, CCIM, HCIM = MTFS().SCICCIHCI()
		
	"""Funcion que inicializa la poblacion"""
	def __init__(self, tamPoblacion = 100, k = 27,
        proMutacion = 0.1, canMutacion = 2,numElitismo = 1,tamTorneo = 4, 
		umbral = 10, proCruce = 0.6, w = [1/3, 1/3, 1/3],secuencia = []):
		self.tamPoblacion = tamPoblacion
		self.k = k
		self.proMutacion = proMutacion
		self.canMutacion = canMutacion
		self.numElitismo = numElitismo
		self.tamTorneo = tamTorneo
		self.umbral = umbral
		self.proCruce = proCruce
		self.w = w
		self.secuencia = secuencia
		self.ind = []
		self.poblacion = []
		self.nuevapoblacion = []
		self.mejor = [[],0.0,0]
		self.fit = [0.0 for i in range(tamPoblacion)]
		self.fitnuevapoblacion = []

		for _ in range(self.tamPoblacion):
			self.ind = []
			for _ in range(self.k):
				self.ind.append(random.choice(self.amoniacido))
				pass
			self.poblacion.append(self.ind)
			self.ind = []
			pass
		pass

	# Funcion de control.
	def control(self):
		aux = list(set(self.fit))
		aux.sort()
		return aux
	
	# Funcion de conservacion del mejor.
	def conservacionMejor(self):
		self.fitsNuevaPoblacion()
		aux = self.fitnuevapoblacion[:]
		auxMin = min(aux)
		i = self.fitnuevapoblacion.index(auxMin)
		self.nuevapoblacion[i][:] = self.mejor[0][:] 
		pass 


	# Funcion para evaluacion de la poblacion.
	def fits(self, motif):
		self.secuencia = motif[:]
		self.fit = []
		# Comenzamos un ciclo para cada individuo.
		for i in range(self.tamPoblacion):
			con = 0.0
			for k in range(self.k):
				con = self.w[0]*(self.SCIM[self.index[self.poblacion[i][k]]][self.index[motif[k]]]) + self.w[1]*(self.CCIM[self.index[self.poblacion[i][k]]][self.index[motif[k]]]) + self.w[2]*(self.HCIM[self.index[self.poblacion[i][k]]][self.index[motif[k]]]) + con
				pass
			self.fit.append(con)
			pass

		mejorFits = self.fit[:]

		# Se evita valores repetidos.
		mejorFits = list(set(mejorFits))
		
		# Se obtiene el indice del mejor individuo.
		mejorIndex = self.fit.index(max(mejorFits))

		if (self.mejor[1] >= self.fit[mejorIndex]):
			self.mejor[2] = self.mejor[2] + 1
		else:
			if(self.mejor[1] < self.fit[mejorIndex]):
				self.mejor[0] = self.poblacion[mejorIndex][:]
				self.mejor[1] = self.fit[mejorIndex]
				self.mejor[2] = 0
				pass
			pass
		pass

	# Funcion para evaluacion de la nueva poblacion.
	def fitsNuevaPoblacion(self):

		self.fitnuevapoblacion = []
		# Comenzamos un ciclo para cada individuo.
		for i in range(self.tamPoblacion):
			con = 0.0
			for k in range(self.k):
				con = self.w[0]*(self.SCIM[self.index[self.nuevapoblacion[i][k]]][self.index[self.secuencia[k]]]) + self.w[1]*(self.CCIM[self.index[self.nuevapoblacion[i][k]]][self.index[self.secuencia[k]]]) + self.w[2]*(self.HCIM[self.index[self.nuevapoblacion[i][k]]][self.index[self.secuencia[k]]]) + con
				pass
			self.fitnuevapoblacion.append(con)
			pass
		pass

	###### Metodos de seleccion. ######

	#### Ruleta Simple
	def ruletaSimple(self):
		
		total = sum(self.fit)

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
		for _ in range(self.tamPoblacion):
			self.nuevapoblacion.append(self.ruletaSimple())
			pass

	### Muestreo Estocastico Universal Simple.
	def estocasticoUniversalSimple(self,k=4):
		total = sum(self.fit)
		ind = []

		# Toma la seleccion Estocastico Universal con base a la matriz con indice indMatriz
		top = random.random()
		for i in range(k):
			a = (top + i) / k
			ii = 0
			contador = 0.0
			while contador < a and ii < self.tamPoblacion-1:
				contador = contador + self.fit[ii]/float(total)
				ii = ii +1
				pass
			ind.append(self.poblacion[ii])
			pass
		return ind

	### Muestreo Estocastico Universal.
	def estocasticoUniversal(self, k=4):

		# Toma la seleccion Estocastico Universal
		for _ in range(self.tamPoblacion // k):
			ind = self.estocasticoUniversalSimple(k)
			for i in ind:
				self.nuevapoblacion.append(i)
				pass
			pass

		# Toma la seleccion Estocastico Universal
		resK = (self.tamPoblacion % k)
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
		for _ in range(self.tamPoblacion):
			self.nuevapoblacion.append(self.torneoSimple(self.tamTorneo))
			pass
		pass

	### Muestreo por Restos Simple.
	def restosSimple(self, numRestos = 1, umbral = 50):

		media = sum(self.fit) / float(self.tamPoblacion)
		# Toma la seleccion por restos
		contador = 0
		for i in range(self.tamPoblacion):
			if self.fit[i] > (media+(media*umbral/100)):
				contador = contador + 1
				pass
			pass
		
		index = self.elitismoSimple(contador)

		ind = []
		for i in index:
			ind.append(self.poblacion[i])
			pass

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
	def restos(self):

		# Toma la seleccion por restos
		ind = self.restosSimple(self.tamPoblacion,self.umbral)
		for i in ind:
			self.nuevapoblacion.append(i)
			pass
		pass

	### Elitismo Simple.
	def elitismoSimple(self,numElitismo=10):
		
		mayorMenorFits = self.fit[:]
		mayorMenorIndex = []

		# Se evita valores repetidos.
		mayorMenorFits = list(set(mayorMenorFits))
		
		# Se ordena los valores de mayor a menor.
		for _ in range(len(mayorMenorFits)):
			mayorMenorIndex.append(self.fit.index(max(mayorMenorFits)))
			mayorMenorFits.remove(max(mayorMenorFits))
			pass

		return mayorMenorIndex[:numElitismo]

	# Elitismo Simple de la nueva poblacion.
	def elitismoSimpleNuevaPoblacion(self,numElitismo):
		
		mayorMenorFits = self.fitnuevapoblacion[:]
		mayorMenorIndex = []

		# Se evita valores repetidos.
		mayorMenorFits = list(set(mayorMenorFits))
		
		# Se ordena los valores de mayor a menor.
		for _ in range(len(mayorMenorFits)):
			mayorMenorIndex.append(self.fit.index(max(mayorMenorFits)))
			mayorMenorFits.remove(max(mayorMenorFits))
			pass

		return mayorMenorIndex[:numElitismo]

	def elitismo(self):
		# Obtiene de mayor a menor los indices de los individuos. 
		index = self.elitismoSimple(self.numElitismo)
		self.fitsNuevaPoblacion()

		aux = self.fitnuevapoblacion[:]

		for x in range(len(index)):
			auxMin = min(aux)
			i = self.fitnuevapoblacion.index(auxMin)
			aux.remove(auxMin)
			self.nuevapoblacion[i] = self.poblacion[index[x]]
		pass

	###### Metodos de seleccion. Fin ######

	###### Metodos de reproduccion. ######

	# Por Punto fijo.
	def puntoFijo(self):
		for i in range(0,len(self.nuevapoblacion),2):
			if self.proCruce > random.random():
				punto = random.randrange(3,self.k-3)
				"""
				Los hijos  estan conformados de la siguiente manera.
				hijo1 es padre + madre 
				hijo2 es madre + padre
				Donde: 
				padre es: self.nuevapoblacion[i]
				madre es: self.nuevapoblacion[i + 1]
				"""
				hijo1 = self.nuevapoblacion[i][:punto] + self.nuevapoblacion[i + 1][punto:]
				hijo2 = self.nuevapoblacion[i + 1][:punto] + self.nuevapoblacion[i][punto:]
				self.nuevapoblacion[i] = hijo1
				self.nuevapoblacion[i + 1] = hijo2
				pass
			pass
		pass

	# Por multi-Punto.
	def multiPunto(self):
		for i in range(1,len(self.nuevapoblacion),2):
			if self.proCruce > random.randrange(100):
				punto = []
				punto.append(random.randrange(int(self.k/2)))
				punto.append(random.randrange(int(self.k/2),self.k))
				"""
				Los hijos  estan conformados de la siguiente manera.
				hijo1 es padre + madre + padre
				hijo2 es madre + padre + madre
				Donde: 
				padre es: self.nuevapoblacion[i]
				madre es: self.nuevapoblacion[i + 1]
				"""
				hijo1 = self.nuevapoblacion[i][:punto[0]] + self.nuevapoblacion[i + 1][punto[0]:punto[1]] + self.nuevapoblacion[i][punto[1]:]
				hijo2 = self.nuevapoblacion[i + 1][:punto[0]] + self.nuevapoblacion[i][punto[0]:punto[1]] + self.nuevapoblacion[i + 1][punto[1]:]
				self.nuevapoblacion[i] = hijo1
				self.nuevapoblacion[i + 1] = hijo2
				pass
			pass
		pass
	
	###### Metodos de reproduccion. Fin ######

	###### Mutación ######

	# Mutacion Uniforme.
	def mutacionUniforme(self):
		pm = (self.proMutacion * 10)/float(self.k)
		for i in range(self.tamPoblacion):
			for x in range(self.k):
				r = random.random()
				if r < pm:
					self.nuevapoblacion[i][x] = random.choice(self.amoniacido)
					pass
				pass
			pass
		pass

	# Mutacion Estandar 
	def mutacionEstandar(self):
		for i in range(self.tamPoblacion):
			if self.proMutacion > random.random():
				mut = []
				while len(mut) < self.canMutacion:
					punto = random.randrange(self.k)
					if not (punto in mut):
						mut.append(punto)
						pass
					pass
				for x in mut:
					self.nuevapoblacion[i][x] = random.choice(self.amoniacido)
					pass
				pass
			pass
		pass
	
	###### Mutación Fin ######

	###### Metodos de Remplazo ######

	# Remplazo de los padres.
	def remplazoPadres(self):
		self.conservacionMejor()
		self.poblacion = self.nuevapoblacion
		self.nuevapoblacion = []
		self.fitnuevapoblacion = []
		pass

    # Remplazo aleatorio
	def remplazoAleatorio(self):
		for i in range(self.tamPoblacion):
			if random.choice([True,False]):
				self.poblacion[i] = self.nuevapoblacion[i]
				pass
			pass
		self.poblacion[random.randrange(self.tamPoblacion)] = self.mejor[0]
		self.nuevapoblacion = []
		pass


	# funcion incompleta, modificar 
    # Remplazo de individuos peor adaptados.
	def remplazoPeorAdaptados(self):
		
		media = sum(self.fit) / float(self.tamPoblacion)
		self.fitsNuevaPoblacion()
		mejorFits = self.fitnuevapoblacion[:]
		# Se evita valores repetidos.
		mejorFits = list(set(mejorFits))		

		for i in range(self.tamPoblacion):
			if self.fit[i] < (media - (media*self.umbral/100.0)):
				# Se obtiene el indice del mejor individuo.
				mejorIndex = self.fitnuevapoblacion.index(max(mejorFits))
				mejorFits.remove(max(mejorFits))
				self.poblacion[i] = self.nuevapoblacion[mejorIndex]
				if len(mejorFits) == 0:
					mejorFits = self.fitnuevapoblacion[:]
					# Se evita valores repetidos.
					mejorFits = list(set(mejorFits))
				pass
			pass

    # Remplazo de individuos de adaptación similar
	def remplazoAdaptacionSimilar(self):
		pass

	###### Metodos de Remplazo Fin ######