from Hongos import Hongos as HG 
import os 

class Posicion(object):
    hongos = HG().matrizHongos()
    
    def __init__(self, secsReferencia = [[]]):
        self.secsReferencia = secsReferencia
        self.tamSec = len(self.secsReferencia[0])
        self.numHongos = len(self.hongos)
        self.tamHongo = len(self.hongos[0])
        self.secuenciasDB = []
        for secRef in secsReferencia:
            self.secuenciaDB = []
            for i in range(self.numHongos):
                secuenciaHongo = []
                for j in range(self.tamHongo - self.tamSec):
                    cont = 0
                    for k in range(self.tamSec):
                        if secRef[k] == self.hongos[i][j + k]:
                            cont = cont + 1
                            pass 
                        pass
                    secuenciaHongo.append([self.hongos[i][j:j + self.tamSec],j,float(cont)])
                    pass
                self.secuenciaDB.append(secuenciaHongo)
                pass
            self.secuenciasDB.append(self.secuenciaDB)
            pass
        pass

    def secuenciaHomogenea (self, secsReferencia = [[]]):
        self.secaReferencia = secsReferencia
        self.tamSec = len(self.secsReferencia)
        self.numHongos = len(self.hongos)
        self.tamHongo = len(self.hongos[0])
        self.secuenciasDB = []
        for secRef in secsReferencia:
            self.secuenciaDB = []
            for i in range(self.numHongos):
                secuenciaHongo = []
                for j in range(self.tamHongo - self.tamSec):
                    cont = 0
                    for k in range(self.tamSec):
                        if secRef[k] == self.hongos[i][j +k ]:
                            cont = cont + 1
                            pass 
                        pass
                    secuenciaHongo.append([self.hongos[i][j:j + self.tamSec],j,float(cont)])
                    pass
                self.secuenciaDB.append(secuenciaHongo)
                pass
            self.secuenciasDB.append(self.secuenciaDB)
            pass
        return self.secuenciasDB


if __name__ == "__main__":
    
    hongos = HG().matrizHongos()
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
    tamSec = len(secsReferencia[0])
    ruta = "SecuenciaDB/10"
    numHongos = len(hongos)
    tamHongo = len(hongos[0])

    if not os.path.exists(ruta):
        os.makedirs(ruta)
        pass

    conttxt = 1

    for secRef in secsReferencia:
        
        while os.path.exists(ruta + "/SecuenciaHomogenea" + str(conttxt) + ".txt"):
            conttxt = conttxt + 1
            pass

        file = open(ruta + "/SecuenciaHomogenea" + str(conttxt) + ".txt","w")
        file.write("Secuencia homogenea." + os.linesep)
        file.write(os.linesep)
        file.write("Las secuencia homogenea tiene un tamano: " + str(tamSec) + os.linesep)
        file.write("La secuencia referencia es: " + str(secRef) + os.linesep)
        
        secuenciaDB = []
        maxhomologo = 0
        for i in range(numHongos):
            secuenciaHongo = []
            for j in range(tamHongo - tamSec):
                cont = 0
                for k in range(tamSec):
                    if secRef[k] == hongos[i][j + k]:
                        cont = cont + 1
                        pass 
                    pass
                secuenciaHongo.append([hongos[i][j : j + tamSec],j,float(cont)])
                if maxhomologo < cont:
                    maxhomologo = cont
                pass
            secuenciaDB.append(secuenciaHongo)
            pass
        file.write("Homologia maxima: " + str(maxhomologo) + os.linesep)
        file.write(os.linesep)
        pro = 1
        for p in secuenciaDB:
            line = False
            for secuencia in p:
                if secuencia[2] > maxhomologo - (maxhomologo * 0.30):
                    file.write("Proteina numero " + str(pro) + os.linesep)
                    file.write("Inicio: " + str(secuencia[1]) + os.linesep)
                    file.write("Secuencia: " + str(secuencia[0]) + os.linesep)
                    file.write("Homogenea: " + str(secuencia[2]) + os.linesep)
                    file.write(os.linesep)
                    line = True
                    pass
                pass
            pro = pro + 1
            if line:
                file.write(os.linesep)
                pass
            pass
        file.close()
        pass
    pass