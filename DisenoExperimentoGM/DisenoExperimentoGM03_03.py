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
ruta = "DisenoExperimentoGM/Resultados/Compu/Biologfico" + str(p[1]) # Ingresa el nombre de la carpeta donde se guardara el archico generado.

if not os.path.exists(ruta):
    os.makedirs(ruta)

while t:
    if (os.path.exists(ruta + "/Experimento" + str(cont) + ".txt")):
        cont = cont + 1 
    else:
        startTimeTotal = time ()

        file = open(ruta + "/Experimento" + str(cont) + ".txt","w")
        file.write("Experimento v1.3."+ str(cont) + os.linesep)
        file.write("Con los siguientes parametros:"+ os.linesep)
        file.write(os.linesep)
                file.write("Tamano de la poblacion:;" + str(p[0]) + os.linesep)
        file.write("Tamano de la secuencia:;" + str(p[1]) + os.linesep)
        file.write("Probabilidad de Mutacion:;" + str(p[2]) + os.linesep)
        file.write("Cantidad de individuos a mutar:;" + str(p[3]) + os.linesep)
        file.write("Numero de individuos seleccionado por Elitismo:;" + str(p[4]) + os.linesep)
        file.write("Eunumero:;" + str(p[5]) + os.linesep)
        file.write("Tamano de torneo:;" + str(p[6]) + os.linesep)
        file.write("Numero de restos:;" + str(p[7]) + os.linesep)
        file.write("Probabilidad de Cruce:;" + str(p[8]) + os.linesep)
        file.write("Pesos de las Matrices:;" + str(p[9]) + os.linesep)
        file.write("Secuencia base:;" + str(p[10]) + os.linesep)
        file.write("Numero de generaciones:;" +str(nGeneraciones) + os.linesep)

        file.write(os.linesep)
        file.write("Metodos" + os.linesep)
        
        # Cambiar segun la prueba
        # file.write("Seleccion:;")
        ##### Metodos de Seleccion. ######
        # file.write("Restos" + os.linesep)

        file.write("Cruzamiento:;")
        ###### Metodos de Cruzamiento. ######
        file.write("Monopunto" + os.linesep)

        file.write("Mutacion:;")
        ###### Metodos de Mutacion. ######
        file.write("Mutacion Estandar Biologica" + os.linesep)

        file.write("Consevacion:;")
        ###### Metodo de conservacion. ######
        file.write("Elitismo" + os.linesep)

        file.write("Paso de generacion:;")
        ###### Metodo de Paso de Generacion. ######
        file.write("Reemplazo de Padres" + os.linesep)

        totalfits = 0.0
        totalGen = 0
        for _ in range(nRepeticiones):
            print ("Repeticion ",_ + 1)
            startTimeExperimento = time ()
            file.write(os.linesep)
            file.write(str(_ + 1 ))
            AGS = GeneticoMotifs(p)
            AGS.evaluacion_poblacion()
            for i in range(nGeneraciones):
                # print (_ + 1, i + 1)
                ##### Metodos de Seleccion. ######
                AGS.restos()

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

            file.write(";" + str(float(sum(AGS.adaptacion))/AGS.tam_poblacion))
            mejor = AGS.mejor
            file.write(";" + str(mejor[0]))
            file.write(";" + str(mejor[1]))
            file.write(";" + str(mejor[2]))
            totalGen = totalGen + mejor[2]
            file.write(";%.10f" %finishTimeexperimento + os.linesep)
            totalfits = mejor[1] + totalfits

        file.write(os.linesep)
        file.write(os.linesep)
        file.write("El Fit promedio del mejor individuo obtenido es: " + str(float(totalfits)/nRepeticiones) + os.linesep)
        file.write("El promedio de generaciones que se mantiene el mejor individuo es: " + str(float(totalGen)/nRepeticiones) + os.linesep)
        finishTimeTotal = time() - startTimeTotal
        t = False

file.write("El experimento N° " + str(cont) + " hizo un tiempo total de %.10f Segundos" %finishTimeTotal + os.linesep)
file.close()
