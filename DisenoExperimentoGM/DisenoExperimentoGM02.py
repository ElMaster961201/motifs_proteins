import os 
from time import time
import sys
sys.path.append(".")

# Se importa nuestra clase
from Genetico_Motifs import GeneticoMotifs
from Parametros_GM import ParametrosGM 

# Se obtrienen los parametros a utilizar de una clase. 
p,nGeneraciones,nRepeticiones = ParametrosGM().parametros()

cont = 1
t = True
ruta = "DisenoExperimentoGM/Resultados/Compu/" + str(p[1]) # Ingresa el nombre de la carpeta donde se guardara el archico generado.

if not os.path.exists(ruta):
    os.makedirs(ruta)

while t:
    if (os.path.exists(ruta + "/Experimento" + str(cont) + ".txt")):
        cont = cont + 1 
    else:
        startTimeTotal = time ()

        file = open(ruta + "/Experimento" + str(cont) + ".txt","w")
        file.write("Experimento v0.2."+ str(cont) + os.linesep)
        file.write("Con los siguientes parametros:"+ os.linesep)
        file.write(os.linesep)
        file.write("Tamano de la poblacion: " + str(p[0]) + os.linesep)
        file.write("Tamano de la secuencia: " + str(p[1]) + os.linesep)
        file.write("Probabilidad de Mutacion: " + str(p[2]) + os.linesep)
        file.write("Cantidad de elementos a mutar: " + str(p[3]) + os.linesep)
        file.write("Numero de individuos seleccionado por Elitismo: " + str(p[4]) + os.linesep)
        file.write("Eunumero: " + str(p[5]) + os.linesep)
        file.write("Tamano de torneo: " + str(p[6]) + os.linesep)
        file.write("Numero de restos: " + str(p[7]) + os.linesep)
        file.write("Probabilidad de Cruce: " + str(p[8]) + os.linesep)
        file.write("Pesos de las Matrices: " + str(p[9]) + os.linesep)
        file.write("Secuencia base: " + str(p[10]) + os.linesep)
        file.write("Numero de repeticiones del experimento: " + str(nRepeticiones) + os.linesep)
        file.write("Numero de generaciones: " +str(nGeneraciones) + os.linesep)

        file.write(os.linesep)
        file.write("Con los siguientes metodos: " + os.linesep)

        file2 = open(ruta + "/ExperimentoConcentrado" + str(cont) + ".txt","w")
        file2.write("Experimento v0.2."+ str(cont) + os.linesep)
        file2.write("Con los siguientes parametros:"+ os.linesep)
        file2.write(os.linesep)
        file2.write("Tamano de la poblacion:;" + str(p[0]) + os.linesep)
        file2.write("Tamano de la secuencia:;" + str(p[1]) + os.linesep)
        file2.write("Probabilidad de Mutacion:;" + str(p[2]) + os.linesep)
        file2.write("Cantidad de individuos a mutar:;" + str(p[3]) + os.linesep)
        file2.write("Numero de individuos seleccionado por Elitismo:;" + str(p[4]) + os.linesep)
        file2.write("Eunumero:;" + str(p[5]) + os.linesep)
        file2.write("Tamano de torneo:;" + str(p[6]) + os.linesep)
        file2.write("Numero de restos:;" + str(p[7]) + os.linesep)
        file2.write("Probabilidad de Cruce:;" + str(p[8]) + os.linesep)
        file2.write("Pesos de las Matrices:;" + str(p[9]) + os.linesep)
        file2.write("Secuencia base:;" + str(p[10]) + os.linesep)
        file2.write("Numero de generaciones:;" +str(nGeneraciones) + os.linesep)
        
        file2.write(os.linesep)
        file2.write("Metodos" + os.linesep)
        
        # Cambiar segun la prueba
        file.write("Metodo de seleccion: ")
        file2.write("Seleccion:;"
        ##### Metodos de Seleccion. ######
        file.write("Ruleta" + os.linesep)
        file2.write("Ruleta" + os.linesep)

        file.write("Metodo de cruzamiento: ")
        file2.write("Cruzamiento:;")
        ###### Metodos de Cruzamiento. ######
        file.write("Monopunto" + os.linesep)
        file2.write("Monopunto" + os.linesep)
        
        file.write("Metodo de mutacion: ")
        file2.write("Mutacion:;")
        ###### Metodos de Mutacion. ######
        file.write("Mutacion Estandar" + os.linesep)
        file2.write("Mutacion Estandar" + os.linesep)

        file.write("Metodo de consevacion: ")
        file2.write("Consevacion:;")

        ###### Metodo de conservacion. ######
        file.write("Elitismo" + os.linesep)
        file2.write("Elitismo" + os.linesep)

        file.write("Metodo de paso de generacion: ")
        file2.write("Paso de generacion:;")
        ###### Metodo de Paso de Generacion. ######
        file.write("Reemplazo de Padres" + os.linesep)
        file2.write("Reemplazo de Padres" + os.linesep)

        totalfits = 0.0
        totalGen = 0
        for _ in range(nRepeticiones):
            print ("Repeticion ",_ + 1)
            startTimeExperimento = time ()
            file.write(os.linesep)
            file.write("Los resultados obtenidos en la repeticion " + str(_ + 1 ) + os.linesep)
            file2.write(os.linesep)
            file2.write(str(_ + 1 ))
            AGS = GeneticoMotifs(p)
            AGS.evaluacion_poblacion()
            for i in range(nGeneraciones):
                # print (_ + 1, i + 1)
                ##### Metodos de Seleccion. ######
                AGS.ruleta()

                ###### Metodos de Cruzamiento. ######
                AGS.cruzamiento_monopunto()

                ###### Metodos de Mutacion. ######
                AGS.mutacion_estandar_biologica()

                ###### Metodo de conservacion. ######
                AGS.elitismo()

                ###### Metodo de Paso de Generacion. ######
                AGS.reemplazo_padres()
                
                AGS.evaluacion_poblacion()

            finishTimeexperimento = time() - startTimeExperimento

            file.write("Fits promedio de la ultima generacion es: " + str(float(sum(AGS.adaptacion))/AGS.tam_poblacion) + os.linesep)
            file.write("El Mejor individuo: " + os.linesep)
            mejor = AGS.mejor
            file.write("Individuo " + str(mejor[0]) + os.linesep)
            file.write("Fits " + str(mejor[1]) + os.linesep)
            file.write("El mejor individuo se mantuvo " + str(mejor[2]) + " Generaciones" + os.linesep)
            totalGen = totalGen + mejor[2]
            file.write("La repeticion " + str(_ + 1) + " hizo un tiempo de %.10f Segundos" %finishTimeexperimento + os.linesep)
            totalfits = mejor[1] + totalfits

            file2.write(";" + str(float(sum(AGS.adaptacion))/AGS.tam_poblacion))
            file2.write(";" + str(mejor[0]))
            file2.write(";" + str(mejor[1]))
            file2.write(";" + str(mejor[2]))
            file2.write(";%.10f" %finishTimeexperimento)

        file.write(os.linesep)
        file.write(os.linesep)
        file.write("El Fit promedio del mejor individuo obtenido es: " + str(float(totalfits)/nRepeticiones) + os.linesep)
        file.write("El promedio de generaciones que se mantiene el mejor individuo es: " + str(float(totalGen)/nRepeticiones) + os.linesep)
        
        file2.write(os.linesep)
        file2.write(os.linesep)
        file2.write("El Fit promedio del mejor individuo obtenido es: " + str(float(totalfits)/nRepeticiones) + os.linesep)
        file2.write("El promedio de generaciones que se mantiene el mejor individuo es: " + str(float(totalGen)/nRepeticiones) + os.linesep)
        
        finishTimeTotal = time() - startTimeTotal
        t = False

file.write("El experimento N° " + str(cont) + " hizo un tiempo total de %.10f Segundos" %finishTimeTotal + os.linesep)
file.close()

file2.write("El experimento N° " + str(cont) + " hizo un tiempo total de %.10f Segundos" %finishTimeTotal + os.linesep)
file2.close()