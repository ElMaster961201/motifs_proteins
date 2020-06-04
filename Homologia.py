from Hongos import Hongos as HG 
import os 

class Posicion(object):
    hongos = HG().matrizHongos()
    ind = {'A':0, 'C':1, 'D':2, 'E':3, 'F':4, 'G':5, 'H':6, 'I':7, 'K':8, 'L':9, 'M':10, 'N':11, 'P':12, 'Q':13, 'R':14, 'S':15, 'T':16, 'V':17, 'W':18, 'Y':19, '-':20}
    
    def __init__(self, secsReferencia = [[]]):
        self.secsReferencia = secsReferencia
        self.tamSec = len(self.secsReferencia[0])
        self.numHongos = len(self.hongos)
        self.tamHongo = len(self.hongos[0])
        self.secuenciasDB = []

        # Inicializamos el contador.
        self.contador = [[0 for _ in range(len(self.ind))] for _ in range(self.tamHongo)]   

        for i in range(self.tamHongo):
            for j in range(self.numHongos):
                self.contador[i][self.ind[self.hongos[j][i]]] = self.contador[i][self.ind[self.hongos[j][i]]] + 1
                pass
            pass
        
        for secRef in self.secsReferencia:
            maxhomologo = 0.0
            c = 0
            for i in range(self.tamHongo - self.tamSec):
                cont = 0.0 
                for j in range(self.tamSec):
                    cont = cont + contador[i + j][ind[secRef[j]]]
                    pass
                cont = 100 * float(cont)/(self.tamSec * self.numHongos)
                if cont > maxhomologo:
                    maxhomologo = cont
                    c = i
                    pass
                pass
            self.secuenciasDB.append([c, maxhomologo])
            pass

    def secuenciaHomogenea (self, secsReferencia = [[]]):
        self.secaReferencia = secsReferencia
        self.tamSec = len(self.secsReferencia)
        self.numHongos = len(self.hongos)
        self.tamHongo = len(self.hongos[0])
        self.secuenciasDB = []
        
        # Inicializamos el contador.
        self.contador = [[0 for _ in range(len(self.ind))] for _ in range(self.tamHongo)]   

        for i in range(self.tamHongo):
            for j in range(self.numHongos):
                self.contador[i][self.ind[self.hongos[j][i]]] = self.contador[i][self.ind[self.hongos[j][i]]] + 1
                pass
            pass

        for secRef in self.secsReferencia:
            maxhomologo = 0.0
            c = 0
            for i in range(self.tamHongo - self.tamSec):
                cont = 0.0 
                for j in range(self.tamSec):
                    cont = cont + contador[i + j][ind[secRef[j]]]
                    pass
                cont = 100 * float(cont)/(self.tamSec * self.numHongos)
                if cont > maxhomologo:
                    maxhomologo = cont
                    c = i
                    pass
                pass
            self.secuenciasDB.append([c, maxhomologo])
            pass
        return self.secuenciasDB


if __name__ == "__main__":
    
    hongos = HG().matrizHongos()
    nombres = HG().listaNombres()
    secsReferencia = [
        ['G','S','G','N','F','S','A','I','D','Q'],
        ['L','T','G','M','K','V','A','H','C','D'],
        ['C','E','R','V','G','V','A','Q','Y','D'],
        ['G','P','S','G','H','A','M','P','Q','D'],
        ['T','R','H','F','P','M','Y','G','V','D'],
        ['A','S','Q','K','L','V','G','A','M','F'],
        ['A','W','N','K','G','S','S','I','L','D'],
        ['Y','D','I','V','G','P','N','I','Y','D'],
        ['R','N','S','V','G','V','A','D','V','E'],
        ['R','S','G','V','Q','G','G','I','W','H'],
        ['I','T','L','Y','T','H','W','F','P','K'],
        ['H','D','Y','C','A','P','F','R','T','P'],
        ['V','T','N','I','C','C','F','Y','Y','R'],
        ['Y','Y','P','I','S','L','K','L','A','I'],
        ['A','L','F','L','L','E','L','Y','E','D'],
        ['P','G','G','V','H','K','S','C','P','P'],
        ['L','M','S','V','F','L','M','N','I','W'],
        ['T','K','V','D','L','Y','F','V','M','P'],
        ['R','M','S','A','H','R','P','T','S','Q'],
        ['Q','D','R','A','S','D','V','V','D','D'],
        ['W','M','C','P','Y','A','V','N','L','T'],
        ['T','V','P','Q','H','I','K','L','V','P'],
        ['G','S','P','Y','I','I','P','A','L','F'],
        ['S','M','K','E','Y','I','M','T','Y','M'],
        ['K','Y','V','P','C','K','M','M','V','W'],
        ['Q','Y','P','W','D','A','R','W','L','P'],
        ['F','T','L','N','C','K','T','H','W','V'],
        ['G','A','Y','S','H','E','D','Y','H','F'],
        ['V','M','A','I','D','V','V','N','L','S'],
        ['A','A','C','V','M','C','T','A','T','D'],
        ['A','V','P','G','G','H','D','V','E','G'],
        ['E','N','P','M','T','M','A','L','E','N'],
        ['V','H','V','S','M','E','P','K','N','L'],
        ['G','Y','F','S','R','D','F','C','G','V'],
        ['R','A','L','R','E','D','M','V','P','P'],
        ['F','R','M','H','P','L','L','T','I','G'],
        ['F','T','V','P','I','V','V','P','M','L'],
        ['K','W','V','G','L','D','R','C','K','W'],
        ['D','S','W','V','M','P','F','Q','C','H'],
        ['N','I','M','V','H','R','L','V','G','F'],
        ['N','V','H','V','H','N','I','P','F','F']
    ]

    ind = {'A':0, 'C':1, 'D':2, 'E':3, 'F':4, 'G':5, 'H':6, 'I':7, 'K':8, 'L':9, 'M':10, 'N':11, 'P':12, 'Q':13, 'R':14, 'S':15, 'T':16, 'V':17, 'W':18, 'Y':19, '-':20}
    ruta = "Homologia"
    numHongos = len(hongos)
    tamHongo = len(hongos[0])

    if not os.path.exists(ruta):
        os.makedirs(ruta)
        pass

    conttxt = 1
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

    for secRef in secsReferencia:
        
        while os.path.exists(ruta + "/SecuenciaHomogenea" + str(conttxt) + ".txt"):
            conttxt = conttxt + 1
            pass

        tamSec = len(secRef)
        file = open(ruta + "/SecuenciaHomogenea" + str(conttxt) + ".txt", "w")
        file.write("Secuencia homogenea." + os.linesep)
        file.write(os.linesep)
        file.write("Las secuencia homogenea tiene un tamano: " + str(tamSec) + os.linesep)
        file.write("La secuencia sintetica es: " + str(secRef) + os.linesep)
        
        maxhomologo = 0.0
        c = 0
        for i in range(tamHongo - tamSec):
            cont = 0.0 
            for j in range(tamSec):
                cont = cont + contador[i + j][ind[secRef[j]]]
                pass
            cont = 100 * float(cont)/(tamSec * numHongos)
            if cont > maxhomologo:
                maxhomologo = cont
                c = i
                pass
            pass

        file.write("Homologia maxima: " + str(maxhomologo) + os.linesep)
        file.write(os.linesep)
        file.write("La homologia maxima se encontro entre las columnas " + str(c + 1) + " y " + str(c + tamSec) + os.linesep)
        file.write("Submatriz:" + os.linesep + os.linesep)
        for i in range(numHongos):
            # file.write(str(nombres[i]) + os.linesep)
            file.write(str(hongos[i][c:c + tamSec]) + os.linesep)
            pass
        file.close()

        file = open(ruta + "/Submatriz" + str(conttxt) + ".fasta", "w")
        for i in range(numHongos):
            file.write(str(nombres[i]) + os.linesep)
            file.write(str(hongos[i][c:c + tamSec]) + os.linesep)
            pass
        file.close()

        pass
    pass