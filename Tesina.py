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
# from Genetico_Pos import Genetico_P
from Genetico_Motifs import GeneticoMotifs
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
AGS = GeneticoMotifs()
# Instancia de la clase Hongos Hns.
# Hns = Hongos()
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
# print("SCIM")
# print (AGS.SCIM)
# print ("CCIM")
# print (AGS.CCIM)
# print ("HCIM")
# print (AGS.HCIM)
# print ()


# print()
# print (max(AGS.CCIM))
# print()
# print(min(AGS.CCIM))


# print()
# print (max(AGS.HCIM))
# print()
# print(min(AGS.HCIM))


# print (AGS.Hongos)
# print ()
# print (AGS.poblacion)

AGS.evaluacionPoblacion(mA)
# print(AGS.fit)
# AGS.ruleta()
# print((AGS.nuevapoblacion))
# print()
# print(len(AGS.nuevapoblacion))

# AGS.estocasticoUniversal()
# print((AGS.nuevapoblacion))
# print()
# print(len(AGS.nuevapoblacion))

# AGS.torneo()
# print((AGS.nuevapoblacion))
# print()
# print(len(AGS.nuevapoblacion))

# AGS.restos()
# print((AGS.nuevapoblacion))
# print()
# print(len(AGS.nuevapoblacion))

# AGS.puntoFijo()

# <------------- Pruebas   --- Fin    ------------- >

# amo = { 0:'A', 1:'C', 2:'D', 3:'E', 4:'F', 5:'G', 6:'H', 7:'I', 8:'K', 9:'L', 10:'M', 11:'N', 12:'P', 13:'Q', 14:'R', 15:'S', 16:'T', 17:'V', 18:'W', 19:'Y' }

