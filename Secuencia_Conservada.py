from Hongos import Hongos as HG 
import random
import os 

class SecuenciaConservada(object):
    ind = {'A':0, 'C':1, 'D':2, 'E':3, 'F':4, 'G':5, 'H':6, 'I':7, 'K':8, 'L':9, 'M':10, 'N':11, 'P':12, 'Q':13, 'R':14, 'S':15, 'T':16, 'V':17, 'W':18, 'Y':19, '-':20}
    hongos = HG().matrizHongos()
    num_hongos = len(hongos)
    tam_hongo = len(hongos[0])
    
    def __init__(self, num_secuencias_conservadas = 50, tam_sec = 30):
        self.num_secuencias_conservadas = num_secuencias_conservadas 
        self.tam_sec = tam_sec
        self.con_sec_con = []

        # Inicializamos el contador.
        self.contador = [[0 for _ in range(len(self.ind))] for _ in range(self.tam_hongo)]   

        # contador [i][j] 
        # i -> representa la columna de la secuencia
        # j -> representa la columna de los aminoacidos

        for i in range(self.tam_hongo):
            for j in range(self.num_hongos):
                self.contador[i][self.ind[self.hongos[j][i]]] = self.contador[i][self.ind[self.hongos[j][i]]] + 1

        for _ in range(self.num_secuencias_conservadas):
            ps = random.randrange(len(self.hongos[0]) - self.tam_sec)
            sec = []
            sum_sec_con = 0 

            for i in range(self.tam_sec):
                index = self.contador[ps + i].index(max(self.contador[ps + i]))
                if index == 20:
                    self.contador[ps + i].pop(index)
                    index = self.contador[ps + i].index(max(self.contador[ps + i]))
                sum_sec_con = sum_sec_con + max(self.contador[ps + i])
                sec.append(list(self.ind.keys())[index])
            self.con_sec_con.append([sec, 100 * float(sum_sec_con)/(self.tam_sec * len(self.hongos)), ps])

    def conjunto_secuencia_conservada(self, num_secuencias_conservadas = 50, tam_sec = 30):
        self.num_secuencias_conservadas = num_secuencias_conservadas 
        self.tam_sec = tam_sec
        self.con_sec_con = []

        # Inicializamos el contador.
        self.contador = [[0 for _ in range(len(self.ind))] for _ in range(self.tam_hongo)]   

        # contador [i][j] 
        # i -> representa la columna de la secuencia
        # j -> representa la columna de los aminoacidos

        for i in range(self.tam_hongo):
            for j in range(self.num_hongos):
                self.contador[i][self.ind[self.hongos[j][i]]] = self.contador[i][self.ind[self.hongos[j][i]]] + 1

        for _ in range(self.num_secuencias_conservadas):
            ps = random.randrange(len(self.hongos[0]) - self.tam_sec)
            sec = []
            sum_sec_con = 0 

            for i in range(self.tam_sec):
                index = self.contador[ps + i].index(max(self.contador[ps + i]))
                if index == 20:
                    self.contador[ps + i].pop(index)
                    index = self.contador[ps + i].index(max(self.contador[ps + i]))
                sum_sec_con = sum_sec_con + max(self.contador[ps + i])
                sec.append(list(self.ind.keys())[index])
            self.con_sec_con.append([sec, 100 * float(sum_sec_con)/(self.tam_sec * len(self.hongos)), ps])
        return self.con_sec_con


if __name__ == "__main__":
    
    ind = {'A':0, 'C':1, 'D':2, 'E':3, 'F':4, 'G':5, 'H':6, 'I':7, 'K':8, 'L':9, 'M':10, 'N':11, 'P':12, 'Q':13, 'R':14, 'S':15, 'T':16, 'V':17, 'W':18, 'Y':19, '-':20}
    hongos = HG().matrizHongos()
    tam_sec = 2
    ruta = "SecuenciaConservada"
    num_hongos = len(hongos)
    tam_hongo = len(hongos[0])
    # Inicializamos el contador.
    contador = [[0 for _ in range(len(ind))] for _ in range(tam_hongo)]   

    for i in range(tam_hongo):
        for j in range(num_hongos):
            contador[i][ind[hongos[j][i]]] = contador[i][ind[hongos[j][i]]] + 1

    # contador [i][j] 
    # i -> representa la columna de la secuencia
    # j -> representa la columna de los aminoacidos

    if not os.path.exists(ruta):
        os.makedirs(ruta)

    while tam_sec < 31:
        if not (os.path.exists(ruta + "/SecuenciaConservada" + str(tam_sec) + ".txt")):
            file = open(ruta + "/SecuenciaConservada" + str(tam_sec) + ".txt", "w")
            file.write("Secuencias conservadas." + os.linesep)
            file.write(os.linesep)
            file.write("Las secuencias conservadas tendran un tamano " + str(tam_sec) + os.linesep)
            file.write(os.linesep)
            con_sec_con = []
            top = 0.0

            for ps in range(len(hongos[0]) - tam_sec):
                sum_sec_con = 0
                sec = []
                for i in range(tam_sec):
                    index = contador[ps + i].index(max(contador[ps + i]))
                    if index == 20:
                        contador[ps + i].pop(index)
                        index = contador[ps + i].index(max(contador[ps + i]))
                    sum_sec_con = sum_sec_con + max(contador[ps + i])
                    sec.append(list(ind.keys())[index])
                con_sec_con.append([sec, 100 * float(sum_sec_con)/(tam_sec * len(hongos))])
                if con_sec_con[ps][1] > 80:
                    file.write("Secuencia: " + str(ps + 1) + os.linesep)
                    file.write("El punto de donde inicia la secuencia conservada es: " + str(ps) + os.linesep)
                    file.write(str(con_sec_con[ps][0]) + os.linesep)
                    file.write("Conservacion: " + str(con_sec_con[ps][1]) + os.linesep + os.linesep)
                    if top < con_sec_con[ps][1]:
                        top = con_sec_con[ps][1]
            file.write("Top: " + str(top) + os.linesep + os.linesep)
            file.close()
        tam_sec = tam_sec + 1
