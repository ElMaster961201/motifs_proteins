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
    secs_referencia = [ #### M15-MP-10
        ['G','S','G','E','G','V','A','I','V','D'],
        ['G','V','G','R','G','S','S','H','G','R'],
        ['G','S','G','V','G','I','A','I','V','D'],
        ['G','S','G','V','G','G','A','I','V','D'],
        ['G','S','G','V','G','V','A','I','G','V'],
        ['G','V','G','V','G','V','A','I','V','D'],
        ['G','S','R','V','G','V','A','I','V','D'],
        ['G','S','G','V','G','V','A','I','L','I'],
        ['G','S','G','V','G','V','A','I','V','T'],
        ['G','S','G','V','G','V','A','N','V','D'],
        ['G','S','G','V','G','V','A','I','V','D'],
        ['G','S','V','A','A','E','Y','R','S','P'],
        ['R','S','G','S','G','A','V','L','V','V'],
        ['D','S','G','V','G','V','L','D','G','Y'],
        ['A','S','D','N','G','S','S','R','Q','E'],
        ['G','L','G','T','G','V','C','D','R','C'],
        ['A','E','N','L','C','M','S','G','E','T'],
        ['G','Y','G','V','G','V','A','I','V','H'],
        ['C','S','R','Q','G','A','S','K','E','H'],
        ['G','V','R','G','W','K','L','R','Q','A'],
        ['A','L','E','A','T','T','S','P','V','Q'],
        ['P','G','L','N','P','Q','S','S','C','L'],
        ['W','H','S','C','G','P','S','H','R','L'],
        ['L','L','R','F','K','Q','S','L','I','T'],
        ['D','S','I','R','R','P','S','T','R','C'],
        ['G','S','G','P','G','G','A','H','L','H'],
        ['E','V','R','H','R','M','S','H','G','R'],
        ['G','S','V','V','G','V','L','I','V','Y'],
        ['P','V','S','T','Y','M','R','P','S','F'],
        ['G','V','A','V','A','N','F','T','E','A'],
        ['G','S','G','V','G','V','A','L','E','S'],
        ['G','L','R','V','R','S','K','V','I','H'],
        ['A','H','V','Y','P','P','T','C','L','P'],
        ['V','S','G','V','A','V','A','I','V','A'],
        ['G','S','G','V','W','L','L','K','I','R'],
        ['G','S','R','F','R','Y','Y','L','D','F'],
        ['G','S','G','V','G','V','D','I','V','D'],
        ['G','T','V','S','A','N','T','P','F','A'],
        ['G','S','R','V','G','S','S','D','S','T'],
        ['G','S','V','N','D','S','T','N','T','A']
    ]

    secs_referencia2 = [ #### M15-UN-10
        ['G','S','G','V','G','V','A','I','V','D']
    ]


    ind = {'A':0, 'C':1, 'D':2, 'E':3, 'F':4, 'G':5, 'H':6, 'I':7, 'K':8, 'L':9, 'M':10, 'N':11, 'P':12, 'Q':13, 'R':14, 'S':15, 'T':16, 'V':17, 'W':18, 'Y':19, '-':20}
    ruta = "SimilitudBiologicaSSAenAMS/M15/MP/10/"
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
