import numpy as np
import random

aa_codon = [["A", 'GCA', 'GCC', 'GCG', 'GCU'], ["C", 'UGC', 'UGU'], ["D", 'GAC', 'GAU'], ["E", 'GAA', 'GAG'],
            ["F", 'UUC', 'UUU'], ["G", 'GGA', 'GGC', 'GGG', 'GGU'], ['H', 'CAC', 'CAU'], ["I", 'AUA', 'AUC', 'AUU'],
            ["K", 'AAA', 'AAG'], ["L", 'CUA', 'CUC', 'CUG', 'CUU', 'UUA', 'UUG'], ["M", 'AUG'], ["N", 'AAC', 'AAU'],
            ["P", 'CCA', 'CCC', 'CCG', 'CCU'], ["Q", 'CAA', 'CAG'], ["R", 'AGA','AGG', 'CGA', 'CGC', 'CGG', 'CGU'],
            ["S", 'AGC', 'AGU', 'UCA', 'UCC', 'UCG', 'UCU'], ["T", 'ACA', 'ACC', 'ACG', 'ACU'],
            ["V", 'GUA', 'GUC', 'GUG', 'GUU'], ["W", 'UGG'], ["Y", 'UAC', 'UAU'], ["*", 'UAA', 'UAG', 'UGA']]

aa_point_mut = [["A"], ["C"], ["D"], ["E"], ["F"], ["G"], ["H"], ["I"], ["K"], ["L"], ["M"], ["N"], ["P"], ["Q"], ["R"],
               ["S"], ["T"], ["V"], ["W"], ["Y"], ["*"]]

aa_frm_mut_ins = [["A"], ["C"], ["D"], ["E"], ["F"], ["G"], ["H"], ["I"], ["K"], ["L"], ["M"], ["N"], ["P"], ["Q"],
                  ["R"], ["S"], ["T"], ["V"], ["W"], ["Y"], ["*"]]

aa_frm_mut_del = [["A"], ["C"], ["D"], ["E"], ["F"], ["G"], ["H"], ["I"], ["K"], ["L"], ["M"], ["N"], ["P"], ["Q"],
                  ["R"], ["S"], ["T"], ["V"], ["W"], ["Y"], ["*"]]

nucleotide = [['A'], ['C'], ['G'], ['U']]

aa_index = [["A", 0], ["C", 1], ["D", 2], ["E", 3], ["F", 4], ["G", 5], ['H', 6], ["I", 7], ["K", 8], ["L", 9],
           ["M", 10], ["N", 11], ["P", 12], ["Q", 13], ["R", 14], ["S", 15], ["T", 16], ["V", 17], ["W", 18],
           ["Y", 19], ["*", 20]]


pmm = np.zeros((len(aa_index), len(aa_index)), int)
fsim = np.zeros((len(aa_index), len(aa_index)), int)
fsdm = np.zeros((len(aa_index), len(aa_index)), int)

pmfm = np.zeros((len(aa_index), len(aa_index)), float)
fsifm = np.zeros((len(aa_index), len(aa_index)), float)
fsdfm = np.zeros((len(aa_index), len(aa_index)), float)

def insertion(i,j):

    for k in range(0, 4):
        x = nucleotide[k][0] + (aa_codon[i][j])[0:2]
        y = (aa_codon[i][j])[0] + nucleotide[k][0] + (aa_codon[i][j])[1]
        z = (aa_codon[i][j])[0:2] + nucleotide[k][0]
        aa_point_mut[i].append(x)
        aa_point_mut[i].append(y)
        aa_point_mut[i].append(z)

def deletion(i,j):

    for k in range(0, 4):
        x = (aa_codon[i][j])[1:3] + nucleotide[k][0]
        y = (aa_codon[i][j])[0] + (aa_codon[i][j])[2] + nucleotide[k][0]
        z = (aa_codon[i][j])[0:2] + nucleotide[k][0]
        aa_point_mut[i].append(x)
        aa_point_mut[i].append(y)
        aa_point_mut[i].append(z)

def subtitution(i,j):

    for k in range(0, 4):
        if nucleotide[k][0] != (aa_codon[i][j])[0]:
            x = nucleotide[k][0] + (aa_codon[i][j])[1:3]
            aa_point_mut[i].append(x)
    for l in range(0, 4):
        if nucleotide[l][0] != (aa_codon[i][j])[1]:
            y = (aa_codon[i][j])[0] + nucleotide[l][0] + (aa_codon[i][j])[2]
            aa_point_mut[i].append(y)
    for m in range(0, 4):
        if nucleotide[m][0] != (aa_codon[i][j])[2]:
            z = (aa_codon[i][j])[0:2] + nucleotide[m][0]
            aa_point_mut[i].append(z)

def frm_sft_ins(i,j):

    for k in range(0, 4):
        x = nucleotide[k][0] + (aa_codon[i][j])[0:2]
        aa_frm_mut_ins[i].append(x)

def frm_sft_del(i,j):

    for k in range(0, 4):
        x = (aa_codon[i][j])[1:3] + nucleotide[k][0]
        aa_frm_mut_del[i].append(x)

def mutationcounter(uu):

    for ww in range(0, len(uu)):
        for ii in range(1, len(uu[ww])):
            xx = uu[ww][ii]
            for jj in range(0, len(aa_codon)):
                for kk in range(1, len(aa_codon[jj])):
                    yy = aa_codon[jj][kk]
                    zz = aa_codon[jj][0]
                    if xx == yy:
                        uu[ww][ii] = zz

def matrixsum(m_m, vv):

    for i in range(0, len(m_m)):
        for j in range(1, len(m_m[i])):
            for k in range(0, len(aa_index)):
                if m_m[i][j] == aa_index[k][0]:
                    n_aa = vv[aa_index[i][1]][aa_index[k][1]] + 1
                    vv[aa_index[i][1]][aa_index[k][1]] = n_aa

def matrixprobability(uu, vv, ww):

    for j in range(0,21):
        for k in range(0,21):
            if (vv[j][k] != 0):
                n = ((len(uu[j]))-1)
                nn = vv[j][k]
                f = nn/n
                ww[j][k] = f

def prob_sum(g_g):

    for i in range(0,len(g_g)):
        y = 0
        for j in range (0,len(g_g)):
            x = g_g[i][j]
            y = x + y
            if x != 0:
                g_g[i][j] = y

for i in range(0, 21):
    for j in range (1, len(aa_codon[i])):
        u = insertion(i,j)
        w = deletion(i,j)
        v = subtitution(i,j)
        uu = frm_sft_ins(i,j)
        ww = frm_sft_del(i,j)

m_m = [aa_point_mut, aa_frm_mut_ins, aa_frm_mut_del]

e_e = [pmm, fsim, fsdm]

g_g = [pmfm, fsifm, fsdfm]

#pmfm [mutacion puntual de subtitución] aquí solo se subtituye directo 
#fsifm [mutación puntual de inserción] una vez que se haya realizado la mutación en x, generar la mutación para cada 
# a la derecha de esta 
#fsdfm [mutación puntual de deleción] una vez que se haya realizado la mutación en x, generar la mutación para cada 
# a la derecha de esta 



for i in range(0, 3):
    uu = m_m[i]
    u = mutationcounter(uu)
    vv = e_e[i]
    w = matrixsum(m_m[i], vv)
    ww = g_g[i]
    x = matrixprobability(uu, vv, ww)

print(g_g)


mut_prob = []

for i in range (0,3):
    prob_sum(g_g[i])

print(g_g)