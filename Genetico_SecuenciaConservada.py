import random
from Hongos import Hongos as HG 

###### Genetico. ######
class GeneticoSecuenciaConservada(object):

	"""
		Inicializamos la clase los parametros que se pueden manupular desde la creacion de la 
		clase son los sigueintes, donde se les asigno un valor por default:
		
		* tam_poblacion = 100
		* num_genomas = 30
		* num_secuencias_conservadas = 20
		* pro_mutacion = 0.1
		* can_mutacion = 2
		* num_elitismo = 1
		* eunumeros = 4
		* tam_torneo = 4
		* num_restos = 500
		* pro_cruce = 0.6

		Metodos que contiene la clase:


		__init__

		##### Metodos de Evaluacion de la poblacion. ##############################
		evaluacion_poblacion
		evaluacion_nueva_poblacion

		##### Funciones Auxiliares. ##############################
		ruleta_simple
		estocastico_universal_simple
		torneo_simple
		restos_simple
		elitismo_simple
		elitismo_simple_nueva_poblacion
		valida_poblacion

		##### Metodos de Seleccion. ##############################
		ruleta
		estocastico_universal
		torneo
		restos

		##### Metodos de Cruzamiento (Reproduccion). ##############################
		cruzamiento_monopunto
		cruzamiento_multipunto
		cruzamiento_uniforme
		cruzamiento_aritmetico

		##### Metodos de Mutacion. ##############################
		mutacion_uniforme
		mutacion_estandar

		##### Metodo de Conservacion. ##############################
		elitismo
		conservar_mejor

		##### Metodos de Paso de Generacion. ##############################
		remplazoPadres
		remplazoAleatorio
		remplazoPeorAdaptados
		remplazoAdaptacionSimilar
	"""

	""" Es utilizado para ubicar la posicion del aminoacido en las matrices de evaluacion. """	
	index = { 'A':0, 'C':1, 'D':2, 'E':3, 'F':4, 'G':5, 'H':6, 'I':7, 'K':8, 'L':9, 'M':10, 'N':11, 'P':12, 'Q':13, 'R':14, 'S':15, 'T':16, 'V':17, 'W':18, 'Y':19, '-':20 }
	hongos = HG().matriz_hongos()
		
	###### Funcion que inicializa la poblacion ######
	def __init__(self, parametros = [100,30,20,0.1,2,1,4,4,500,0.6]):
		self.tam_poblacion = parametros[0]
		self.num_genomas = parametros[1]
		self.num_secuencias_conservadas = parametros[2]
		self.pro_mutacion = parametros[3]
		self.can_mutacion = parametros[4]
		self.num_elitismo = parametros[5]
		self.eunumeros = parametros[6]
		self.tam_torneo = parametros[7]
		self.num_restos = parametros[8]
		self.pro_cruce = parametros[9]
		self.con_sec = []
        # Inicializamos el contador.
		self.contador = [[0 for _ in range(len(self.index))] for _ in range(len(self.hongos[0]))]
		for i in range(len(self.hongos[0])):
			for j in range(len(self.hongos)):
				self.contador[i][self.index[self.hongos[j][i]]] = self.contador[i][self.index[self.hongos[j][i]]] + 1

		for i in range(len(self.hongos[0]) - self.num_genomas):
			sec = []
			sum_sec_con = 0.0
			for am in range(self.num_genomas):
				index = self.contador[i + am].index(max(self.contador[i + am]))
				if index == 20:
					self.contador[i + am].pop(index)
					index = self.contador[i + am].index(max(self.contador[i + am]))
				sum_sec_con = sum_sec_con + max(self.contador[i + am])
				sec.append(list(self.index.keys())[index])
			self.con_sec.append([sec, 100 * float(sum_sec_con)/(self.num_genomas * len(self.hongos) * self.num_secuencias_conservadas)])

        # Inicializacion de la poblacion.
		self.poblacion = []
		self.poblacion = [[self.valida_poblacion(self.poblacion, random.randrange(len(self.hongos[0]) - self.num_genomas)) for _ in range(self.num_secuencias_conservadas)] for _ in range(self.tam_poblacion)]
		self.nuevapoblacion = []
		self.mejor = [[], 0.0, 0]
		self.adaptacion = []
		self.adaptacionnuevaploblacion = []

	###### Funcion que inicializa la poblacion ######

	###### Funciones Auxiliares. ###### 

	#### Ruleta simple.
	def ruleta_simple(self):
		
		total = sum(self.adaptacion)

		# Toma la seleccion por ruleta.
		top = random.random()
		i = 0
		contador = 0.0
		while contador < top and i < self.tam_poblacion - 1:
			contador = contador + self.adaptacion[i]/float(total)
			i = i + 1
		return self.poblacion[i]

	### Muestreo Estocastico universal simple.
	def estocastico_universal_simple(self, eunumeros = 4):
		total = sum(self.adaptacion)
		ind = []

		# Toma la seleccion estocastico universal con base a la matriz con indice indMatriz
		top = random.random()
		ii = 0
		contador = 0.0
		for i in range(eunumeros):
			a = (top + i)/eunumeros
			while contador < a and ii < self.tam_poblacion - 1:
				contador = contador + self.adaptacion[ii]/float(total)
				ii = ii + 1
			ind.append(self.poblacion[ii])
		return ind

	### Torneo simple
	def torneo_simple(self, tam_torneo = 4):
		
		num = []

		while len(num) < tam_torneo:
			tem = random.randrange(self.tam_poblacion)
			if not (tem in num):
				num.append(tem)
		tor = self.adaptacion[num[0]]
		ind = num[0]
		for i in num:
			if tor < self.adaptacion[i]:
				tor = self.adaptacion[i]
				ind = i
		return self.poblacion[ind]

	### Muestreo por Restos simple.
	def restos_simple(self, num_restos = 500):

		# Toma la seleccion por restos
		ind = []
		for i in range(self.tam_poblacion):
			pi = int((self.adaptacion[i]/sum(self.adaptacion) * num_restos))
			for _ in range(pi):
				ind.append(self.poblacion[i])

		if len(ind) < self.tam_poblacion:

			fun = [
					lambda _: self.estocastico_universal_simple(1),
					lambda _: self.ruleta_simple(),
					lambda _: self.torneo_simple(self.tam_torneo)
					]

			for _ in range(len(ind), self.tam_poblacion):
				tem = random.randrange(3)
				if tem == 0:
					ind.append(fun[tem](0)[0]) 
				else:
					ind.append(fun[tem](0))
		return ind[:self.tam_poblacion]

	### Elitismo simple.
	def elitismo_simple(self, num_elitismo = 10):
		
		mayor_menor_fits = self.adaptacion[:]
		mayor_menor_index = []

		# Se evita valores repetidos.
		mayor_menor_fits = list(set(mayor_menor_fits))
		
		# Se ordena los valores de mayor a menor.
		for _ in range(len(mayor_menor_fits)):
			mayor_menor_index.append(self.adaptacion.index(max(mayor_menor_fits)))
			mayor_menor_fits.remove(max(mayor_menor_fits))

		return mayor_menor_index[:num_elitismo]

	### Elitismo simple de la nueva poblacion.
	def elitismo_simple_nueva_poblacion(self, num_elitismo = 10):
		
		mayor_menor_fits = self.adaptacionnuevapoblacion[:]
		mayor_menor_index = []

		# Se evita valores repetidos.
		mayor_menor_fits = list(set(mayor_menor_fits))
		
		# Se ordena los valores de mayor a menor.
		for _ in range(len(mayor_menor_fits)):
			mayor_menor_index.append(self.adaptacionnuevapoblacion.index(max(mayor_menor_fits)))
			mayor_menor_fits.remove(max(mayor_menor_fits))

		return mayor_menor_index[:num_elitismo]

	### Validacion de la poblacion para evitar genomas repetidos.
	def valida_poblacion(self, individuo, genoma):
		t = True
		ind = 0
		while t:
			for i in individuo:
				ind = ind + 1
				if (genoma > i - self.num_genomas and genoma < i + self.num_genomas):
					genoma = random.randrange(len(self.hongos[0]) - self.num_genomas)
					ind = 0
					break
			if (ind == len(individuo)):
				t = False
		return genoma 

	def secuencia_adaptacion(self, individuo):
		result = []
		for ind in individuo:
			secuencia = []
			total = 0.0
			for i in range(self.num_genomas):
				index = self.contador[i + ind].index(max(self.contador[i + ind]))
				if index == 20:
					self.contador[i + ind].pop(index)
					index = self.contador[i + ind].index(max(self.contador[i + ind]))
				total = total + max(self.contador[i + ind])
				secuencia.append(list(self.index.keys())[index])
			total = 100 * float(total)/(self.num_genomas * len(self.hongos))
			result.append([secuencia, total])
		return result

	###### Funciones Auxiliares. ######

	###### Metodo de evaluacion de la poblacion. ######

	# Funcion para evaluacion de la poblacion.
	def evaluacion_poblacion(self):
		self.adaptacion = []
		# Comenzamos un ciclo para cada individuo.
		for individuo in self.poblacion:
			sum_total = 0.0
			for genoma in individuo:
				sum_total = sum_total + self.con_sec[genoma][1]
			self.adaptacion.append(sum_total)

		mejor_adaptacion = self.adaptacion[:]

		# Se evita valores repetidos.
		mejor_adaptacion = list(set(mejor_adaptacion))
		
		# Se obtiene el indice del mejor individuo.
		mejor_index = self.adaptacion.index(max(mejor_adaptacion))

		if (self.mejor[1] >= self.adaptacion[mejor_index]):
			self.mejor[2] = self.mejor[2] + 1
		else:
			if(self.mejor[1] < self.adaptacion[mejor_index]):
				self.mejor[0] = self.poblacion[mejor_index][:]
				self.mejor[1] = self.adaptacion[mejor_index]
				self.mejor[2] = 0

	# Funcion para evaluacion de la nueva poblacion.
	def evaluacion_nueva_poblacion(self):

		self.adaptacionnuevapoblacion = []
		# Comenzamos un ciclo para cada individuo.
		for individuo in self.poblacion:
			sum_total = 0.0
			for genoma in individuo:
				sum_total = sum_total + self.con_sec[genoma][1]
			self.adaptacionnuevapoblacion.append(sum_total)

	###### Metodo de evaluacion de la poblacion. Fin ######
	 
	###### Metodos de seleccion. ######

	# Ruleta.
	def ruleta(self):

		# Toma la seleccion por ruleta.
		for _ in range(self.tam_poblacion):
			self.nuevapoblacion.append(self.ruleta_simple())

	# Muestreo estocastico universal.
	def estocastico_universal(self):

		# Ciclo para valores enteros del tam_poblacion/eunumeros
		for _ in range(self.tam_poblacion // self.eunumeros):
			ind = self.estocastico_universal_simple(self.eunumeros)
			for i in ind:
				self.nuevapoblacion.append(i)
	
		# Ciclo para el residuo obtenido de tam_poblacion/eunumeros
		res_k = (self.tam_poblacion % self.eunumeros)
		ind = self.estocastico_universal_simple(res_k)
		for i in ind:
			self.nuevapoblacion.append(i)

	# Torneo.
	def torneo(self):

		# Toma la seleccion por toneo
		for _ in range(self.tam_poblacion):
			self.nuevapoblacion.append(self.torneo_simple(self.tam_torneo))

	# Muestreo por restos. 
	def restos(self):

		# Toma la seleccion por restos
		ind = self.restos_simple(self.num_restos)
		for i in ind:
			self.nuevapoblacion.append(i)

	###### Metodos de seleccion. Fin ######

	###### Metodos de cruzamiento. ######

	# cruzamiento monopunto.
	def cruzamiento_monopunto(self):
		for i in range(0, self.tam_poblacion, 2):
			if self.pro_cruce > random.random():
				punto = random.randrange(3, self.num_secuencias_conservadas - 3)
				hijo1 = []
				hijo2 = []
				"""
				Los hijos estan conformados de la siguiente manera.
				hijo1 es padre + madre 
				hijo2 es madre + padre
				Donde: 
				padre es: self.nuevapoblacion[i]
				madre es: self.nuevapoblacion[i + 1]
				"""
				for j in range(0, punto):
					hijo1.append(self.valida_poblacion(hijo1, self.nuevapoblacion[i][j]))
					hijo2.append(self.valida_poblacion(hijo2, self.nuevapoblacion[i + 1][j]))

				for j in range(punto, self.num_secuencias_conservadas):
					hijo1.append(self.valida_poblacion(hijo1, self.nuevapoblacion[i + 1][j]))
					hijo2.append(self.valida_poblacion(hijo2, self.nuevapoblacion[i][j]))

				self.nuevapoblacion[i] = hijo1
				self.nuevapoblacion[i + 1] = hijo2

	# Cruzamiento Multipunto.
	def cruzamiento_multipunto(self):
		for i in range(0, self.tam_poblacion, 2):
			if self.pro_cruce > random.random():
				punto = []
				hijo1 = []
				hijo2 = []
				punto.append(random.randrange(3, int(self.num_secuencias_conservadas/2) - 1))
				punto.append(random.randrange(int(self.num_secuencias_conservadas/2) + 1, self.num_secuencias_conservadas - 3))
				"""
				Los hijos estan conformados de la siguiente manera.
				hijo1 es padre + madre + padre
				hijo2 es madre + padre + madre
				Donde: 
				padre es: self.nuevapoblacion[i]
				madre es: self.nuevapoblacion[i + 1]
				"""
				for j in range(0, punto[0]):
					hijo1.append(self.valida_poblacion(hijo1, self.nuevapoblacion[i][j]))
					hijo2.append(self.valida_poblacion(hijo2, self.nuevapoblacion[i + 1][j]))

				for j in range(punto[0], punto[1]):
					hijo1.append(self.valida_poblacion(hijo1, self.nuevapoblacion[i + 1][j]))
					hijo2.append(self.valida_poblacion(hijo2, self.nuevapoblacion[i][j]))

				for j in range(punto[1], self.num_secuencias_conservadas):
					hijo1.append(self.valida_poblacion(hijo1, self.nuevapoblacion[i][j]))
					hijo2.append(self.valida_poblacion(hijo2, self.nuevapoblacion[i + 1][j]))

				self.nuevapoblacion[i] = hijo1
				self.nuevapoblacion[i + 1] = hijo2

	# Cruzamiento uniforme.
	def cruzamiento_uniforme(self):
		for i in range(0, self.tam_poblacion, 2):
			hijo1 =[]
			hijo2 = []
			for x in range(self.num_secuencias_conservadas):
				r = random.random()
				if self.pro_cruce > r:
					hijo1.append(self.valida_poblacion(hijo1, self.nuevapoblacion[i + 1][x]))
					hijo2.append(self.valida_poblacion(hijo2, self.nuevapoblacion[i][x]))
				else:
					hijo1.append(self.valida_poblacion(hijo1, self.nuevapoblacion[i][x]))
					hijo2.append(self.valida_poblacion(hijo2, self.nuevapoblacion[i + 1][x]))
			self.nuevapoblacion[i] = hijo1
			self.nuevapoblacion[i + 1] = hijo2
	
	# Cruzamiento Aritmetico.
	def cruzamiento_aritmetico(self):
		for i in range(0, self.tam_poblacion, 2):
			if self.pro_cruce > random.random():
				hijo1 =[]
				hijo2 = []
				alpha = random.random()
				for x in range(self.num_secuencias_conservadas):
					hijo1.append(self.valida_poblacion(hijo1, int ((alpha * self.nuevapoblacion[i][x]) + ((1 - alpha) * self.nuevapoblacion[i + 1][x]))))
					hijo2.append(self.valida_poblacion(hijo2, int ((alpha * self.nuevapoblacion[i + 1][x]) + ((1 - alpha) * self.nuevapoblacion[i][x]))))
				self.nuevapoblacion[i] = hijo1
				self.nuevapoblacion[i + 1] = hijo2
	###### Metodos de cruzamiento. Fin ######

	###### Mutación ######

	# Mutacion uniforme.
	def mutacion_uniforme(self):
		pm = float(self.pro_mutacion/float(self.num_genomas))
		for i in range(self.tam_poblacion):
			for x in range(self.num_secuencias_conservadas):
				r = random.random()
				if r < pm:
					self.nuevapoblacion[i][x] = self.valida_poblacion(self.nuevapoblacion[i], random.randrange(len(self.hongos[0]) - self.num_genomas))

	# Mutacion estandar.
	def mutacion_estandar(self):
		for i in range(self.tam_poblacion):
			if self.pro_mutacion > random.random():
				mut = []
				while len(mut) < self.can_mutacion:
					punto = random.randrange(self.num_secuencias_conservadas)
					if not (punto in mut):
						mut.append(punto)
				for x in mut:
					self.nuevapoblacion[i][x] = self.valida_poblacion(self.nuevapoblacion[i], random.randrange(len(self.hongos[0]) - self.num_genomas))
	
	###### Mutación Fin ######

	###### Metodos de Conservacion. ######
	
	# Elitismo.
	def elitismo(self):
		# Obtiene de mayor a menor los indices de los individuos. 
		index = self.elitismo_simple(self.num_elitismo)
		self.evaluacion_nueva_poblacion()

		aux = self.adaptacionnuevapoblacion[:]

		for x in range(len(index)):
			aux_min = min(aux)
			i = self.adaptacionnuevapoblacion.index(aux_min)
			aux.remove(aux_min)
			self.nuevapoblacion[i] = self.poblacion[index[x]]

	# Conservar el mejor.
	def conservar_mejor(self, i):
		self.poblacion[i] = self.mejor[0]
		self.nuevapoblacion = []
		self.adaptacionnuevapoblacion = []

	##### Metodo de Conservacion. Fin ######

	###### Metodos de Paso de generacion. ######

	# Reemplazo de los padres.
	def reemplazo_padres(self):
		self.evaluacion_nueva_poblacion()
		i = self.adaptacionnuevapoblacion.index(min(self.adaptacionnuevapoblacion[:]))
		self.poblacion = self.nuevapoblacion
		self.conservar_mejor(i)

    # Reemplazo aleatorio.
	def reemplazo_aleatorio(self):
		for i in range(self.tam_poblacion):
			if random.choice([True, False]):
				self.poblacion[i] = self.nuevapoblacion[i]
		self.conservar_mejor(random.randrange(self.tam_poblacion))

    # Reemplazo de los individuos peor adaptados.
	def reemplazo_peor_adaptados(self):
		
		media = sum(self.adaptacion)/float(self.tam_poblacion)
		
		self.evaluacion_nueva_poblacion()
		mejor_fits = self.adaptacionnuevapoblacion[:]
		# Se evita valores repetidos.
		mejor_fits = list(set(mejor_fits))		

		for i in range(self.tam_poblacion):
			if self.adaptacion[i] < (media - (media * 0.1)):
				# Se obtiene el indice del mejor individuo.
				mejor_index = self.adaptacionnuevapoblacion.index(max(mejor_fits))
				mejor_fits.remove(max(mejor_fits))
				self.poblacion[i] = self.nuevapoblacion[mejor_index]
				if len(mejor_fits) == 0:
					mejor_fits = self.adaptacionnuevapoblacion[:]
					# Se evita valores repetidos.
					mejor_fits = list(set(mejor_fits))
		self.conservar_mejor(random.randrange(self.tam_poblacion))

    # Reemplazo de individuos de adaptación similar.
	def reemplazo_adaptacion_similar(self):
		# Se ordena la poblacion y la nueva generacion 

		poblacion_fits = self.adaptacion[:]
		poblacion_index = []

		self.evaluacion_nueva_poblacion()
		nuevapoblacion_fits = self.adaptacionnuevapoblacion[:]
		nuevapoblacion_index = []
		
		# Se ordena los valores de mayor a menor.
		for _ in range(self.tam_poblacion):
			# Se ordena la poblacion.
			poblacion_index.append(self.adaptacion.index(max(poblacion_fits)))
			poblacion_fits.remove(max(poblacion_fits))

			# Se ordena la nueva poblacion.
			nuevapoblacion_index.append(self.adaptacionnuevapoblacion.index(max(nuevapoblacion_fits)))
			nuevapoblacion_fits.remove(max(nuevapoblacion_fits))

		vecindad = random.randrange(3, 6)
		ei = [i for i in range(vecindad)]
		for i in range(0, self.tam_poblacion - vecindad, vecindad):
			self.poblacion[poblacion_index[i + random.choice(ei)]] = self.nuevapoblacion[nuevapoblacion_index[i]]
		self.conservar_mejor(random.randrange(self.tam_poblacion))

	###### Metodos de Paso de generacion. Fin ######

###### Genetico. Fin ######