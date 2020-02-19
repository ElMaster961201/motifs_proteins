from Bio import AlignIO
import os 
import numpy
import math
#help(AlignIO)

counter = [["A", 0], ["C", 0], ["D", 0], ["E", 0], ["F", 0], ["G", 0], ['H', 0], ["I", 0],
           ["K", 0], ["L", 0], ["M", 0], ["N", 0], ["P", 0], ["Q", 0], ["R", 0], ["S", 0],
           ["T", 0], ["V", 0], ["W", 0], ["Y", 0], ["Gap", 0]]

countresults = []
probabilities = []
shannonentropies = []
totalentropies = []


aminoacids = ["Ala", "Cys", "Glu", "Asp", "Phe", "Gly", "His", "Iso", "Lys", "Leu", "Met", "Asn", "Pro", "Gln", "Arg",
              "Ser", "Thr", "Val", "Trp", "Tyr", "Gap"]

alignments = AlignIO.parse(open("Mul.fasta", "r+"), "fasta")



for alignment in alignments:
    print(alignment)
# print(type(alignment))


# print("Cadena resultante de la posición: ", alignment[:, 0])  #muestra la composicion en aa de una columna
print("longitud de las secuencias:", str(alignment.get_alignment_length()))

i = 0

for loop in range(0, alignment.get_alignment_length()):         #Recorrer las columnas

    positions = alignment[:, i]                                 #Asigna la cadena correspondiente a la columna actual

    #COMIENZAN CONTEOS POR IDENTIDAD POR COLUMNA
    counter[0][1] = positions.count('A')
    counter[1][1] = positions.count('C')
    counter[2][1] = positions.count('D')
    counter[3][1] = positions.count('E')
    counter[4][1] = positions.count('F')
    counter[5][1] = positions.count('G')
    counter[6][1] = positions.count('H')
    counter[7][1] = positions.count('I')
    counter[8][1] = positions.count('K')
    counter[9][1] = positions.count('L')
    counter[10][1] = positions.count('M')
    counter[11][1] = positions.count('N')
    counter[12][1] = positions.count('P')
    counter[13][1] = positions.count('Q')
    counter[14][1] = positions.count('R')
    counter[15][1] = positions.count('S')
    counter[16][1] = positions.count('T')
    counter[17][1] = positions.count('V')
    counter[18][1] = positions.count('W')
    counter[19][1] = positions.count('Y')
    counter[20][1] = positions.count('-')

     #HACER CALCULOS(PROBABILIDAD y ENTROPÍA DE SHANNON)

    currentresults = [i, counter[0][1], counter[1][1], counter[2][1], counter[3][1], counter[4][1], counter[5][1],
                      counter[6][1], counter[7][1], counter[8][1], counter[9][1], counter[10][1], counter[11][1],
                      counter[12][1], counter[13][1], counter[14][1], counter[15][1], counter[16][1], counter[17][1],
                      counter[18][1], counter[19][1], counter[20][1]]

    countresults.append(currentresults)                     #Agrega por columna los valores del conteo a una lista

    i = i+1

# print(len(countresults))
#

file = open("Matriz.txt","w")
for result in countresults:
    file.write(str(result) + os.linesep )                              
    print(result)                             #Imprime la lista de listas resultante.
file.close()


probabilities = countresults
total = 0
k = 1
l = 0

for result in countresults:

    for loop in range(1, 21):

        total = total + result[k]

        k = k+1

    k = 1

    for loop in range(1, 21):
        if total > 0:
            probabilities[l][k] = (result[k]/total)

        k = k+1

    k = 1
    l = l + 1
    total = 0

# print("-------------- P R O B A B I L I D A D E S ------------------")
# for element in probabilities:  #Imprime la lista de listas resultante.
#     print(element)




shannonentropies = probabilities
m = 0
n = 0

for element in probabilities:

    for loop in range(1, 20):

        if element[m] == 0.0:

            shannonentropies[n][m] = 0

        elif element[m] == 0:

            shannonentropies[n][m] = 0

        else:

            shannonentropies[n][m] = (-1*element[m]*(math.log(element[m], 20)))     #Cálculo de la entropía para cada
                                                                                    # elemento de cada posición

        m = m+1

    m = 1
    n = n + 1


# print("-------------- ENTROPÍAS ------------------")
# for element in probabilities:  #Imprime la lista de listas resultante.
#     print(element)

k = 0
totalentropy = 0

for result in shannonentropies:

    for loop in range(1, 20):

        totalentropy = totalentropy + result[k]

        k = k+1

    totalentropies.append([shannonentropies.index(result), totalentropy])
    totalentropy = 0
    k = 1

print("-------------- ENTROPÍAS TOTALES ------------------")
file = open("Entropia.txt","w")
for result in totalentropies:  #Imprime la lista de listas resultante.
    print (result)
    file.write(str(result) + os.linesep)
file.close()