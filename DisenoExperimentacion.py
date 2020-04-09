import os 
from time import time

# Se importa nuestra clase
from Genetico_Motifs import Genetico

# Se genera una instancia del algoritmo genetico con los siguientes parametros
p = [
    100, # tamPoblacion -> 0
    27, # k -> 1
    0.5, # proMutacion -> 2 
    8, # canMutacion -> 3
    10, # numElitismo -> 4
    15, # tamTorneo -> 5
    500, # numRestos -> 6
    1.0, # proCruce -> 7
    [0,0,1],#1/3, 1/3, 1/3], # w -> 8
    ['F', 'W', 'L', 'V', 'N', 'L','S','A','H','M','K','L','F','S','C','Q','P','E','E','G','I','A','Y','L','F','M','Q'] # secuencia  -> 9
]

nExperimientos = 10 
nGeneraciones = 500

cont = 0

while cont < 22:
    t = True
    while t:
        if (os.path.exists("DisennoExperimentacion" + str(cont) + ".txt")):
            cont = cont + 1 
        else:
            print("Ciclo: ",cont)
            startTimeTotal = time ()

            file = open("DisennoExperimentacion" + str(cont) + ".txt","w")
            file.write("Diseño de experimento v0.1."+ str(cont) + os.linesep)
            file.write("Con los siguientes parametros:"+ os.linesep)
            file.write(os.linesep)
            file.write("Tamano de la poblacion: " + str(p[0]) + os.linesep)
            file.write("Tamano de la secuencia: " + str(p[1]) + os.linesep)
            file.write("Probabilidad de Mutacion: " + str(p[2]) + os.linesep)
            file.write("Cantidad de Aminiacidos a mutar: " + str(p[3]) + os.linesep)
            file.write("Numero de individuos seleccionado por Elitismo: " + str(p[4]) + os.linesep)
            file.write("Tamano de torneo: " + str(p[5]) + os.linesep)
            file.write("Numero de restos: " + str(p[6]) + os.linesep)
            file.write("Probabilidad de Cruce: " + str(p[7]) + os.linesep)
            file.write("Pesos de las Matrices: " + str(p[8]) + os.linesep)
            file.write(os.linesep)
            file.write("Secuencia base: " + str(p[9]) + os.linesep)
            file.write(os.linesep)
            file.write("El Experimento se realizo " + str(nExperimientos) + " veces." + os.linesep)
            file.write("Con " +str(nGeneraciones)+" Generaciones" + os.linesep)
            # file.write("Con los metodos de ruleta, cruzamiento por punto fijo" + os.linesep)
            file.write("Con los metodos de torneo, cruzamiento por punto fijo" + os.linesep)
            file.write("Mutacion Estandar, Elitismo del mejor individuo y Remplazo de padres." + os.linesep)

            totalfits = 0.0
            for _ in range(nExperimientos):
                startTimeExperimento = time ()
                file.write(os.linesep)
                file.write("Los resultados obtenidos en el experimento N° " + str(_ + 1 ) + os.linesep)
                AGS = Genetico(p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8])
                for i in range(nGeneraciones):
                    AGS.fits(p[9])
                    # AGS.ruleta()
                    # AGS.estocasticoUniversal()
                    AGS.torneo()
                    # AGS.restos()
                    AGS.puntoFijo()
                    # AGS.multiPunto()
                    AGS.mutacionEstandar()
                    AGS.elitismo()
                    AGS.remplazoPadres()
                    # AGS.remplazoAleatorio()
                    pass
                file.write(os.linesep)
                mejor = AGS.mejor
                file.write("Individuo " + str(mejor[0]) + os.linesep)
                file.write("Fits " + str(mejor[1]) + os.linesep)
                file.write("fits promedio del experimento " + str(float(sum(AGS.fit))/AGS.tamPoblacion) + os.linesep)
                file.write(os.linesep)
                file.write(os.linesep)
                file.write("El mejor individuo se mantuvo " + str(mejor[2]) + " Generaciones" + os.linesep)
                finishTimeexperimento = time() - startTimeExperimento
                file.write("El experimento N° " + str(_ + 1) + " hizo un tiempo de %.10f Segundos" %finishTimeexperimento + os.linesep)
                totalfits = mejor[1] + totalfits
                pass
            file.write("El Fit promedio del experimento es: " + str(float(totalfits)/nExperimientos) + os.linesep)
            finishTimeTotal = time() - startTimeTotal
            t = False
            pass
        pass
    file.write(os.linesep)
    file.write(os.linesep)
    file.write("El Experimiento hizo un tiempo total de %.10f Segundos" %finishTimeTotal + os.linesep)
    file.close()
    pass 