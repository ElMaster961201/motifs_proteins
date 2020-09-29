import random as rm
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

	nombre_archivo = "Mul.fasta"

	"""Inicializacion"""
	def __init__(self, archivo = nombre_archivo):

		self.lista_hongos = []
		self.nombres = []
		self.hongo = ""
		self.file = open(archivo, "r").readlines()
		self.file = self.file[1:]

		for l in self.file:
			if l[0] == '>':
				self.lista_hongos.append(self.hongo)
				self.hongo = ""
				self.nombres.append(l[:len(l) - 1])
				continue
			self.hongo = self.hongo + l[:len(l) - 1]
		self.hongo = ""
		
	def matriz_hongos(self, archivo = nombre_archivo):

		self.lista_hongos = []
		self.hongo = ""
		self.file = open(archivo, "r").readlines()
		self.file = self.file[1:]

		for l in self.file:
			if l[0] == '>':
				self.lista_hongos.append(self.hongo)
				self.hongo = ""
				continue
			self.hongo = self.hongo + l[:len(l) - 1]
		self.hongo = ""
		return self.lista_hongos
	
	def lista_nombres(self, archivo = nombre_archivo):
		self.nombres = []
		self.file = open(archivo, "r").readlines()
		self.file = self.file[1:]

		for l in self.file:
			if l[0] == '>':
				self.nombres.append(l[:len(l) - 1])
		return self.nombres

if __name__ == "__main__":
	archivo = "Mul.fasta"
	lista_hongos = []
	nombres = []
	hongo = ""
	file = open(archivo, "r").readlines()
	file = file[1:]
	for l in file:
		if l[0] == '>':
			lista_hongos.append(hongo)
			hongo = ""
			nombres.append(l[:len(l) - 1])
			continue
		hongo = hongo + l[:len(l) - 1]
	hongo = ""
	for i in range(len(lista_hongos)):
		print(nombres[i])
		print (lista_hongos[i][1212:1219])
