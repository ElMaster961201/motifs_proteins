# Jesus Alberto Correa Morales.
# 17/09/2019 - ??/??/????

# En el siguiente archivo .py es un Script con el cual se buscan motivos
# conservados en la sucesion de proteinas de los hongos.
# Para la busqueda de motivos conservados se implementara la metaheuristica 
# de algoritmo genetico.

# <------------- Librerias ------------- >
# Generar numeros o selecciones de manera random.
import random as rm
# Permite la lectura y escritura de archivos.
import os

# <------------- Variables ------------- >
# poblacion -> Vector donde se almacenara la poblacion de individuos que utilizara el algoritmo 
poblacion = []
# individuo -> Vector donde se almacenara una solucion potencial.
individuo = [] 
# Numero de generaciones (nG) -> Numero de generaciones que tendra nuestro algoritmo.
nG = 100
# Tamaño de poblacion (tP) -> Indica cuantos individuos conformaran la generacion.
tP = 30
# Probabilidad de mutacion (pM) -> Probabilidad de que un individuo mute. 
pM = 0.01
# Cantidad de mutacion (cM) -> Cantidad de genes que muta el individuo. 
cM = 2


hongos = []
hongo = []
bases = ['A','T','C','G','A','T','C','G',' ']

# # Codigo para generar una poblacion de hongos de manera aleatoria.
# for x in range(50):
# 	for y in range(30):
# 		hongo.append(rm.choice(bases))
# 	hongos.append(hongo)
# 	hongo = []
# file = open("./hongos.txt", "w")
# for h in hongos:
# 	file.write(str(h) + os.linesep)
# 	pass
# file.close()

file = open("./hongos.txt", "r")

print(file.read())
