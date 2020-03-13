import os 
# Se importa nuestra clase
from Genetico_Motifs import Genetico

# Se genera una instancia del algoritmo genetico con los siguientes parametros
p = [
    100, # tamPoblacion -> 0
    27, # k -> 1
    0.1, # proMutacion -> 2 
    2, # canMutacion -> 3
    1, # numElitismo -> 4
    4, # tamTorneo -> 5
	50, # umbral -> 6 
    0.6, # proCruce -> 7
    [1/3, 1/3, 1/3], # w -> 8
    ['F', 'W', 'L', 'V', 'N', 'L','S','A','H','M','K','L','F','S','C','Q','P','E','E','G','I','A','Y','L','F','M','Q'] # secuencia  -> 9
]

file = open("Matriz.txt","w")
file.write("Diseño de experimento v0.1"+ os.linesep)
file.write("Con los siguientes parametros:"+ os.linesep)
file.write(os.linesep)
file.write("Tamano de la poblacion: " + str(p[0]) + os.linesep)
file.write("Tamano de la secuencia: " + str(p[1]) + os.linesep)
file.write("Probabilidad de Mutacion: ",p[2],os.linesep)
file.write("Cantidad de Aminiacidos a mutar: ", p[3],os.linesep)
file.write("Numero de individuos seleccionado por Elitismo: ", p[4],os.linesep)
file.write("Tamano de torneo: ", p[5], os.linesep)
file.write("Umbral: ", p[6], os.linesep)
file.write("Probabilidad de Cruce: ", p[7], os.linesep)
file.write("Pesos de las Matrices: ", p[8], os.linesep)
file.write(os.linesep)
file.write("Secuencia base: ", p[9], os.linesep)
file.write(os.linesep)
file.write("El Experimento se realizo 30 veces.", os.linesep)
file.write("Con los metodos de Ruleta, cruzamiento por punto fijo",os.linesep)
file.write("Mutacion Estandar, Elitismo del mejor individuo y Remplazo de padres.",os.linesep)

totalfits = 0.0
for _ in range(30):
    file.write("Los resultados obtenidos en el experimento N° ", _, os.linesep)
    AGS = Genetico(p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8])
    for i in range(100):
        AGS.fits(p[9])
        AGS.ruleta()
        # AGS.estocasticoUniversal()
        # AGS.torneo()
        # AGS.restos()
        AGS.puntoFijo()
        # AGS.multiPunto()
        AGS.mutacionEstandar()
        AGS.elitismo()
        AGS.remplazoPadres()
        # AGS.remplazoAleatorio()
        pass
    file.write(os.linesep)
    mejor = AGS.elitismoSimple(1)
    file.write("Individuo ", mejor[0], os.linesep)
    file.write("Fits", mejor[1], os.linesep)
    file.write("fits promedio del experimento ",float(sum(AGS.fit))/AGS.tamPoblacion, os.linesep)
    file.write(os.linesep)
    file.write(os.linesep)
    totalfits = mejor[1] + totalfits
    pass
file.write("El Fit promedio del experimento es: ", float(totalfits)/30, os.linesep)
num = []

file.close()
# print(max(AGS.fit))
# print(min(AGS.fit))

