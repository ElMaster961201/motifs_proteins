from Hongos import Hongos as HG 
import os 

class Posicion(object):
    hongos = HG().matrizHongos()
    
    def __init__(self, secReferencia = []):
        self.secReferencia = secReferencia
        self.tamSec = len(secReferencia)
        self.secuenciaDB = []
        self.numHongos = len(self.hongos)
        self.tamHongo = len(self.hongos[0])
        for i in range(self.numHongos):
            secuenciaHongo = []
            for j in range(self.tamHongo - self.tamSec):
                cont = 0
                for k in range(self.tamSec):
                    if self.secReferencia[k] == self.hongos[i][j +k]:
                        cont = cont + 1
                        pass 
                    pass
                secuenciaHongo.append([self.hongos[i][j:j + self.tamSec],j,float(cont)/float(self.tamSec)])
                pass
            self.secuenciaDB.append(secuenciaHongo)
            pass
        pass

    def secuenciaHomogenea (self, secReferencia = []):
        self.secReferencia = secReferencia
        self.tamSec = len(secReferencia)
        self.secuenciaDB = []
        self.numHongos = len(self.hongos)
        self.tamHongo = len(self.hongos[0])
        for i in range(self.numHongos):
            secuenciaHongo = []
            for j in range(self.tamHongo - self.tamSec):
                cont = 0
                for k in range(self.tamSec):
                    if self.secReferencia[k] == self.hongos[i][j +k]:
                        cont = cont + 1
                        pass 
                    pass
                secuenciaHongo.append([self.hongos[i][j:j + self.tamSec], j, cont])
                pass
            self.secuenciaDB.append(secuenciaHongo)
            pass
        return self.secuenciaDB


if __name__ == "__main__":
    
    hongos = HG().matrizHongos()
    secReferencia = ['W', 'W', 'F', 'G', 'R', 'D', 'C', 'A', 'M', 'M', 'Y', 'A', 'F', 'K', 'M', 'Y', 'P', 'L', 'P', 'R', 'W', 'G', 'Y', 'L', 'N', 'I', 'Q', 'A', 'R', 'K']
    tamSec = len(secReferencia)
    ruta = "SecuenciaDB"
    secuenciaDB = []
    numHongos = len(hongos)
    tamHongo = len(hongos[0])

    if not os.path.exists(ruta):
        os.makedirs(ruta)
        pass

    if not (os.path.exists(ruta + "/SecuenciaHomogenea.txt")):
        file = open(ruta + "/SecuenciaHomogenea.txt","w")
        file.write("Secuencia homogenea." + os.linesep)
        file.write(os.linesep)
        file.write("Las secuencia homogenea tiene un tamano " + str(tamSec) + os.linesep)
        file.write("La secuencia referencia es: " + str(secReferencia) + os.linesep)
        file.write(os.linesep)
        for i in range(numHongos):
            secuenciaHongo = []
            print(i)
            for j in range(tamHongo - tamSec):
                cont = 0
                for k in range(tamSec):
                    if secReferencia[k] == hongos[i][j +k]:
                        cont = cont + 1
                        pass 
                    pass
                secuenciaHongo.append([hongos[i][j : j + tamSec], j, cont])
                pass
            secuenciaDB.append(secuenciaHongo)
            pass
        pro = 1
        for p in secuenciaDB:
            for secuencia in p:
                file.write("Proteina numero " + str(pro) + os.linesep)
                file.write("Inicio: " + str(secuencia[1]) + os.linesep)
                file.write("Secuencia: " + str(secuencia[0]) + os.linesep)
                file.write("Homogenea: " + str(secuencia[2]) + os.linesep)
                file.write(os.linesep)
                pass
            pro = pro + 1
            file.write(os.linesep)
            pass
        file.close()
        pass
    pass