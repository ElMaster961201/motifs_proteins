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
    # print('Insertion')
    # print(aa_point_mut[i][0])
    for k in range(0, 4):
        x = nucleotide[k][0] + (aa_codon[i][j])[0:2]
        y = (aa_codon[i][j])[0] + nucleotide[k][0] + (aa_codon[i][j])[1]
        z = (aa_codon[i][j])[0:2] + nucleotide[k][0]
        aa_point_mut[i].append(x)
        aa_point_mut[i].append(y)
        aa_point_mut[i].append(z)
        # print('index',aa_point_mut[i])

    #     print('in 0:', x, 'in 1:', y, 'in 2:', z)
    # print(20*'-')

def deletion(i,j):
    # print('Deletion')
    for k in range(0, 4):
        x = (aa_codon[i][j])[1:3] + nucleotide[k][0]
        y = (aa_codon[i][j])[0] + (aa_codon[i][j])[2] + nucleotide[k][0]
        z = (aa_codon[i][j])[0:2] + nucleotide[k][0]
        aa_point_mut[i].append(x)
        aa_point_mut[i].append(y)
        aa_point_mut[i].append(z)
        # print('in 0:', x, 'in 1:', y, 'in 2:', z)
    # print(20 * '-')

def subtitution(i,j):
    # print('Substitution')
    for k in range(0, 4):
        # print('pinche', nucleotide[k][0])
        if nucleotide[k][0] != (aa_codon[i][j])[0]:
            # print('puta', (aa_codon[i][j])[0])
            x = nucleotide[k][0] + (aa_codon[i][j])[1:3]
            aa_point_mut[i].append(x)
            # print(x)
    for l in range(0, 4):
        # print('pin', nucleotide[l][0])
        if nucleotide[l][0] != (aa_codon[i][j])[1]:
            # print('pito', (aa_codon[i][j])[1])
            y = (aa_codon[i][j])[0] + nucleotide[l][0] + (aa_codon[i][j])[2]
            aa_point_mut[i].append(y)
            # print(y)
    for m in range(0, 4):
        # print('che', nucleotide[m][0])
        if nucleotide[m][0] != (aa_codon[i][j])[2]:
            # print('peto', (aa_codon[i][j])[2])
            z = (aa_codon[i][j])[0:2] + nucleotide[m][0]
            aa_point_mut[i].append(z)
            # print(z)
    # print(20 * '-')

def frm_sft_ins(i,j):
    # print('Insertion')
    # print(aa_point_mut[i][0])
    for k in range(0, 4):
        x = nucleotide[k][0] + (aa_codon[i][j])[0:2]
        # y = (aa_codon[i][j])[0] + nucleotide[k][0] + (aa_codon[i][j])[1]
        # z = (aa_codon[i][j])[0:2] + nucleotide[k][0]
        aa_frm_mut_ins[i].append(x)
        # aa_point_mut[i].append(y)
        # aa_point_mut[i].append(z)

def frm_sft_del(i,j):
    # print('Deletion')
    for k in range(0, 4):
        x = (aa_codon[i][j])[1:3] + nucleotide[k][0]
        # y = (aa_codon[i][j])[0] + (aa_codon[i][j])[2] + nucleotide[k][0]
        # z = (aa_codon[i][j])[0:2] + nucleotide[k][0]
        aa_frm_mut_del[i].append(x)
        # aa_point_mut[i].append(y)
        # aa_point_mut[i].append(z)

for i in range(0, 21):
    for j in range (1, len(aa_codon[i])):
        u = insertion(i,j)
        w = deletion(i,j)
        v = subtitution(i,j)
        uu = frm_sft_ins(i,j)
        ww = frm_sft_del(i,j)
        # print(u)
        # print (w)
        # print(v)
# print('frameshif insertion',aa_frm_mut_ins)
# print('frameshift deletion', aa_frm_mut_del)


# for ww in range(0,len(aa_point_mut)):
#     for ii in range(1,len(aa_point_mut[ww])):
#         xx = aa_point_mut[ww][ii]
#         for jj in range(0,len(aa_codon)):
#             for kk in range(1,len(aa_codon[jj])):
#                 yy = aa_codon[jj][kk]
#                 zz = aa_codon[jj][0]
#                 if xx == yy:
#                     aa_point_mut[ww][ii] = zz

def mutationcounter(uu):
    for ww in range(0, len(uu)):
        # print ('ww', ww)
        for ii in range(1, len(uu[ww])):
            # print ('ii', ii)
            xx = uu[ww][ii]
            # print ('xx', xx)
            for jj in range(0, len(aa_codon)):
                # print ('jj', jj)
                for kk in range(1, len(aa_codon[jj])):
                    # print('kk', kk)
                    yy = aa_codon[jj][kk]
                    zz = aa_codon[jj][0]
                    # print ('yy', yy, 'zz', zz)
                    if xx == yy:
                        # print ('si')
                        uu[ww][ii] = zz

def matrixsum(m_m, vv):
    for i in range(0, len(m_m)):
        # print ('i', i)
        for j in range(1, len(m_m[i])):
            # print ('j', j, m_m[i])
            for k in range(0, len(aa_index)):
                # print ('k', k, 'm_m-ij', m_m[i][j])
                # print(aa_index[k][0])
                if m_m[i][j] == aa_index[k][0]:
                    # print(aa_index[i][1], aa_index[k][1])
                    n_aa = vv[aa_index[i][1]][aa_index[k][1]] + 1
                    vv[aa_index[i][1]][aa_index[k][1]] = n_aa

def matrixprobability(uu, vv, ww):
    for j in range(0,21):
        # print ('j', j)
        for k in range(0,21):
            # print ('k', k)
            # n = uu[j]
            # nn = uu[j][k]
            # print('n', type(n), n, 'nn', type(nn), nn)
            if (vv[j][k] != 0):
                n = ((len(uu[j]))-1)
                # print (n)
                nn = vv[j][k]
                # print (nn)
                f = nn/n
                ww[j][k] = f


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
    # print (vv)
    w = matrixsum(m_m[i], vv)
    ww = g_g[i]
    # print(uu)
    x = matrixprobability(uu, vv, ww)
    # print (ww)
    # print (vv)
    # print (u)


# print (aa_point_mut, aa_frm_mut_ins, aa_frm_mut_del)

# pmm = np.zeros((len(aa_index), len(aa_index)), int)  #point mutation matrix
# pmfm = np.zeros((len(aa_index), len(aa_index)), float)  #point mutation frenquency matrix

# e_e = [ppm, fsim, fsdm]

# for i in range(0, len(aa_point_mut)):
#     print ('i', i)
#     for j in range(1, len(aa_point_mut[i])):
#         print ('j', j, aa_point_mut[i])
#         for k in range(0, len(aa_index)):
#             print ('k', k, aa_point_mut[i][j])
#             print(aa_index[k][0])
#             if aa_point_mut[i][j] == aa_index[k][0]:
#                 print('aa', aa_point_mut[i][j], 'i', aa_index[i][1], 'k', aa_index[k][1])
#                 n_aa = pmm[aa_index[i][1]][aa_index[k][1]] + 1
#                 pmm[aa_index[i][1]][aa_index[k][1]] = n_aa
#
#
# print (pmm)


# for i in range(0,21):
#     print ('q', i)
#     for j in range(0,20):
#         print('j', j)
#         # n = aa_frm_mut_ins[i]
#         # nn = aa_frm_mut_ins[i][j]
#         # print(aa_frm_mut_ins)
#         # print('n', type(n), n, 'nn', type(nn), nn)
#         if (fsim[i][j] != 0):
#             n = (len(aa_frm_mut_ins[i]))-1
#             print (n)
#             nn = fsim[i][j]
#             print (nn)
#             f = nn/n
#             fsifm[i][j] = f



# print (pmm)
# print(pmfm)
# print (fsifm)
# print (fsdfm)

# for i in range(0,len(aa_point_mut)):
#     print((len(aa_point_mut[i]))-1)
#
# for i in range(0,len(aa_frm_mut_ins)):
#     print((len(aa_frm_mut_ins[i]))-1)
#
# for i in range(0,len(aa_frm_mut_del)):
#     print((len(aa_frm_mut_del[i]))-1)

y = 0
def prob_sum(g_g, y):
    for i in range(0,len(g_g)):
        # print(i)

        for j in range (0,len(g_g)):
            # print (j)
            x = g_g[i][j]
            # print (x)
            y = x + y
            # print (y)

            if x != 0:
                g_g[i][j] = y

            else:
                pass
        y = 0



# for i in range(0,len(pmfm)):
#     print(i)
#     for j in range (0,len(pmfm)):
#         print (j)
#         x = pmfm[i][j]
#         print (x)
#         x += x
#         print (x)
#         pmfm[i][j] = x
# print(pmfm)

mut_prob = []

def prob_tuple(i, j, pmfm):
    i = int(random.uniform(0,20))
    print ('matrix i', i)
    for j in range(0, len(pmfm)):

        if pmfm[i][j] > 0:
            tp = [pmfm[i][j], aa_index[j][0]]
            mut_prob.append(tp)
    # print (mut_prob)

aa_mut = []

def random_mutation(mut_prob):
    x = random.random()

    for i in range (0, (len(mut_prob))):
        # print(mut_prob[i][0])
        # print('random', x)

        if (x < mut_prob[i][0]):
            # aa_mut.append(mut_prob[i][1])
            print(mut_prob[i][1])
            break

        else:
            pass
    # print (aa_mut)
    # print(aa_mut[0])



for i in range (0,3):
    prob_sum(g_g[i], y)
    # print(g_g[i])

prob_tuple(i,j,pmfm)
random_mutation(mut_prob)

print(g_g)