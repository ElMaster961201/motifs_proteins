# <------------- Librerias ------------- >
# Generar numeros o selecciones de manera random.
import random


class Genetico(object):

	"""
		Inicializamos la clase con el 
		tamaño de poblacion de manera aleatoria
		necesitamos:
		* Tamaño de la poblacion,
		* Tamaño de la proteina, 
		* Tamaño del motivo consercado
	"""
	
	"""Funcion que inicializa la poblacion"""
	def __init__(self, tamPoblacion = 100, tamProteina = 2654,
		tamMotivo = 20,numHongos = 1245):
		self.tamPoblacion = tamPoblacion
		self.tamProteina = tamProteina
		self.tamMotivo = tamMotivo
		self.numHongos = numHongos
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


	def fits(self, matrix, hongo, motif):
		aminoacido [{'A':1}]
		con = 0.0
		for x in range (len(motif)):
			con = con + matrix[individuo][x]

			pass