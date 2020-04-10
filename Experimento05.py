import os 
from time import time

# Se importa nuestra clase
from Genetico_Motifs import Genetico
from Parametros import Parametros 

# Se obtrienen los parametros a utilizar de una clase. 
p,nGeneraciones,nRepeticiones = Parametros().parametros()

cont = 1

while cont < 10:
    t = True
    while t:
        if (os.path.exists("Experimento" + str(cont) + ".txt")):
            cont = cont + 1 
        else:
            print("Ciclo: ",cont)
            startTimeTotal = time ()

            file = open("Experimento" + str(cont) + ".txt","w")
            file.write("Experimento v0.5."+ str(cont) + os.linesep)
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
            file.write("Secuencia base: " + str(p[9]) + os.linesep)
            file.write("El Experimento se realizo " + str(nRepeticiones) + " veces." + os.linesep)
            file.write("Con " +str(nGeneraciones)+" Generaciones" + os.linesep)

            file.write(os.linesep)
            file.write("Con los siguientes metodos: " + os.linesep)
            
            # Cambiar segun la prueba
            ##### Metodos de Seleccion. ######
            # file.write("Ruleta" + os.linesep)
            # file.write("Estocastico Universal" + os.linesep)
            # file.write("Torneo" + os.linesep)
            # file.write("Restos" + os.linesep)
            ###### Metodos de Cruzamiento. ######
            # file.write("Punto Fijo" + os.linesep)
            # file.write("Multi-Punto" + os.linesep)
            ###### Metodos de Mutacion. ######
            # file.write("Mutacion Uniforme" + os.linesep)
            # file.write("Mutacion Estandar" + os.linesep)
            ###### Metodo de conservacion. ######
            # file.write("Elitismo" + os.linesep)
            ###### Metodo de Paso de Generacion. ######
            # file.write("Remplazo de Padres" + os.linesep)
            # file.write("Remplazo Aleatorio" + os.linesep)
            # file.write("Remplazo de los Peor Adaptados" + os.linesep)
            # file.write("Remplazo de Adaptacion Similar" + os.linesep)

            totalfits = 0.0
            for _ in range(nRepeticiones):
                startTimeExperimento = time ()
                file.write(os.linesep)
                file.write("Los resultados obtenidos en el experimento N° 1." + str(_ + 1 ) + os.linesep)
                AGS = Genetico(p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8])
                for i in range(nGeneraciones):
                    AGS.fits(p[9])

                    ##### Metodos de Seleccion. ######
                    # AGS.ruleta()
                    # AGS.estocasticoUniversal()
                    # AGS.torneo()
                    # AGS.restos()

                    ###### Metodos de Cruzamiento. ######
                    # AGS.puntoFijo()
                    # AGS.multiPunto()

                    ###### Metodos de Mutacion. ######
                    # AGS.mutacionEstandar()
                    # AGS.mutacionUniforme()

                    ###### Metodo de conservacion. ######
                    # AGS.elitismo()

                    ###### Metodo de Paso de Generacion. ######
                    # AGS.remplazoPadres()
                    # AGS.remplazoAleatorio()
                    # AGS.remplazoPeorAdaptados()
                    # AGS.remplazoAdaptacionSimilar()

                    pass
                finishTimeexperimento = time() - startTimeExperimento

                file.write("fits promedio del experimento N° 1." + str(cont) + "." + str(_ + 1) + str(float(sum(AGS.fit))/AGS.tamPoblacion) + os.linesep)
                file.write("El Mejor individuo: " + os.linesep)
                mejor = AGS.mejor
                file.write("Individuo " + str(mejor[0]) + os.linesep)
                file.write("Fits " + str(mejor[1]) + os.linesep)
                file.write("El mejor individuo se mantuvo " + str(mejor[2]) + " Generaciones" + os.linesep)
                
                file.write("El experimento N° 1." + str(_ + 1) + " hizo un tiempo de %.10f Segundos" %finishTimeexperimento + os.linesep)
                totalfits = mejor[1] + totalfits
                pass
            file.write("El Fit promedio del experimiento es: " + str(float(totalfits)/nRepeticiones) + os.linesep)
            finishTimeTotal = time() - startTimeTotal
            t = False
            pass
        pass
    file.write(os.linesep)
    file.write(os.linesep)
    file.write("El experimento N° 1 hizo un tiempo total de %.10f Segundos" %finishTimeTotal + os.linesep)
    file.close()
    pass 