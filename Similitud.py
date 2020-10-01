from Hongos import Hongos as HG 
import os 

class Similitud(object):
    hongos = HG().matriz_hongos()
    ind = {'A':0, 'C':1, 'D':2, 'E':3, 'F':4, 'G':5, 'H':6, 'I':7, 'K':8, 'L':9, 'M':10, 'N':11, 'P':12, 'Q':13, 'R':14, 'S':15, 'T':16, 'V':17, 'W':18, 'Y':19, '-':20}
    
    def __init__(self, secs_referencia = None):
        if secs_referencia is None:
            self.secs_referencia = list()
        else:
            self.secs_referencia = secs_referencia
        self.tam_sec = len(self.secs_referencia[0])
        self.num_hongos = len(self.hongos)
        self.tam_hongo = len(self.hongos[0])
        self.secuencias_db = []

        # Inicializamos el contador.
        self.contador = [[0 for _ in range(len(self.ind))] for _ in range(self.tam_hongo)]   

        for i in range(self.tam_hongo):
            for j in range(self.num_hongos):
                self.contador[i][self.ind[self.hongos[j][i]]] = self.contador[i][self.ind[self.hongos[j][i]]] + 1
        
        for sec_ref in self.secs_referencia:
            maxhomologo = 0.0
            c = 0
            for i in range(self.tam_hongo - self.tam_sec):
                cont = 0.0 
                for j in range(self.tam_sec):
                    cont = cont + contador[i + j][ind[sec_ref[j]]]
                cont = 100 * float(cont)/(self.tam_sec * self.num_hongos)
                if cont > maxhomologo:
                    maxhomologo = cont
                    c = i
            self.secuencias_db.append([c, maxhomologo])

    def secuencia_homogenea (self, secs_referencia = None):
        if secs_referencia is None:
            self.secs_referencia = list()
        else:
            self.seca_referencia = secs_referencia
        self.tam_sec = len(self.secs_referencia)
        self.num_hongos = len(self.hongos)
        self.tam_hongo = len(self.hongos[0])
        self.secuencias_db = []
        
        # Inicializamos el contador.
        self.contador = [[0 for _ in range(len(self.ind))] for _ in range(self.tam_hongo)]   

        for i in range(self.tam_hongo):
            for j in range(self.num_hongos):
                self.contador[i][self.ind[self.hongos[j][i]]] = self.contador[i][self.ind[self.hongos[j][i]]] + 1

        for sec_ref in self.secs_referencia:
            maxhomologo = 0.0
            c = 0
            for i in range(self.tam_hongo - self.tam_sec):
                cont = 0.0 
                for j in range(self.tam_sec):
                    cont = cont + contador[i + j][ind[sec_ref[j]]]
                cont = 100 * float(cont)/(self.tam_sec * self.num_hongos)
                if cont > maxhomologo:
                    maxhomologo = cont
                    c = i
            self.secuencias_db.append([c, maxhomologo])
        return self.secuencias_db


if __name__ == "__main__":
    
    hongos = HG().matriz_hongos()
    nombres = HG().lista_nombres()
    secs_referencia = [
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
    ruta = "SimilitudSSAenAMS"
    num_hongos = len(hongos)
    tam_hongo = len(hongos[0])

    if not os.path.exists(ruta):
        os.makedirs(ruta)

    conttxt = 1
    # Inicializamos el contador.
    contador = [[0 for _ in range(len(ind))] for _ in range(tam_hongo)]   

    for i in range(tam_hongo):
        for j in range(num_hongos):
            contador[i][ind[hongos[j][i]]] = contador[i][ind[hongos[j][i]]] + 1

    # contador [i][j] 
    # i -> representa la columna de la secuencia
    # j -> representa la columna de los aminoacidos

    for sec_ref in secs_referencia:
        
        while os.path.exists(ruta + "/Similitud" + str(conttxt) + ".txt"):
            conttxt = conttxt + 1

        tam_sec = len(sec_ref)
        file = open(ruta + "/Similitud" + str(conttxt) + ".txt", "w")
        file.write("Similitud de la secuencia en el alineamiento multiple." + os.linesep)
        file.write(os.linesep)
        file.write("Las secuencia tiene un tamano: " + str(tam_sec) + os.linesep)
        file.write("La secuencia sintetica es: " + str(sec_ref) + os.linesep)
        
        maxhomologo = 0.0
        c = 0
        for i in range(tam_hongo - tam_sec):
            cont = 0.0 
            for j in range(tam_sec):
                cont = cont + contador[i + j][ind[sec_ref[j]]]
            cont = 100 * float(cont)/(tam_sec * num_hongos)
            if cont > maxhomologo:
                maxhomologo = cont
                c = i

        file.write("Similitud maxima: " + str(maxhomologo) + os.linesep)
        file.write(os.linesep)
        file.write("La similitud maxima se encontro entre las columnas " + str(c + 1) + " y " + str(c + tam_sec) + os.linesep)
        file.write("Submatriz:" + os.linesep + os.linesep)
        for i in range(num_hongos):
            # file.write(str(nombres[i]) + os.linesep)
            file.write(str(hongos[i][c:c + tam_sec]) + os.linesep)
        file.close()

        file = open(ruta + "/Submatriz" + str(conttxt) + ".fasta", "w")
        for i in range(num_hongos):
            file.write(str(nombres[i]) + os.linesep)
            file.write(str(hongos[i][c:c + tam_sec]) + os.linesep)
        file.close()
