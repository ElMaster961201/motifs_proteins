import random
from Hongos import Hongos as HG


###### Genetico. ######
class GeneticoPosiciones(object):

	"""
		Inicializamos la clase los parametros que se pueden manupular desde la creacion de la 
		clase son los sigueintes, donde se les asigno un valor por default:
		
		* tamPoblacion = 100
		* numGenomas = 
		* proMutacion = 0.1
		* canMutacion = 2
		* numElitismo = 1
		* knumeros = 4
		* tamTorneo = 4
		* numRestos = 500
		* proCruce = 0.6
		* secuenciaSintetica = []

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
		cruzamientoPuntoFijo
		cruzamientoMultiPunto
		cruzamientoUniforme
		cruzamientoAritmetico

		##### Metodos de Mutacion. ##############################
		mutacionUniforme
		mutacionEstandar

		##### Metodo de Conservacion. ##############################
		elitismo
		conservarMejor

		##### Metodos de Paso de Generacion. ##############################
		remplazoPadres
		remplazoAleatorio
		remplazoPeorAdaptados
		remplazoAdaptacionSimilar
	"""

	""" Es utilizado para ubicar la posicion del aminoacido en las matrices de evaluacion. """	
	index = { 'A':0, 'C':1, 'D':2, 'E':3, 'F':4, 'G':5, 'H':6, 'I':7, 'K':8, 'L':9, 'M':10, 
			  'N':11, 'P':12, 'Q':13, 'R':14, 'S':15, 'T':16, 'V':17, 'W':18, 'Y':19, '-':20 }
	hongos = HG().matrizHongos()
		
	###### Funcion que inicializa la poblacion ######
	def __init__(self, tamPoblacion = 100, numGenomas = 30, proMutacion = 0.1, canMutacion = 2, 
				numElitismo = 1, knumeros = 4, tamTorneo = 4, 
				numRestos = 500, proCruce = 0.6, secuenciaSintetica = []):
		self.tamPoblacion = tamPoblacion
		self.numGenomas = numGenomas
		self.proMutacion = proMutacion
		self.canMutacion = canMutacion
		self.numElitismo = numElitismo
		self.knumeros = knumeros
		self.tamTorneo = tamTorneo
		self.numRestos = numRestos
		self.proCruce = proCruce
		self.secuenciaSintetica = secuenciaSintetica
		self.numHongos = len(self.hongos)
		self.longHongo = len(self.hongos[0])
        # Inicializacion de la poblacion.
		self.poblacion = []
		self.poblacion = [[random.randrange(self.numHongos - self.numGenomas) for _ in range(self.numHongos)] for _ in range(self.tamPoblacion)]
		self.contador = [[0 for _ in range(self.longHongo - self.numGenomas)] for _ in range(self.numHongos)]
		for p in range(self.numHongos):
			for c in range(self.longHongo - self.numGenomas):
				cont = 0
				for i in range(self.numGenomas):
					if self.secuenciaSintetica[i] == self.hongos[p][c + i]:
						cont = cont + 1
						pass
					pass
				self.contador[p][c] = cont
				pass
			pass
		self.nuevapoblacion = []
		self.mejor = [[],0.0,0]
		self.adaptacion = []
		self.adaptacionnuevaploblacion = []
		pass

	###### Funcion que inicializa la poblacion ######

	###### Funciones Auxiliares. ###### 

	#### Ruleta simple.
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

	### Muestreo Estocastico universal simple.
	def estocasticoUniversalSimple(self,knumeros = 4):
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

	### Torneo simple
	def torneoSimple(self, tamTorneo = 4):
		
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

	### Muestreo por Restos simple.
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

	### Elitismo simple.
	def elitismoSimple(self,numElitismo = 10):
		
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

	### Elitismo simple de la nueva poblacion.
	def elitismoSimpleNuevaPoblacion(self,numElitismo = 10):
		
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

	def secuenciaAdaptacion(self,individuo):
		result = []
		for h in range(self.numHongos):
			secuencia = []
			total = 0.0
			secuencia = self.hongos[h][individuo[h]: individuo[h] + self.numGenomas]
			total = float(self.contador[h][individuo[h]])
			result.append([secuencia,total])
			pass
		return result

	###### Funciones Auxiliares. ######

	###### Metodo de evaluacion de la poblacion. ######

	# Funcion para evaluacion de la poblacion.
	def evaluacionPoblacion(self):
		self.adaptacion = []
		# Comenzamos un ciclo para cada individuo.
		for i in range(self.tamPoblacion):
			total = 0.0
			for j in range(self.numHongos):
				total = float((self.w1[j][self.poblacion[i][j]] + self.w2[j][self.poblacion[i][j]] + self.w3[j][self.poblacion[i][j]])) + total
				pass
			total = float(total/self.numHongos)
			self.adaptacion.append(total)
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
			total = 0.0
			for j in range(self.numHongos):
				total = float((self.w1[j][self.nuevapoblacion[i][j]] + self.w2[j][self.nuevapoblacion[i][j]] + self.w3[j][self.nuevapoblacion[i][j]])) + total
				pass
			total = float(total/self.numHongos)
			self.adaptacionnuevapoblacion.append(total)
			pass

	###### Metodo de evaluacion de la poblacion. Fin ######
	 
	###### Metodos de seleccion. ######

	# Ruleta.
	def ruleta(self):

		# Toma la seleccion por ruleta.
		for _ in range(self.tamPoblacion):
			self.nuevapoblacion.append(self.ruletaSimple())
			pass
		pass

	# Muestreo estocastico universal.
	def estocasticoUniversal(self):

		# Ciclo para valores enteros del tamPoblacion/knumeros
		for _ in range(self.tamPoblacion // self.knumeros):
			ind = self.estocasticoUniversalSimple(self.knumeros)
			for i in ind:
				self.nuevapoblacion.append(i)
				pass
			pass
	
		# Ciclo para el residuo obtenido de tamPoblacion/knumeros
		resK = (self.tamPoblacion % self.knumeros)
		ind = self.estocasticoUniversalSimple(resK)
		for i in ind:
			self.nuevapoblacion.append(i)
			pass
		pass

	# Torneo.
	def torneo(self):

		# Toma la seleccion por toneo
		for _ in range(self.tamPoblacion):
			self.nuevapoblacion.append(self.torneoSimple(self.tamTorneo))
			pass
		pass

	# Muestreo por restos. 
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
	def cruzamientoPuntoFijo(self):
		for i in range(0,self.tamPoblacion,2):
			if self.proCruce > random.random():
				punto = random.randrange(3,self.numHongos-3)
				hijo1 = []
				hijo2 = []
				"""
				Los hijos  estan conformados de la siguiente manera.
				hijo1 es padre + madre 
				hijo2 es madre + padre
				Donde: 
				padre es: self.nuevapoblacion[i]
				madre es: self.nuevapoblacion[i + 1]
				"""
				for j in range(0, punto):
					hijo1.append(self.nuevapoblacion[i][j])
					hijo2.append(self.nuevapoblacion[i + 1][j])
					pass

				for j in range(punto, self.numHongos):
					hijo1.append(self.nuevapoblacion[i + 1][j])
					hijo2.append(self.nuevapoblacion[i][j])
					pass 

				self.nuevapoblacion[i] = hijo1
				self.nuevapoblacion[i + 1] = hijo2
				pass
			pass
		pass

	# Por Multipunto.
	def cruzamientoMultiPunto(self):
		for i in range(0,self.tamPoblacion,2):
			if self.proCruce > random.random():
				punto = []
				hijo1 = []
				hijo2 = []
				punto.append(random.randrange(3, int(self.numHongos/2) - 1))
				punto.append(random.randrange(int(self.numHongos/2) + 1, self.numHongos - 3))
				"""
				Los hijos  estan conformados de la siguiente manera.
				hijo1 es padre + madre + padre
				hijo2 es madre + padre + madre
				Donde: 
				padre es: self.nuevapoblacion[i]
				madre es: self.nuevapoblacion[i + 1]
				"""
				for j in range(0, punto[0]):
					hijo1.append(self.nuevapoblacion[i][j])
					hijo2.append(self.nuevapoblacion[i + 1][j])
					pass

				for j in range(punto[0],punto[1]):
					hijo1.append(self.nuevapoblacion[i + 1][j])
					hijo2.append(self.nuevapoblacion[i][j])
					pass

				for j in range(punto[1],self.numHongos):
					hijo1.append(self.nuevapoblacion[i][j])
					hijo2.append(self.nuevapoblacion[i + 1][j])
					pass

				self.nuevapoblacion[i] = hijo1
				self.nuevapoblacion[i + 1] = hijo2
				pass
			pass
		pass

	# Por Cruzamiento uniforme.
	def cruzamientoUniforme(self):
		for i in range(0,self.tamPoblacion,2):
			hijo1 =[]
			hijo2 = []
			for x in range(self.numHongos):
				r = random.random()
				if self.proCruce > r:
					hijo1.append(self.nuevapoblacion[i + 1][x])
					hijo2.append(self.nuevapoblacion[i][x])
					pass
				else:
					hijo1.append(self.nuevapoblacion[i][x])
					hijo2.append(self.nuevapoblacion[i + 1][x])
					pass
				pass
			self.nuevapoblacion[i] = hijo1
			self.nuevapoblacion[i + 1] = hijo2
			pass
		pass
	
	# Por Cruzamiento Aritmetico.
	def cruzamientoAritmetico(self):
		for i in range(0,self.tamPoblacion,2):
			if self.proCruce > random.random():
				hijo1 =[]
				hijo2 = []
				alpha = random.random()
				for x in range(self.numHongos):
					hijo1.append(int ((alpha * self.nuevapoblacion[i][x]) + ((1 - alpha) * self.nuevapoblacion[i + 1][x])))
					hijo2.append(int ((alpha * self.nuevapoblacion[i + 1][x]) + ((1 - alpha) * self.nuevapoblacion[i][x])))
					pass
				self.nuevapoblacion[i] = hijo1
				self.nuevapoblacion[i + 1] = hijo2
				pass
			pass
		pass
	###### Metodos de reproduccion. Fin ######

	###### Mutación ######

	# Mutacion uniforme.
	def mutacionUniforme(self):
		pm = (self.proMutacion * 10)/float(self.numGenomas)
		for i in range(self.tamPoblacion):
			for x in range(self.numHongos):
				r = random.random()
				if r < pm:
					self.nuevapoblacion[i][x] = random.randrange(len(self.hongos[0]) - self.numGenomas)
					pass
				pass
			pass
		pass

	# Mutacion estandar.
	def mutacionEstandar(self):
		for i in range(self.tamPoblacion):
			if self.proMutacion > random.random():
				mut = []
				while len(mut) < self.canMutacion:
					punto = random.randrange(self.numHongos)
					if not (punto in mut):
						mut.append(punto)
						pass
					pass
				for x in mut:
					self.nuevapoblacion[i][x] = random.randrange(len(self.hongos[0]) - self.numGenomas)
					pass
				pass
			pass
		pass
	
	###### Mutación Fin ######

	###### Metodos de Conservacion. ######
	
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
		pass

	# Conservar el mejor.
	def conservarMejor(self, i):
		self.poblacion[i] = self.mejor[0]
		self.nuevapoblacion = []
		self.adaptacionnuevapoblacion = []
		pass

	##### Metodo de Conservacion. Fin ######

	###### Metodos de Paso de generacion. ######

	# Reemplazo de los padres.
	def reemplazoPadres(self):
		self.evaluacionNuevaPoblacion()
		i = self.adaptacionnuevapoblacion.index(min(self.adaptacionnuevapoblacion[:]))
		self.poblacion = self.nuevapoblacion
		self.conservarMejor(i)
		pass

    # Reemplazo aleatorio.
	def reemplazoAleatorio(self):
		for i in range(self.tamPoblacion):
			if random.choice([True,False]):
				self.poblacion[i] = self.nuevapoblacion[i]
				pass
			pass
		self.conservarMejor(random.randrange(self.tamPoblacion))
		pass

    # Reemplazo de los individuos peor adaptados.
	def reemplazoPeorAdaptados(self):
		
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
			pass
		self.conservarMejor(random.randrange(self.tamPoblacion))
		pass

    # Reemplazo de individuos de adaptación similar.
	def reemplazoAdaptacionSimilar(self):
		# Se ordena la poblacion y la nueva generacion 

		poblacionFits = self.adaptacion[:]
		poblacionIndex = []

		self.evaluacionNuevaPoblacion()
		nuevaPoblacionFits = self.adaptacionnuevapoblacion[:]
		nuevaPoblacionIndex = []
		
		# Se ordena los valores de mayor a menor.
		for _ in range(self.tamPoblacion):
			# Se ordena la poblacion.
			poblacionIndex.append(self.adaptacion.index(max(poblacionFits)))
			poblacionFits.remove(max(poblacionFits))

			# Se ordena la nueva poblacion.
			nuevaPoblacionIndex.append(self.adaptacionnuevapoblacion.index(max(nuevaPoblacionFits)))
			nuevaPoblacionFits.remove(max(nuevaPoblacionFits))
			pass

		vecindad = random.randrange(3,6)
		ei = [i for i in range(vecindad)]
		for i in range(0,self.tamPoblacion - vecindad, vecindad):
			self.poblacion[poblacionIndex[i + random.choice(ei)]] = self.nuevapoblacion[nuevaPoblacionIndex[i]]
			pass

		self.conservarMejor(random.randrange(self.tamPoblacion))
		pass

	###### Metodos de Paso de generacion. Fin ######

###### Genetico. Fin ######