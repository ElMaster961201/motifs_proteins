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
        ['W','W','F','G','R','D','C','A','M','M','Y','A','F','K','M','Y','P','L','P','R','W','G','Y','L','N','I','Q','A','R','K'],
        ['R','Y','Y','H','P','E','M','A','R','L','P','T','W','N','H','R','G','I','G','S','Y','T','Y','T','K','V','L','Q','Y','K'],
        ['P','V','K','W','K','H','Y','I','H','K','L','S','I','K','L','M','T','P','C','K','A','W','N','A','N','W','P','Y','H','P'],
        ['L','V','K','C','F','F','W','A','P','L','C','G','Q','S','D','E','P','N','T','L','H','D','I','I','N','N','H','W','I','D'],
        ['C','S','E','L','Y','K','N','M','H','K','L','T','A','Q','L','C','A','S','I','C','Y','G','F','G','N','F','L','E','G','Q'],
        ['H','M','P','N','T','I','P','N','Y','D','G','L','A','H','A','S','P','E','F','R','D','D','D','L','E','E','W','M','H','P'],
        ['D','W','W','K','S','T','C','L','S','V','C','K','N','H','H','N','M','I','A','Y','Q','R','R','S','H','Q','S','H','M','Y'],
        ['D','Y','Q','W','S','I','W','S','T','L','Q','A','T','P','N','L','V','H','V','D','E','C','E','T','W','T','M','R','I','S'],
        ['H','F','E','H','L','D','H','A','C','C','D','D','E','T','V','F','H','E','I','G','Q','V','V','E','A','C','W','H','E','Q'],
        ['D','A','L','M','I','C','W','W','D','V','A','R','R','M','I','H','N','Q','S','A','D','V','H','S','N','W','D','Y','P','Y'],
        ['Y','D','A','K','L','S','F','D','M','T','K','G','S','S','Y','C','I','E','F','D','Y','V','W','S','T','P','E','F','M','S'],
        ['G','H','M','G','E','P','G','S','M','D','F','H','D','D','T','F','V','E','K','E','E','K','F','P','Q','F','H','W','Q','F'],
        ['Q','T','Y','G','D','I','E','R','D','G','G','W','G','G','T','T','D','E','G','Y','M','W','Q','Q','P','E','T','W','T','H'],
        ['P','D','G','D','V','G','S','L','N','Q','Q','H','Y','T','D','P','C','K','G','G','I','V','H','T','V','E','P','M','T','I'],
        ['C','I','G','S','F','F','F','V','L','N','Q','V','D','A','C','M','H','A','N','L','Y','G','Q','K','T','C','E','T','N','L']
        ]
    tamSec = len(secsReferencia[0])
    ruta = "SecuenciaDB"
    numHongos = len(hongos)
    tamHongo = len(hongos[0])
    umbral = 5

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
        file.write("Las secuencia homogenea tiene un tamano " + str(tamSec) + os.linesep)
        file.write("La secuencia referencia es: " + str(secRef) + os.linesep)
        file.write(os.linesep)
        secuenciaDB = []
        for i in range(numHongos):
            secuenciaHongo = []
            print(i)
            for j in range(tamHongo - tamSec):
                cont = 0
                for k in range(tamSec):
                    if secRef[k] == hongos[i][j + k]:
                        cont = cont + 1
                        pass 
                    pass
                secuenciaHongo.append([hongos[i][j : j + tamSec],j,float(cont)])
                pass
            secuenciaDB.append(secuenciaHongo)
            pass
        pro = 1
        for p in secuenciaDB:
            line = False
            for secuencia in p:
                if secuencia[2] > umbral:
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