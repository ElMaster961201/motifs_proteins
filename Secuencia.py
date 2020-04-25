from Hongos import Hongos as HG 
import random

class Secuencia(object):


    pass

if __name__ == "__main__":
    
    ind = {'A':0, 'C':1, 'D':2, 'E':3, 'F':4, 'G':5, 'H':6, 'I':7, 'K':8, 'L':9, 'M':10, 'N':11, 'P':12, 'Q':13, 'R':14, 'S':15, 'T':16, 'V':17, 'W':18, 'Y':19, '-':20}
    hongos = HG().matrizHongos()
    tamlen = 30
    tamSec = len(hongos[0])
    ps = random.randrange(tamSec-tamlen)
    cont = [[0 for _ in range(len(ind))] for _ in range(tamlen)]

    print (len(cont))
    print(len(cont[0]))
    print("PS = ",ps)
    print(len(hongos))
    print(len(hongos[523]))
    # print()
    # print()
    # print()
    # for i in range(tamlen):
    #     for j in range(len(hongos)):
    #         # print("i ",i," j ", j)
    #         # if (hongos[j][i] == '>'):
    #         #     print(hongos[j])
    #         # print(hongos[j][i])
    #         # print ("i =", i, "j =",j)
    #         cont[i][ind[hongos[j][i+ps]]] = cont[i][ind[hongos[j][i+ps]]] +1
    #         pass
    #     pass

print(len(cont[0]))
print(cont[0])
print (len(cont))
print(type(ind))
print(list(ind.keys())[1])

# for c in cont:
#     print(c)
#     pass


    # for h in hongos:
    #     print (h[ps:ps+tamlen])
    #     pass
    # print (tamSec)
    # print (len (hongos))
    # print (ps)
    # # print(hongos)
    # pass

# [34, 2, 41, 71, 28, 35, 20, 73, 58, 88, 14, 42, 22, 40, 43, 47, 44, 64, 3, 31, 1024, 0, 0, 0, 0, 0, 0, 0, 0, 0]


