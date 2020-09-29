import random
import copy

class SubtitutionalMatrix(object):

    _aa_codon = [["A", 'GCA', 'GCC', 'GCG', 'GCU'], ["C", 'UGC', 'UGU'], ["D", 'GAC', 'GAU'], ["E", 'GAA', 'GAG'],
                ["F", 'UUC', 'UUU'], ["G", 'GGA', 'GGC', 'GGG', 'GGU'], ['H', 'CAC', 'CAU'], ["I", 'AUA', 'AUC', 'AUU'],
                ["K", 'AAA', 'AAG'], ["L", 'CUA', 'CUC', 'CUG', 'CUU', 'UUA', 'UUG'], ["M", 'AUG'], ["N", 'AAC', 'AAU'],
                ["P", 'CCA', 'CCC', 'CCG', 'CCU'], ["Q", 'CAA', 'CAG'], ["R", 'AGA','AGG', 'CGA', 'CGC', 'CGG', 'CGU'],
                ["S", 'AGC', 'AGU', 'UCA', 'UCC', 'UCG', 'UCU'], ["T", 'ACA', 'ACC', 'ACG', 'ACU'],
                ["V", 'GUA', 'GUC', 'GUG', 'GUU'], ["W", 'UGG'], ["Y", 'UAC', 'UAU'], ["-", 'UAA', 'UAG', 'UGA']]

    _aa_point_mut = [["A"], ["C"], ["D"], ["E"], ["F"], ["G"], ["H"], ["I"], ["K"], ["L"], ["M"], ["N"], ["P"], ["Q"], ["R"],
                ["S"], ["T"], ["V"], ["W"], ["Y"], ["-"]]

    _aa_frm_mut_ins = [["A"], ["C"], ["D"], ["E"], ["F"], ["G"], ["H"], ["I"], ["K"], ["L"], ["M"], ["N"], ["P"], ["Q"],
                    ["R"], ["S"], ["T"], ["V"], ["W"], ["Y"], ["-"]]

    _aa_frm_mut_del = [["A"], ["C"], ["D"], ["E"], ["F"], ["G"], ["H"], ["I"], ["K"], ["L"], ["M"], ["N"], ["P"], ["Q"],
                    ["R"], ["S"], ["T"], ["V"], ["W"], ["Y"], ["-"]]

    _nucleotide = [['A'], ['C'], ['G'], ['U']]

    _aa_index = [["A", 0], ["C", 1], ["D", 2], ["E", 3], ["F", 4], ["G", 5], ['H', 6], ["I", 7], ["K", 8], ["L", 9],
            ["M", 10], ["N", 11], ["P", 12], ["Q", 13], ["R", 14], ["S", 15], ["T", 16], ["V", 17], ["W", 18],
            ["Y", 19], ["-", 20]]

    def _insertion(self, i, j):

        for k in range(0, 4):
            x = self._nucleotide[k][0] + (self._aa_codon[i][j])[0:2]
            y = (self._aa_codon[i][j])[0] + self._nucleotide[k][0] + (self._aa_codon[i][j])[1]
            z = (self._aa_codon[i][j])[0:2] + self._nucleotide[k][0]
            self._aa_point_mut[i].append(x)
            self._aa_point_mut[i].append(y)
            self._aa_point_mut[i].append(z)

    def _deletion(self, i, j):

        for k in range(0, 4):
            x = (self._aa_codon[i][j])[1:3] + self._nucleotide[k][0]
            y = (self._aa_codon[i][j])[0] + (self._aa_codon[i][j])[2] + self._nucleotide[k][0]
            z = (self._aa_codon[i][j])[0:2] + self._nucleotide[k][0]
            self._aa_point_mut[i].append(x)
            self._aa_point_mut[i].append(y)
            self._aa_point_mut[i].append(z)

    def _subtitution(self, i, j):

        for k in range(0, 4):
            if self._nucleotide[k][0] != (self._aa_codon[i][j])[0]:
                x = self._nucleotide[k][0] + (self._aa_codon[i][j])[1:3]
                self._aa_point_mut[i].append(x)
        
        for l in range(0, 4):
            if self._nucleotide[l][0] != (self._aa_codon[i][j])[1]:
                y = (self._aa_codon[i][j])[0] + self._nucleotide[l][0] + (self._aa_codon[i][j])[2]
                self._aa_point_mut[i].append(y)
        
        for m in range(0, 4):
            if self._nucleotide[m][0] != (self._aa_codon[i][j])[2]:
                z = (self._aa_codon[i][j])[0:2] + self._nucleotide[m][0]
                self._aa_point_mut[i].append(z)

    def _frm_sft_ins(self, i, j):

        for k in range(0, 4):
            x = self._nucleotide[k][0] + (self._aa_codon[i][j])[0:2]
            self._aa_frm_mut_ins[i].append(x)

    def _frm_sft_del(self, i, j):

        for k in range(0, 4):
            x = (self._aa_codon[i][j])[1:3] + self._nucleotide[k][0]
            self._aa_frm_mut_del[i].append(x)

    def _mutationcounter(self, uu):

        for ww in range(0, len(uu)):
            for ii in range(1, len(uu[ww])):
                xx = uu[ww][ii]
                for jj in range(0, len(self._aa_codon)):
                    for kk in range(1, len(self._aa_codon[jj])):
                        yy = self._aa_codon[jj][kk]
                        zz = self._aa_codon[jj][0]
                        if xx == yy:
                            uu[ww][ii] = zz

    def _matrixsum(self, m_m, vv):

        for i in range(0, len(m_m)):
            for j in range(1, len(m_m[i])):
                for k in range(0, len(self._aa_index)):
                    if m_m[i][j] == self._aa_index[k][0]:
                        n_aa = vv[self._aa_index[i][1]][self._aa_index[k][1]] + 1
                        vv[self._aa_index[i][1]][self._aa_index[k][1]] = n_aa

    def _matrixprobability(self, uu, vv, ww):

        for j in range(0,21):
            for k in range(0,21):
                if (vv[j][k] != 0):
                    n = ((len(uu[j]))-1)
                    nn = vv[j][k]
                    f = nn/n
                    ww[j][k] = f

    def _prob_sum(self, g_g):

        for i in range(0,len(g_g)):
            y = 0
            for j in range (0,len(g_g[i])):
                x = g_g[i][j]
                y = x + y
                if x != 0:
                    g_g[i][j] = y
    
    def __init__(self):

        self._pmm = [[0 for _ in range(len(self._aa_index))] for _ in range(len(self._aa_index))]
        self._fsim = [[0 for _ in range(len(self._aa_index))] for _ in range(len(self._aa_index))]
        self._fsdm = [[0 for _ in range(len(self._aa_index))] for _ in range(len(self._aa_index))]

        self._pmfm = [[0.0 for _ in range(len(self._aa_index))] for _ in range(len(self._aa_index))]
        self._fsifm = [[0.0 for _ in range(len(self._aa_index))] for _ in range(len(self._aa_index))]
        self._fsdfm = [[0.0 for _ in range(len(self._aa_index))] for _ in range(len(self._aa_index))]

        for i in range(0, 21):
            for j in range (1, len(self._aa_codon[i])):
                self._insertion(i,j)
                self._deletion(i,j)
                self._subtitution(i,j)
                self._frm_sft_ins(i,j)
                self._frm_sft_del(i,j)

        self._m_m = [self._aa_point_mut, self._aa_frm_mut_ins, self._aa_frm_mut_del]

        self._e_e = [self._pmm, self._fsim, self._fsdm]

        self.g_g = [self._pmfm, self._fsifm, self._fsdfm]

        #pmfm [mutacion puntual de subtitución] aquí solo se subtituye directo 
        #fsifm [mutación puntual de inserción] una vez que se haya realizado la mutación en x, generar la mutación para cada 
        # a la derecha de esta 
        #fsdfm [mutación puntual de deleción] una vez que se haya realizado la mutación en x, generar la mutación para cada 
        # a la derecha de esta 

        for i in range(0, 3):
            uu = self._m_m[i]
            self._mutationcounter(uu)
            vv = self._e_e[i]
            self._matrixsum(self._m_m[i], vv)
            ww = self.g_g[i]
            self._matrixprobability(uu, vv, ww)

        self.g_g_prom = copy.deepcopy(self.g_g)
        
        for i in range (0,3):
            self._prob_sum(self.g_g_prom[i])

    def gg_ggprom(self):
        """
        Devuelve llas matrices g_g y g_g_prom
        """
        return self.g_g, self.g_g_prom

if __name__ == "__main__":
    import os
    sub_ma = SubtitutionalMatrix()

    if not os.path.exists("Matriz"):
        os.makedirs("Matriz")
        
    file = open("Matriz/subtitucion-Ordenada.txt", "w")
    file2 = open("Matriz/subtitución.txt", "w")
    val = False
    for x in sub_ma.g_g[0]:
        file.write("[")
        for y in x:
            if val:
                file.write(", ")
            file.write(str("{:16.14f}".format(y)))
            val = True
        file.write("]" + os.linesep)
        val = False
        file2.write(str(x) + os.linesep)
    
    file.close()
    file2.close()
    
    file = open("Matriz/inserción-Ordenada.txt", "w")
    file2 = open("Matriz/inserción.txt", "w")
    val = False
    for x in sub_ma.g_g[1]:
        file.write("[")
        for y in x:
            if val:
                file.write(", ")
            file.write(str("{:16.14f}".format(y)))
            val = True
        file.write("]" + os.linesep)
        val = False
        file2.write(str(x) + os.linesep)
    
    file.close()
    file2.close()

    file = open("Matriz/delecion-Ordenada.txt", "w")
    file2 = open("Matriz/delecion.txt", "w")
    val = False
    for x in sub_ma.g_g[2]:
        file.write("[")
        for y in x:
            if val:
                file.write(", ")
            file.write(str("{:16.14f}".format(y)))
            val = True
        file.write("]" + os.linesep)
        val = False
        file2.write(str(x) + os.linesep)
    
    file.close()
    file2.close()

    file = open("Matriz/subtitucion-Prom-Ordenada.txt", "w")
    file2 = open("Matriz/subtitución-Prom.txt", "w")
    val = False
    for x in sub_ma.g_g_prom[0]:
        file.write("[")
        for y in x:
            if val:
                file.write(", ")
            file.write(str("{:16.14f}".format(y)))
            val = True
        file.write("]" + os.linesep)
        val = False
        file2.write(str(x) + os.linesep)
    
    file.close()
    file2.close()
    
    file = open("Matriz/inserción-Prom-Ordenada.txt", "w")
    file2 = open("Matriz/inserción-Prom.txt", "w")
    val = False
    for x in sub_ma.g_g_prom[1]:
        file.write("[")
        for y in x:
            if val:
                file.write(", ")
            file.write(str("{:16.14f}".format(y)))
            val = True
        file.write("]" + os.linesep)
        val = False
        file2.write(str(x) + os.linesep)
    
    file.close()
    file2.close()

    file = open("Matriz/delecion-Prom-Ordenada.txt", "w")
    file2 = open("Matriz/delecion-Prom.txt", "w")
    val = False
    for x in sub_ma.g_g_prom[2]:
        file.write("[")
        for y in x:
            if val:
                file.write(", ")
            file.write(str("{:16.14f}".format(y)))
            val = True
        file.write("]" + os.linesep)
        val = False
        file2.write(str(x) + os.linesep)
    
    file.close()
    file2.close()
