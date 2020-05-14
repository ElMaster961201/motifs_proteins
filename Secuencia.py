from Hongos import Hongos as HG 
import random
import os 

class Secuencia(object):
    ind = {'A':0, 'C':1, 'D':2, 'E':3, 'F':4, 'G':5, 'H':6, 'I':7, 'K':8, 'L':9, 'M':10, 'N':11, 'P':12, 'Q':13, 'R':14, 'S':15, 'T':16, 'V':17, 'W':18, 'Y':19, '-':20}
    hongos = HG().matrizHongos()
    
    def __init__(self, numSecuenciasConservadas = 50, tamSec = 30):
        self.numSecuenciasConservadas = numSecuenciasConservadas 
        self.tamSec = 30
        self.ConSecCon = []
        for _ in range(self.numSecuenciasConservadas):
            ps = random.randrange(len(self.hongos[0])-self.tamSec)
            sec = []
            sumSecCon = 0 

            # Inicializamos el contador.
            contador = [[0 for _ in range(len(self.ind))] for _ in range(self.tamSec)]

            for i in range(self.tamSec):
                for j in range(len(self.hongos)):
                    contador[i][self.ind[self.hongos[j][i + ps]]] = contador[i][self.ind[self.hongos[j][i + ps]]] +1
                    pass
                pass

            for am in contador:
                index = am.index(max(am))
                if index == 20:
                    am.pop(index)
                    index = am.index(max(am))
                    pass
                sumSecCon = sumSecCon + max(am)
                sec.append(list(self.ind.keys())[index])
                pass
            self.ConSecCon.append([sec, 100 * float(sumSecCon)/(self.tamSec * len(self.hongos)), ps])
            pass
        pass
    

    def ConjuntoSecuenciaConservada(self,numSecuenciasConservadas = 50, tamSec = 30):
        self.numSecuenciasConservadas = numSecuenciasConservadas 
        self.tamSec = 30
        self.ConSecCon = []
        for _ in range(self.numSecuenciasConservadas):
            ps = random.randrange(len(self.hongos[0])-self.tamSec)
            sec = []
            sumSecCon = 0 

            # Inicializamos el contador.
            contador = [[0 for _ in range(len(self.ind))] for _ in range(self.tamSec)]

            for i in range(self.tamSec):
                for j in range(len(self.hongos)):
                    contador[i][self.ind[self.hongos[j][i + ps]]] = contador[i][self.ind[self.hongos[j][i + ps]]] +1
                    pass
                pass

            for am in contador:
                index = am.index(max(am))
                if index == 20:
                    am.pop(index)
                    index = am.index(max(am))
                    pass
                sumSecCon = sumSecCon + max(am)
                sec.append(list(self.ind.keys())[index])
                pass
            self.ConSecCon.append([sec, 100 * float(sumSecCon)/(self.tamSec * len(self.hongos)), ps])
            pass
        return self.ConSecCon


if __name__ == "__main__":
    
    ind = {'A':0, 'C':1, 'D':2, 'E':3, 'F':4, 'G':5, 'H':6, 'I':7, 'K':8, 'L':9, 'M':10, 'N':11, 'P':12, 'Q':13, 'R':14, 'S':15, 'T':16, 'V':17, 'W':18, 'Y':19, '-':20}
    hongos = HG().matrizHongos()
    tamSec = 30
    ruta = "SecuenciaConservada"

    if not os.path.exists(ruta):
        os.makedirs(ruta)
        pass

    if not (os.path.exists(ruta + "/SecuenciaConservada.txt")):
        file = open(ruta + "/SecuenciaConservada.txt","w")
        file.write("Secuencias conservadas." + os.linesep)
        file.write(os.linesep)
        file.write("Las secuencias conservadas tendran un tamano " + str(tamSec) + os.linesep)
        file.write(os.linesep)
        ConSecCon = []
        for ps in range(len(hongos[0])-tamSec):
            file.write("El punto de donde inicia la secuencia conservada es: " + str(ps + 1) + os.linesep)
            sec = []
            sumSecCon = 0 

            # Inicializamos el contador.
            contador = [[0 for _ in range(len(ind))] for _ in range(tamSec)]

            for i in range(tamSec):
                for j in range(len(hongos)):
                    contador[i][ind[hongos[j][i + ps]]] = contador[i][ind[hongos[j][i + ps]]] +1
                    pass
                pass

            for am in contador:
                index = am.index(max(am))
                if index == 20:
                    am.pop(index)
                    index = am.index(max(am))
                    pass
                sumSecCon = sumSecCon + max(am)
                sec.append(list(ind.keys())[index])
                pass
            ConSecCon.append([sec, 100 * float(sumSecCon)/(tamSec * len(hongos))])
            file.write("Secuencia " + str(ps + 1) + os.linesep)
            file.write(str(ConSecCon[ps][0]) + os.linesep)
            file.write("Con " + str(ConSecCon[ps][1]) + " de conservacion" + os.linesep + os.linesep)
            pass
        file.close()
        pass
    pass
