import os 
from time import time
import sys
sys.path.append(".")

# Se importa nuestra clase
from DisenoExperimentoGP.Parametros_GP import ParametrosGP
from Genetico_Posiciones import GeneticoPosiciones
# Se obtrienen los parametros a utilizar de una clase. 
p,nGeneraciones,nRepeticiones = ParametrosGP().parametros()

cont = 1
t = True
ruta = "DisenoExperimentoGP/Resultados/Compu" # Ingresa el nombre de la carpeta donde se guardara el archico generado.

if not os.path.exists(ruta):
    os.makedirs(ruta)
    pass

while t:
    if (os.path.exists(ruta + "/Experimento" + str(cont) + ".txt")):
        cont = cont + 1 
    else:
        startTimeTotal = time ()

        file = open(ruta + "/Experimento" + str(cont) + ".txt","w")
        file.write("Experimento v0.1."+ str(cont) + os.linesep)
        file.write("Con los siguientes parametros:" + os.linesep)
        file.write(os.linesep)
        file.write("Tamano de la poblacion: " + str(p[0]) + os.linesep)
        file.write("Numero de Genomas: " + str(p[1]))
        file.write("Numero de Secuencias Consenso: " + str(p[2]))
        file.write("Probabilidad de Mutacion: " + str(p[3]) + os.linesep)
        file.write("Cantidad de Secuencias a mutar: " + str(p[4]) + os.linesep)
        file.write("Numero de individuos seleccionado por Elitismo: " + str(p[5]) + os.linesep)
        file.write("Tamano de k en estocastico universal: " + str(p[6]) + os.linesep)
        file.write("Tamano de torneo: " + str(p[7]) + os.linesep)
        file.write("Numero de restos: " + str(p[8]) + os.linesep)
        file.write("Probabilidad de Cruce: " + str(p[9]) + os.linesep)
        file.write("Secuencia sintetica: " + str(p[10]) + os.linesep)
        file.write("El Experimento se realizo " + str(nRepeticiones) + " veces." + os.linesep)
        file.write("Con " +str(nGeneraciones)+" Generaciones" + os.linesep)

        file.write(os.linesep)
        file.write("Con los siguientes metodos: " + os.linesep)
        
        # Cambiar segun la prueba
        ##### Metodos de Seleccion. ######
        file.write("Ruleta" + os.linesep)
        # file.write("Estocastico Universal" + os.linesep)
        # file.write("Torneo" + os.linesep)
        # file.write("Restos" + os.linesep)

        ###### Metodos de Cruzamiento. ######
        file.write("Punto Fijo" + os.linesep)
        # file.write("Multi-Punto" + os.linesep)
        # file.write("Cruzamiento Uniforme" + os.linesep)
        # file.write("Cruzamiento Aritmetico" + os.linesep)

        ###### Metodos de Mutacion. ######
        file.write("Mutacion Uniforme" + os.linesep)
        # file.write("Mutacion Estandar" + os.linesep)

        ###### Metodo de conservacion. ######
        file.write("Elitismo" + os.linesep)
        
        ###### Metodo de Paso de Generacion. ######
        file.write("Reemplazo de Padres" + os.linesep)
        # file.write("Reemplazo Aleatorio" + os.linesep)
        # file.write("Reemplazo de los Peor Adaptados" + os.linesep)
        # file.write("Reemplazo de Adaptacion Similar" + os.linesep)

        for _ in range(nRepeticiones):
            print ("Repeticion ",_ + 1)
            startTimeExperimento = time ()
            file.write(os.linesep)
            file.write("Los resultados obtenidos en la repeticion " + str(_ + 1 ) + os.linesep)
            AGS = GeneticoPosiciones(p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9])
            AGS.evaluacionPoblacion(p[10])
            for i in range(nGeneraciones):

                ##### Metodos de Seleccion. ######
                AGS.ruleta()
                # AGS.estocasticoUniversal()
                # AGS.torneo()
                # AGS.restos()

                ###### Metodos de Cruzamiento. ######
                AGS.cruzamientoPuntoFijo()
                # AGS.cruzamientoMultiPunto()
                # AGS.cruzamientoUniforme()
                # AGS.cruzamientoAritmetico()

                ###### Metodos de Mutacion. ######
                AGS.mutacionUniforme()
                # AGS.mutacionEstandar()

                ###### Metodo de conservacion. ######
                AGS.elitismo()

                ###### Metodo de Paso de Generacion. ######
                AGS.reemplazoPadres()
                # AGS.reemplazoAleatorio()
                # AGS.reemplazoPeorAdaptados()
                # AGS.reemplazoAdaptacionSimilar()
                
                AGS.evaluacionPoblacion(p[10])
                pass
            finishTimeexperimento = time() - startTimeExperimento

            file.write("Fits promedio de la ultima generacion es: " + str(float(sum(AGS.adaptacion))/AGS.tamPoblacion) + os.linesep)
            file.write("El Mejor individuo: " + os.linesep)
            mejor = AGS.mejor
            file.write("Individuo " + str(mejor[0]) + os.linesep)
            file.write("Fits " + str(mejor[1]) + os.linesep)
            file.write("El mejor individuo se mantuvo " + str(mejor[2]) + " Generaciones" + os.linesep)
            file.write("Las secuencias encontradas son: " + os.linesep)
            k = AGS.secuenciaAdaptacion(AGS.mejor[0])
            for j in range(AGS.numHongos):
                file.write("Hongo " + str(j + 1) + os.linesep)
                file.write("Secuencia: " + str(k[j][0]) + os.linesep)
                file.write("Compatibilidad: " + str(k[j][1]) + os.linesep)
                file.write("Inicio: " + str(AGS.mejor[0][j]) + os.linesep)
                pass
            file.write(os.linesep)
            file.write("La repeticion " + str(_ + 1) + " hizo un tiempo de %.10f Segundos" %finishTimeexperimento + os.linesep)
            pass
        file.write(os.linesep)
        file.write(os.linesep)
        finishTimeTotal = time() - startTimeTotal
        t = False
        pass
    pass
file.write("El experimento N° " + str(cont) + " hizo un tiempo total de %.10f Segundos" %finishTimeTotal + os.linesep)
file.close()
