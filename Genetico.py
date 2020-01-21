# <------------- Librerias ------------- >
# Generar numeros o selecciones de manera random.
import random
from Motifs import Motifs as MTFS
from Hongos import Hongos as HNS

class Genetico(object):

	"""
		Inicializamos la clase con el 
		tamaño de poblacion de manera aleatoria
		necesitamos:
		* Tamaño de la poblacion,
		* Tamaño de la proteina, 
		* Tamaño del motivo consercado
	"""
	

	""" Es utilizado para ubicar la posicion del aminoacido en las matrices de evaluacion. """	
	index = { 'A':0, 'C':1, 'D':2, 'E':3, 'F':4, 'G':5, 'H':6, 'I':7, 'K':8, 'L':9, 'M':10, 'N':11, 'P':12, 'Q':13, 'R':14, 'S':15, 'T':16, 'V':17, 'W':18, 'Y':19 }
	
	SCIM, CCIM, HCIM = MTFS().SCICCIHCI()
	Hongos = HNS().matrizHongos()
		
	"""Funcion que inicializa la poblacion"""
	def __init__(self, tamPoblacion = 100, tamProteina = 2654,
		tamMotivo = 20,numHongos = 1245,proMutacion = 0.01,
		canMutacion = 2):
		self.tamPoblacion = tamPoblacion
		self.tamProteina = tamProteina
		self.tamMotivo = tamMotivo
		self.numHongos = numHongos
		self.proMutacion = proMutacion
		self.canMutacion = canMutacion
		self.ind = []
		self.poblacion = []
		self.fit = [0.0 for i in range(tamPoblacion)]

		for x in range(self.tamPoblacion):
			self.ind = []
			for r in range(self.numHongos):
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

	###### Algoritmos de seleccion. ######

	#### Ruleta.
	def ruleta(self):
		aux0 = 0.0		
		aux1 = 0.0
		aux2 = 0.0
		for fi in self.fit:
			aux0 = abs(fi[0]) + aux0 	
			aux1 = abs(fi[1]) + aux1 
			aux2 = abs(fi[2]) + aux2 
			pass
		
		# print(aux0)
		# print(aux1)		
		# print(aux2)
		media0 = aux0/float(self.numHongos)
		media1 = aux1/float(self.numHongos)
		media2 = aux2/float(self.numHongos)
		# print(media0)
		# print(media1)		
		# print(media2)
		
		pass
	### Muestreo Estocastico Universal.

	### Torneo.

	### Muestreo por Restos. 

		
