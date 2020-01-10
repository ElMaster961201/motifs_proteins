#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Jesus Alberto Correa Morales.
 	17/09/2019 - ??/??/????
"""

"""
	En el siguiente archivo .py es un Script con el cual se buscan motivos
	conservados en la sucesion de proteinas de los hongos.
	Para la busqueda de motivos conservados se implementara la metaheuristica 
	de algoritmo genetico.
"""

# <------------- Importaciones Inicio ------------- > 
from Genetico import Genetico
from Hongos import Hongos
from Motifs import Motifs
# <------------- Importaciones Fin    ------------- > 


# <------------- Variables -------- Inicio ----- >

# Numero de generaciones (nG) -> Numero de generaciones que tendra nuestro algoritmo.
nG = 100
# Tamaño de poblacion (tP) -> Indica cuantos individuos conformaran la generacion.
tP = 30
# Probabilidad de mutacion (pM) -> Probabilidad de que un individuo mute. 
pM = 0.01
# Cantidad de mutacion (cM) -> Cantidad de genes que muta el individuo. 
cM = 2
# Motivo altamente conservado (mA) -> Motivo conservado que se buscara en los hongos.
mA = ['A','H','M','K','L','F','S','C','Q','P','E','E','G','I','A','Y','L','F','M','Q']

# <------------- Variables -------- Fin    ----- >


# <------------- Instancias--- Inicio ------------- > 

# Instancia de algoritmo Genetico AGS.
AGS = Genetico()
# Instancia de la clase Hongos Hns.
Hns = Hongos()
# Instancia de la clase Motifs Mtfs.
# Mtfs = Motifs()

# <------------- Instancias--- Fin    ------------- > 


# <------------- Codigó    --- Inicio ------------- > 





# <------------- Codigó    --- Fin    ------------- > 


# <------------- Pruebas   --- Inicio ------------- >
# print (AGS.poblacion)
# print(Hns.hongos)
# print(len(Hns.hongo))
# Mtfs.imprimeMatrix(Mtfs.CCIM)
# print (len(Mtfs.CCIM[0]))
# print (len(AGS.poblacion[0]))
# print ((Hns.hongos[0]))

# print(len(motif))
print()
print (AGS.SCIM)
print ()
print (AGS.CCIM)
print ()
print (AGS.SCIM)

# <------------- Pruebas   --- Fin    ------------- >

# amo = { 0:'A', 1:'C', 2:'D', 3:'E', 4:'F', 5:'G', 6:'H', 7:'I', 8:'K', 9:'L', 10:'M', 11:'N', 12:'P', 13:'Q', 14:'R', 15:'S', 16:'T', 17:'V', 18:'W', 19:'Y' }

