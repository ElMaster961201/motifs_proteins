# <------------- Librerias ------------- >
# Generar numeros o selecciones de manera random.
import random
from Motifs import Motifs as MTFS

###### Genetico. ######
class Genetico(object):

	"""
		Inicializamos la clase los parametros que se pueden manupular desde la creacion de la 
		clase son los sigueintes, donde se les asigno un valor por default:
		
		* tamPoblacion = 100
		* k = 27
		* proMutacion = 0.1
		* canMutacion = 2
		* numElitismo = 1
		* knumeros = 4
		* tamTorneo = 4
		* numRestos = 500
		* proCruce = 0.6
		* w = [1/3, 1/3, 1/3]
		* secuencia = []

		Metodos que contiene la clase:


		__init__

		##### Metodos de Evaluacion de la poblacion. ##############################
		evaluacionPoblacion
		evaluacionNuevaPoblacion

		##### Funciones Auxiliares. ##############################
		ruletaSimple
		estocasticoUniversalSimple
		torneoSimple
		restosSimple
		elitismoSimple
		elitismoSimpleNuevaPoblacion

		##### Metodos de Seleccion. ##############################
		ruleta
		estocasticoUniversal
		torneo
		restos

		##### Metodos de Cruzamiento (Reproduccion). ##############################
		puntoFijo
		multiPunto

		##### Metodos de Mutacion. ##############################
		mutacionUniforme
		mutacionEstandar

		##### Metodo de Conservacion. ##############################
		elitismo

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
		
	###### Funcion que inicializa la poblacion ######
	def __init__(self, tamPoblacion = 100, k = 27,
        proMutacion = 0.1, canMutacion = 2, numElitismo = 1, knumeros = 4, tamTorneo = 4, 
		numRestos = 500, proCruce = 0.6, w = [1/3, 1/3, 1/3], secuencia = []):
		self.tamPoblacion = tamPoblacion
		self.k = k
		self.proMutacion = proMutacion
		self.canMutacion = canMutacion
		self.numElitismo = numElitismo
		self.knumeros = knumeros
		self.tamTorneo = tamTorneo
		self.numRestos = numRestos
		self.proCruce = proCruce
		self.w = w
		self.secuencia = secuencia
		# Inicializacion de la poblacion.
		self.poblacion = [[random.choice(self.amoniacido) for _ in range(self.k) ] for _ in range(self.tamPoblacion)]
		self.nuevapoblacion = []
		self.mejor = [[],0.0,0]
		self.adaptacion = []
		self.adaptacionnuevapoblacion = []

		pass

	###### Funcion que inicializa la poblacion ######

	###### Funciones Auxiliares. ###### 

	#### Ruleta Simple.
	def ruletaSimple(self):
		
		total = sum(self.adaptacion)

		# Toma la seleccion por ruleta.
		top = random.random()
		i = 0
		contador = 0.0
		while contador < top and i < self.tamPoblacion-1:
			contador = contador + self.adaptacion[i]/float(total)
			i = i +1
			pass
		return self.poblacion[i]

	### Muestreo Estocastico Universal Simple.
	def estocasticoUniversalSimple(self,knumeros=4):
		total = sum(self.adaptacion)
		ind = []

		# Toma la seleccion estocastico universal con base a la matriz con indice indMatriz
		top = random.random()
		for i in range(knumeros):
			a = (top + i) / knumeros
			ii = 0
			contador = 0.0
			while contador < a and ii < self.tamPoblacion-1:
				contador = contador + self.adaptacion[ii]/float(total)
				ii = ii +1
				pass
			ind.append(self.poblacion[ii])
			pass
		return ind

	### Torneo Simple
	def torneoSimple(self, tamTorneo=4):
		
		num = []

		while len(num) < tamTorneo:
			tem = random.randrange(self.tamPoblacion)
			if not (tem in num):
				num.append(tem)
				pass
			pass
		tor = self.adaptacion[num[0]]
		ind = num[0]
		for i in num:
			if tor < self.adaptacion[i]:
				tor = self.adaptacion[i]
				ind = i
				pass
			pass
		return self.poblacion[ind]

	### Muestreo por Restos Simple.
	def restosSimple(self, numRestos = 500):

		# Toma la seleccion por restos
		ind = []
		for i in range(self.tamPoblacion):
			pi = int((self.adaptacion[i]/sum(self.adaptacion)*numRestos))
			for _ in range(pi):
				ind.append(self.poblacion[i])
				pass
			pass

		if len(ind) < self.tamPoblacion:

			fun = [
					lambda _: self.estocasticoUniversalSimple(1),
					lambda _: self.ruletaSimple(),
					lambda _: self.torneoSimple(self.tamTorneo)
					]

			for _ in range(len(ind),self.tamPoblacion):
				tem = random.randrange(3)
				if tem == 0:
					ind.append(fun[tem](0)[0]) 
				else:
					ind.append(fun[tem](0))
					pass
				pass
			pass
		return ind[:self.tamPoblacion]

	### Elitismo Simple.
	def elitismoSimple(self,numElitismo=10):
		
		mayorMenorFits = self.adaptacion[:]
		mayorMenorIndex = []

		# Se evita valores repetidos.
		mayorMenorFits = list(set(mayorMenorFits))
		
		# Se ordena los valores de mayor a menor.
		for _ in range(len(mayorMenorFits)):
			mayorMenorIndex.append(self.adaptacion.index(max(mayorMenorFits)))
			mayorMenorFits.remove(max(mayorMenorFits))
			pass

		return mayorMenorIndex[:numElitismo]

	### Elitismo Simple de la nueva poblacion.
	def elitismoSimpleNuevaPoblacion(self,numElitismo):
		
		mayorMenorFits = self.adaptacionnuevapoblacion[:]
		mayorMenorIndex = []

		# Se evita valores repetidos.
		mayorMenorFits = list(set(mayorMenorFits))
		
		# Se ordena los valores de mayor a menor.
		for _ in range(len(mayorMenorFits)):
			mayorMenorIndex.append(self.adaptacionnuevapoblacion.index(max(mayorMenorFits)))
			mayorMenorFits.remove(max(mayorMenorFits))
			pass

		return mayorMenorIndex[:numElitismo]

	###### Funciones Auxiliares. ######

	###### Metodo de evaluacion de la poblacion. ######

	# Funcion para evaluacion de la poblacion.
	def evaluacionPoblacion(self, motif):
		self.secuencia = motif[:]
		self.adaptacion = []
		# Comenzamos un ciclo para cada individuo.
		for i in range(self.tamPoblacion):
			con = 0.0
			for k in range(self.k):
				con = self.w[0]*(self.SCIM[self.index[self.poblacion[i][k]]][self.index[motif[k]]]) + self.w[1]*(self.CCIM[self.index[self.poblacion[i][k]]][self.index[motif[k]]]) + self.w[2]*(self.HCIM[self.index[self.poblacion[i][k]]][self.index[motif[k]]]) + con
				pass
			self.adaptacion.append(con)
			pass

		mejorAdaptacion = self.adaptacion[:]

		# Se evita valores repetidos.
		mejorAdaptacion = list(set(mejorAdaptacion))
		
		# Se obtiene el indice del mejor individuo.
		mejorIndex = self.adaptacion.index(max(mejorAdaptacion))

		if (self.mejor[1] >= self.adaptacion[mejorIndex]):
			self.mejor[2] = self.mejor[2] + 1
		else:
			if(self.mejor[1] < self.adaptacion[mejorIndex]):
				self.mejor[0] = self.poblacion[mejorIndex][:]
				self.mejor[1] = self.adaptacion[mejorIndex]
				self.mejor[2] = 0
				pass
			pass
		pass

	# Funcion para evaluacion de la nueva poblacion.
	def evaluacionNuevaPoblacion(self):

		self.adaptacionnuevapoblacion = []
		# Comenzamos un ciclo para cada individuo.
		for i in range(self.tamPoblacion):
			con = 0.0
			for k in range(self.k):
				con = self.w[0]*(self.SCIM[self.index[self.nuevapoblacion[i][k]]][self.index[self.secuencia[k]]]) + self.w[1]*(self.CCIM[self.index[self.nuevapoblacion[i][k]]][self.index[self.secuencia[k]]]) + self.w[2]*(self.HCIM[self.index[self.nuevapoblacion[i][k]]][self.index[self.secuencia[k]]]) + con
				pass
			self.adaptacionnuevapoblacion.append(con)
			pass
		pass

	###### Metodo de evaluacion de la poblacion. Fin ######
	 
	###### Metodos de seleccion. ######

	# Ruleta.
	def ruleta(self):

		# Toma la seleccion por ruleta.
		for _ in range(self.tamPoblacion):
			self.nuevapoblacion.append(self.ruletaSimple())
			pass

	# Muestreo Estocastico Universal.
	def estocasticoUniversal(self):

		# Toma la seleccion Estocastico Universal
		for _ in range(self.tamPoblacion // self.knumeros):
			ind = self.estocasticoUniversalSimple(self.knumeros)
			for i in ind:
				self.nuevapoblacion.append(i)
				pass
			pass

		# Toma la seleccion Estocastico Universal
		resK = (self.tamPoblacion % self.knumeros)
		ind = self.estocasticoUniversalSimple(resK)
		for i in ind:
			self.nuevapoblacion.append(i)
			pass

	# Torneo.
	def torneo(self):

		# Toma la seleccion por toneo con base a la matriz de SCIM
		for _ in range(self.tamPoblacion):
			self.nuevapoblacion.append(self.torneoSimple(self.tamTorneo))
			pass
		pass

	# Muestreo por Restos. 
	def restos(self):

		# Toma la seleccion por restos
		ind = self.restosSimple(self.numRestos)
		for i in ind:
			self.nuevapoblacion.append(i)
			pass
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

	# Mutacion Estandar.
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

	###### Metodo de Conservacion. ######
	
	# Elitismo.
	def elitismo(self):
		# Obtiene de mayor a menor los indices de los individuos. 
		index = self.elitismoSimple(self.numElitismo)
		self.evaluacionNuevaPoblacion()

		aux = self.adaptacionnuevapoblacion[:]

		for x in range(len(index)):
			auxMin = min(aux)
			i = self.adaptacionnuevapoblacion.index(auxMin)
			aux.remove(auxMin)
			self.nuevapoblacion[i] = self.poblacion[index[x]]
		pass

	##### Metodo de Conservacion. Fin ######

	###### Metodos de Paso de generacion. ######

	# Remplazo de los padres.
	def remplazoPadres(self):
		self.evaluacionNuevaPoblacion()
		i = self.adaptacionnuevapoblacion.index(min(self.adaptacionnuevapoblacion[:]))
		self.nuevapoblacion[i] = self.mejor[0]
		self.poblacion = self.nuevapoblacion
		self.nuevapoblacion = []
		self.adaptacionnuevapoblacion = []
		pass

    # Remplazo aleatorio.
	def remplazoAleatorio(self):
		for i in range(self.tamPoblacion):
			if random.choice([True,False]):
				self.poblacion[i] = self.nuevapoblacion[i]
				pass
			pass
		self.poblacion[random.randrange(self.tamPoblacion)] = self.mejor[0]
		self.nuevapoblacion = []
		self.adaptacionnuevapoblacion = []
		pass

    # Remplazo de individuos peor adaptados.
	def remplazoPeorAdaptados(self):
		
		media = sum(self.adaptacion) / float(self.tamPoblacion)
		
		self.evaluacionNuevaPoblacion()
		mejorFits = self.adaptacionnuevapoblacion[:]
		# Se evita valores repetidos.
		mejorFits = list(set(mejorFits))		

		for i in range(self.tamPoblacion):
			if self.adaptacion[i] < (media - (media*0.1)):
				# Se obtiene el indice del mejor individuo.
				mejorIndex = self.adaptacionnuevapoblacion.index(max(mejorFits))
				mejorFits.remove(max(mejorFits))
				self.poblacion[i] = self.nuevapoblacion[mejorIndex]
				if len(mejorFits) == 0:
					mejorFits = self.adaptacionnuevapoblacion[:]
					# Se evita valores repetidos.
					mejorFits = list(set(mejorFits))
				pass
			pass
		self.poblacion[random.randrange(self.tamPoblacion)] = self.mejor[0]
		self.nuevapoblacion = []
		self.adaptacionnuevapoblacion = []
		pass

    # Remplazo de individuos de adaptación similar.
	def remplazoAdaptacionSimilar(self):
		# Se ordena la poblacion y la nueva generacion 

		poblacionFits = self.adaptacion[:]
		poblacionIndex = []

		self.evaluacionNuevaPoblacion()
		nuevaPoblacionFits = self.adaptacionnuevapoblacion[:]
		nuevaPoblacionIndex = []
		
		# Se ordena los valores de mayor a menor.
		for _ in range(len(poblacionFits)):
			# Se ordena la poblacion.
			poblacionIndex.append(self.adaptacion.index(max(poblacionFits)))
			poblacionFits.remove(max(poblacionFits))

			# Se ordena la nueva poblacion.
			nuevaPoblacionIndex.append(self.adaptacionnuevapoblacion.index(max(nuevaPoblacionFits)))
			nuevaPoblacionFits.remove(max(nuevaPoblacionFits))

			pass

		vecindad = random.randrange(3,6)
		ei = [i for i in range(vecindad)]
		for i in range(0,self.tamPoblacion - vecindad,vecindad):
			self.poblacion[poblacionIndex[i + random.choice(ei)]] = self.nuevapoblacion[nuevaPoblacionIndex[i]]
			pass

		self.poblacion[random.randrange(self.tamPoblacion)] = self.mejor[0]
		self.nuevapoblacion = []
		self.adaptacionnuevapoblacion = []
		pass

	###### Metodos de Paso de generacion. Fin ######

###### Genetico. Fin ######