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
        file.write("Experimento v0.1."+ str(cont) + os.linesep)
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
        
        # Cambiar segun la prueba
        file.write("Metodo de seleccion: ")
        ##### Metodos de Seleccion. ######
        # file.write("Torneo" + os.linesep)
        # file.write("Ruleta" + os.linesep)
        # file.write("Restos" + os.linesep)
        # file.write("Estocastico Universal" + os.linesep)

        file.write("Metodo de cruzamiento: ")
        ###### Metodos de Cruzamiento. ######
        # file.write("Monopunto" + os.linesep)
        # file.write("Multipunto" + os.linesep)
        # file.write("Cruzamiento Uniforme" + os.linesep)
        
        file.write("Metodo de mutacion: ")
        ###### Metodos de Mutacion. ######
        # file.write("Mutacion Uniforme" + os.linesep)
        # file.write("Mutacion Estandar" + os.linesep)

        file.write("Metodo de consevacion: ")
        ###### Metodo de conservacion. ######
        # file.write("Elitismo" + os.linesep)

        file.write("Metodo de paso de generacion: ")
        ###### Metodo de Paso de Generacion. ######
        # file.write("Reemplazo de Padres" + os.linesep)
        # file.write("Reemplazo Aleatorio" + os.linesep)
        # file.write("Reemplazo de los Peor Adaptados" + os.linesep)
        # file.write("Reemplazo de Adaptacion Similar" + os.linesep)

        totalfits = 0.0
        totalGen = 0
        for _ in range(nRepeticiones):
            print ("Repeticion ",_ + 1)
            startTimeExperimento = time ()
            file.write(os.linesep)
            file.write("Los resultados obtenidos en la repeticion " + str(_ + 1 ) + os.linesep)
            AGS = GeneticoMotifs(p)
            AGS.evaluacion_poblacion()
            for i in range(nGeneraciones):
                print(_ + 1, i)
                ##### Metodos de Seleccion. ######
                # AGS.torneo()
                # AGS.ruleta()
                # AGS.restos()
                # AGS.estocastico_universal()

                ###### Metodos de Cruzamiento. ######
                # AGS.cruzamiento_monopunto()
                # AGS.cruzamiento_multipunto()
                # AGS.cruzamiento_uniforme()

                ###### Metodos de Mutacion. ######
                # AGS.mutacion_uniforme()
                # AGS.mutacion_estandar()

                ###### Metodo de conservacion. ######
                # AGS.elitismo()

                ###### Metodo de Paso de Generacion. ######
                # AGS.reemplazo_padres()
                # AGS.reemplazo_aleatorio()
                # AGS.reemplazo_peor_adaptados()
                # AGS.reemplazo_adaptacion_similar()
                
                # AGS.evaluacion_poblacion()
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
            
        file.write(os.linesep)
        file.write(os.linesep)
        file.write("El Fit promedio del mejor individuo obtenido es: " + str(float(totalfits)/nRepeticiones) + os.linesep)
        file.write("El promedio de generaciones que se mantiene el mejor individuo es: " + str(float(totalGen)/nRepeticiones) + os.linesep)
        finishTimeTotal = time() - startTimeTotal
        t = False
file.write("El experimento N° " + str(cont) + " hizo un tiempo total de %.10f Segundos" %finishTimeTotal + os.linesep)
file.close()