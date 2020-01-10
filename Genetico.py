# <------------- Librerias ------------- >
# Generar numeros o selecciones de manera random.
import random
from Motifs import Motifs as MTFS

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

		for x in range(self.tamPoblacion):
			self.ind = []
			for r in range(self.numHongos):
				self.ind.append(random.randrange(1+ self.tamProteina-self.tamMotivo))
				pass
			self.poblacion.append(self.ind)
			pass
			self.ind = []


	# def fits(self, matrix, hongo, motif):
	# 	aminoacido [{'A':1}]
	# 	con = 0.0
	# 	for x in range (len(motif)):
	# 		con = con + matrix[individuo][x]

	# 		pass
