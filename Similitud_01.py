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
