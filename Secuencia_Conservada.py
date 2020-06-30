from Hongos import Hongos as HG 
import random
import os 

class SecuenciaConservada(object):
    ind = {'A':0, 'C':1, 'D':2, 'E':3, 'F':4, 'G':5, 'H':6, 'I':7, 'K':8, 'L':9, 'M':10, 'N':11, 'P':12, 'Q':13, 'R':14, 'S':15, 'T':16, 'V':17, 'W':18, 'Y':19, '-':20}
    hongos = HG().matrizHongos()
    numHongos = len(hongos)
    tamHongo = len(hongos[0])
    
    def __init__(self, numSecuenciasConservadas = 50, tamSec = 30):
        self.numSecuenciasConservadas = numSecuenciasConservadas 
        self.tamSec = tamSec
        self.ConSecCon = []

        # Inicializamos el contador.
        self.contador = [[0 for _ in range(len(self.ind))] for _ in range(self.tamHongo)]   

        # contador [i][j] 
        # i -> representa la columna de la secuencia
        # j -> representa la columna de los aminoacidos

        for i in range(self.tamHongo):
            for j in range(self.numHongos):
                self.contador[i][self.ind[self.hongos[j][i]]] = self.contador[i][self.ind[self.hongos[j][i]]] + 1
                pass
            pass

        for _ in range(self.numSecuenciasConservadas):
            ps = random.randrange(len(self.hongos[0]) - self.tamSec)
            sec = []
            sumSecCon = 0 

            for i in range(self.tamSec):
                index = self.contador[ps + i].index(max(self.contador[ps + i]))
                if index == 20:
                    self.contador[ps + i].pop(index)
                    index = self.contador[ps + i].index(max(self.contador[ps + i]))
                    pass
                sumSecCon = sumSecCon + max(self.contador[ps + i])
                sec.append(list(self.ind.keys())[index])
                pass
            self.ConSecCon.append([sec, 100 * float(sumSecCon)/(self.tamSec * len(self.hongos)), ps])
            pass
        pass
    

    def ConjuntoSecuenciaConservada(self, numSecuenciasConservadas = 50, tamSec = 30):
        self.numSecuenciasConservadas = numSecuenciasConservadas 
        self.tamSec = tamSec
        self.ConSecCon = []

        # Inicializamos el contador.
        self.contador = [[0 for _ in range(len(self.ind))] for _ in range(self.tamHongo)]   

        # contador [i][j] 
        # i -> representa la columna de la secuencia
        # j -> representa la columna de los aminoacidos

        for i in range(self.tamHongo):
            for j in range(self.numHongos):
                self.contador[i][self.ind[self.hongos[j][i]]] = self.contador[i][self.ind[self.hongos[j][i]]] + 1
                pass
            pass

        for _ in range(self.numSecuenciasConservadas):
            ps = random.randrange(len(self.hongos[0]) - self.tamSec)
            sec = []
            sumSecCon = 0 

            for i in range(self.tamSec):
                index = self.contador[ps + i].index(max(self.contador[ps + i]))
                if index == 20:
                    self.contador[ps + i].pop(index)
                    index = self.contador[ps + i].index(max(self.contador[ps + i]))
                    pass
                sumSecCon = sumSecCon + max(self.contador[ps + i])
                sec.append(list(self.ind.keys())[index])
                pass
            self.ConSecCon.append([sec, 100 * float(sumSecCon)/(self.tamSec * len(self.hongos)), ps])
            pass
        return self.ConSecCon


if __name__ == "__main__":
    
    ind = {'A':0, 'C':1, 'D':2, 'E':3, 'F':4, 'G':5, 'H':6, 'I':7, 'K':8, 'L':9, 'M':10, 'N':11, 'P':12, 'Q':13, 'R':14, 'S':15, 'T':16, 'V':17, 'W':18, 'Y':19, '-':20}
    hongos = HG().matrizHongos()
    tamSec = 2
    ruta = "SecuenciaConservada"
    numHongos = len(hongos)
    tamHongo = len(hongos[0])
    # Inicializamos el contador.
    contador = [[0 for _ in range(len(ind))] for _ in range(tamHongo)]   

    for i in range(tamHongo):
        for j in range(numHongos):
            contador[i][ind[hongos[j][i]]] = contador[i][ind[hongos[j][i]]] + 1
            pass
        pass

    # contador [i][j] 
    # i -> representa la columna de la secuencia
    # j -> representa la columna de los aminoacidos

    if not os.path.exists(ruta):
        os.makedirs(ruta)
        pass

    while tamSec < 31:
        if not (os.path.exists(ruta + "/SecuenciaConservada" + str(tamSec) + ".txt")):
            file = open(ruta + "/SecuenciaConservada" + str(tamSec) + ".txt", "w")
            file.write("Secuencias conservadas." + os.linesep)
            file.write(os.linesep)
            file.write("Las secuencias conservadas tendran un tamano " + str(tamSec) + os.linesep)
            file.write(os.linesep)
            ConSecCon = []
            top = 0.0

            for ps in range(len(hongos[0]) - tamSec):
                sumSecCon = 0
                sec = []
                for i in range(tamSec):
                    index = contador[ps + i].index(max(contador[ps + i]))
                    if index == 20:
                        contador[ps + i].pop(index)
                        index = contador[ps + i].index(max(contador[ps + i]))
                        pass
                    sumSecCon = sumSecCon + max(contador[ps + i])
                    sec.append(list(ind.keys())[index])
                    pass
                ConSecCon.append([sec, 100 * float(sumSecCon)/(tamSec * len(hongos))])
                if ConSecCon[ps][1] > 80:
                    file.write("Secuencia: " + str(ps + 1) + os.linesep)
                    file.write("El punto de donde inicia la secuencia conservada es: " + str(ps) + os.linesep)
                    file.write(str(ConSecCon[ps][0]) + os.linesep)
                    file.write("Conservacion: " + str(ConSecCon[ps][1]) + os.linesep + os.linesep)
                    if top < ConSecCon[ps][1]:
                        top = ConSecCon[ps][1]
                    pass
                pass
            file.write("Top: " + str(top) + os.linesep + os.linesep)
            file.close()
            pass
        tamSec = tamSec + 1
        pass
    pass
