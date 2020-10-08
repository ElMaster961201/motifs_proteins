import os 
from Motifs import Motifs as MTFS

scim,ccim,hcim = MTFS().sciccihci()
index = { 'A':0,'C':1,'D':2,'E':3,'F':4,'G':5,'H':6,'I':7,'K':8,'L':9,'M':10,'N':11,'P':12,'Q':13,'R':14,'S':15,'T':16,'V':17,'W':18,'Y':19}

secuencia_conservada = ['G','T','G','L','G','L','A','I','V','K']
secuencias_sinteticas = [

]

ruta = "Resultados/Compu/" + str(len(secuencia_conservada)) # Ingresa el nombre de la carpeta donde se guardara el archico generado.

if not os.path.exists(ruta):
    os.makedirs(ruta)

file = open(ruta + "/ValidacionResultados.txt","w")
file.write("Validacion de resultados de " + str(ruta) + os.linesep)



for sintetica in secuencias_sinteticas:
    sum_scim = 0.0
    sum_ccim = 0.0
    sum_hcim = 0.0
    for i in range(len(secuencia_conservada)):
        sum_scim = sum_scim + scim[index[sintetica[i]]][index[secuencia_conservada[i]]]
        sum_ccim = sum_ccim + ccim[index[sintetica[i]]][index[secuencia_conservada[i]]]
        sum_hcim = sum_hcim + hcim[index[sintetica[i]]][index[secuencia_conservada[i]]]
    file.write(str(sintetica) + ";" + str(((sum_scim * 0.2) + (sum_ccim * 0.4) + (sum_hcim * 0.4))) + ";")
    file.write(str(sum_scim * 0.2 ) + ";" )
    file.write(str(sum_ccim * 0.4 ) + ";" )
    file.write(str(sum_hcim * 0.4 ) + ";" + os.linesep)
    # print((sum_scim * 0.2) + (sum_ccim * 0.4) + (sum_hcim * 0.4))




