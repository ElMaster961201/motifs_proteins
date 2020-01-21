# <------------- Librerias ------------- >
# Generar numeros o selecciones de manera random.
import random as rm
# Permite la lectura y escritura de archivos.
import os


class Hongos(object):

	"""
	# Matriz donde se almacenaran todas las succesiones 
	de proteinas de los hongos.
	
	hongos

	# String auxiliar que permite la unin de la 
	succesion de proteinas de los hongos del documnto 

	hongo

	# Variable que utilizamos para leer el archivo.

	file 
	"""

	"""Inicializacion"""
	def __init__(self,archivo = "./Mul.fasta"):

		self.hongos = []
		self.hongo = ""
		self.file = open(archivo, "r").readlines()
		self.file = self.file[1:]

		for l in self.file:
			if l[0] == '>':
				self.hongos.append(self.hongo)
				self.hongo = ""
				continue
			self.hongo = self.hongo + l[:len(l)-1]
			pass
		self.hongo = ""
		
	def matrizHongos(self,archivo = "./Mul.fasta"):

		self.hongos = []
		self.hongo = ""
		self.file = open(archivo, "r").readlines()
		self.file = self.file[1:]

		for l in self.file:
			if l[0] == '>':
				self.hongos.append(self.hongo)
				self.hongo = ""
				continue
			self.hongo = self.hongo + l[:len(l)-1]
			pass
		self.hongo = ""
		return self.hongos