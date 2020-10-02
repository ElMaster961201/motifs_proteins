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
        ['G','S','G','V','G','V','A','V','V','D'],
        ['G','S','G','C','W','S','G','H','G','G'],
        ['G','S','G','V','G','V','A','I','R','R'],
        ['G','S','G','V','G','S','Q','Y','L','T'],
        ['G','S','G','V','G','C','P','L','S','I'],
        ['G','S','E','L','E','Y','Q','Y','L','I'],
        ['G','S','G','V','E','V','A','I','V','D'],
        ['G','S','G','V','G','V','A','I','V','V'],
        ['G','S','G','V','G','V','A','I','V','V'],
        ['G','S','G','V','G','V','A','H','R','G'],
        ['E','I','L','T','R','S','A','R','I','A'],
        ['G','R','V','E','L','A','T','V','Y','G'],
        ['G','S','D','F','A','L','P','S','F','T'],
        ['G','V','A','I','G','A','G','N','R','Y'],
        ['P','R','G','Q','G','P','C','Y','T','R'],
        ['G','T','G','S','L','C','R','F','L','Y'],
        ['R','A','R','L','S','R','N','C','P','I'],
        ['G','S','S','W','E','L','T','H','W','R'],
        ['R','S','M','A','G','Y','I','Y','V','T'],
        ['R','C','D','A','R','V','M','R','R','D'],
        ['V','E','R','H','C','P','H','P','S','T'],
        ['G','P','G','E','Q','S','S','E','W','A'],
        ['G','S','G','V','G','P','E','T','S','T'],
        ['Q','A','S','R','F','K','V','D','P','F'],
        ['A','T','S','I','V','Q','A','G','G','R'],
        ['G','T','V','R','V','S','H','S','C','R'],
        ['G','S','D','V','G','G','A','I','V','D'],
        ['G','R','R','I','R','L','A','T','G','S'],
        ['R','D','R','L','T','R','H','V','I','I'],
        ['G','R','W','A','K','S','G','P','R','V'],
        ['R','F','S','S','R','L','T','H','A','R'],
        ['G','S','G','F','G','I','C','L','A','N'],
        ['G','S','G','V','G','V','A','Y','R','R'],
        ['G','R','S','C','V','G','C','H','V','N'],
        ['K','P','A','G','C','G','V','L','S','R'],
        ['G','K','A','S','V','S','H','A','R','S'],
        ['G','S','G','V','G','V','A','I','V','E'],
        ['E','S','A','C','I','C','Q','S','H','G'],
        ['T','A','G','E','S','Y','G','P','P','T'],
        ['R','L','R','R','R','G','G','N','V','C']
    ]

    secs_referencia2 = [
        ['G','S','G','V','G','V','A','I','G','D'],
        ['G','S','G','S','R','R','G','H','G','R'],
        ['G','S','G','Y','G','V','A','I','V','D'],
        ['G','S','G','V','D','S','P','L','C','T'],
        ['G','S','G','V','G','V','A','Y','V','D'],
        ['G','S','G','V','G','V','G','I','V','D'],
        ['G','S','G','V','G','R','A','I','V','D'],
        ['G','S','G','V','G','G','A','I','V','D'],
        ['G','S','G','V','G','V','S','Y','S','R'],
        ['G','S','G','V','G','V','A','I','S','D'],
        ['G','S','G','T','T','M','Y','L','S','R'],
        ['G','S','G','V','G','V','A','F','Q','H'],
        ['G','S','G','V','G','V','A','I','V','E'],
        ['G','I','G','R','W','G','G','Y','C','G'],
        ['G','S','G','V','G','V','A','T','V','R'],
        ['G','S','G','V','G','V','A','I','G','D'],
        ['G','L','R','V','G','C','H','L','F','M'],
        ['G','S','G','V','G','V','A','I','V','D'],
        ['G','S','G','V','G','V','A','I','V','D'],
        ['G','S','G','R','W','C','C','Y','G','R'],
        ['G','S','G','L','W','G','C','H','S','R'],
        ['G','T','V','V','A','Y','Y','I','G','Q'],
        ['G','A','A','C','V','G','G','S','S','E'],
        ['G','S','G','V','V','V','K','A','S','M'],
        ['G','S','G','G','G','V','A','I','L','I'],
        ['G','F','D','V','G','S','A','I','S','R'],
        ['G','S','G','V','G','V','H','S','W','T'],
        ['G','C','W','S','R','R','S','D','S','G'],
        ['G','D','V','H','R','C','V','L','K','P'],
        ['G','S','G','V','G','V','A','I','V','D'],
        ['G','S','R','S','R','M','Q','G','S','L'],
        ['G','P','D','P','L','V','I','L','I','G'],
        ['G','S','G','V','G','G','G','Y','S','R'],
        ['G','I','R','C','G','G','S','F','K','Q'],
        ['P','V','S','L','P','S','E','E','V','K'],
        ['G','Q','G','G','R','R','R','H','S','G'],
        ['G','S','G','L','R','R','C','N','I','R'],
        ['G','S','G','V','G','V','A','I','V','D'],
        ['G','S','G','V','G','V','Q','W','I','I'],
        ['G','L','A','S','G','V','L','S','L','N']
    ]

    secs_referencia3 = [
        ['G','S','G','V','R','V','A','I','V','D'],
        ['G','R','G','V','A','V','A','I','G','D'],
        ['G','S','G','V','G','V','A','I','F','M'],
        ['E','Q','G','V','G','V','A','I','V','D'],
        ['G','S','G','V','G','V','A','I','S','T'],
        ['G','S','G','V','G','V','A','T','V','D'],
        ['G','S','G','V','G','V','S','N','G','R'],
        ['G','I','G','V','G','V','A','I','V','D'],
        ['G','S','G','A','G','V','A','I','V','H'],
        ['G','S','G','V','G','V','R','Y','S','R'],
        ['T','L','R','V','L','G','G','I','F','P'],
        ['R','K','I','G','I','S','D','A','K','F'],
        ['F','V','I','I','Y','S','E','P','C','L'],
        ['G','S','G','L','A','Y','V','S','S','S'],
        ['L','T','T','E','G','A','M','Q','T','K'],
        ['A','I','L','V','Q','H','R','F','R','C'],
        ['G','T','G','S','G','S','R','H','G','W'],
        ['V','L','I','V','L','L','L','S','R','T'],
        ['G','L','C','C','R','F','A','P','D','V'],
        ['G','T','N','P','V','R','F','I','M','R'],
        ['G','H','G','E','W','D','R','A','P','V'],
        ['Y','H','Y','R','D','K','Q','P','D','D'],
        ['G','L','I','V','G','P','A','P','S','I'],
        ['G','C','A','R','T','A','V','T','C','R'],
        ['P','L','I','T','R','S','F','I','F','T'],
        ['W','R','R','R','R','F','N','T','S','V'],
        ['G','S','G','V','G','S','Q','S','C','T'],
        ['R','H','A','A','P','G','H','V','K','L'],
        ['W','T','N','L','S','L','E','S','V','H'],
        ['E','S','T','R','A','S','D','Q','T','R'],
        ['A','F','V','V','H','A','F','T','S','W'],
        ['G','V','V','T','F','E','R','Y','E','Y'],
        ['A','F','W','L','P','R','K','L','L','G'],
        ['G','R','R','A','A','V','L','F','S','L'],
        ['G','P','G','V','G','L','D','I','V','E'],
        ['G','S','A','V','D','Y','P','H','G','Q'],
        ['W','S','V','D','P','S','V','S','C','P'],
        ['R','V','G','H','T','S','T','T','R','G'],
        ['I','Q','V','S','D','S','S','A','H','V'],
        ['G','E','R','R','G','L','S','A','L','V']
    ]

    ind = {'A':0, 'C':1, 'D':2, 'E':3, 'F':4, 'G':5, 'H':6, 'I':7, 'K':8, 'L':9, 'M':10, 'N':11, 'P':12, 'Q':13, 'R':14, 'S':15, 'T':16, 'V':17, 'W':18, 'Y':19, '-':20}
    ruta = "SimilitudBiologicaSSAenAMS"
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
    
    file2 = open(ruta + "/SimilitudConcentrada.txt", "w")

    for sec_ref in secs_referencia:
        print(conttxt)
        
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

        file2.write(str(conttxt) + ";" + str(sec_ref) + "; ;" + str(maxhomologo) + ";" + str(c + 2) + os.linesep)

        for i in range(num_hongos):
            # file.write(str(nombres[i]) + os.linesep)
            file.write(str(hongos[i][c:c + tam_sec]) + os.linesep)
        file.close()

        file = open(ruta + "/Submatriz" + str(conttxt) + ".fasta", "w")
        for i in range(num_hongos):
            file.write(str(nombres[i]) + os.linesep)
            file.write(str(hongos[i][c:c + tam_sec]) + os.linesep)
        file.close()
