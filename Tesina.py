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

from Genetico import Genetico
from Hongos import Hongos
from Motifs import Motifs

# <------------- Variables ------------- >
# Numero de generaciones (nG) -> Numero de generaciones que tendra nuestro algoritmo.
nG = 100
# Tamaño de poblacion (tP) -> Indica cuantos individuos conformaran la generacion.
tP = 30
# Probabilidad de mutacion (pM) -> Probabilidad de que un individuo mute. 
pM = 0.01
# Cantidad de mutacion (cM) -> Cantidad de genes que muta el individuo. 
cM = 2

motif = ['','','','','','','','','','','','','','','','','','','','']


AGS = Genetico()
# print (AGS.poblacion)

Hns = Hongos()
# print(Hns.hongos)
# print(len(Hns.hongo))

Mtfs = Motifs()
# Mtfs.imprimeMatrix(Mtfs.CCIM)
print (len(Mtfs.CCIM[0]))
print (len(AGS.poblacion[0]))
print ((Hns.hongos[0]))

# print(len(motif))


amo={ 2:'B',1:'A'}

print(amo[2])