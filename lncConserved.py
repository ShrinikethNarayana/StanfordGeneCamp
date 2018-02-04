import anydbm
from pyentrp import entropy as ent
import numpy as np
import time

entrps = np.load('lncEntropies.npy')

numLncH = anydbm.open('lncH', 'c')
numLncM = anydbm.open('lncM', 'c')

lncEntrpH = anydbm.open('lncEntrpH', 'c')
lncEntrpM = anydbm.open('lncEntrpM', 'c')

conserved = {}

print len(entrps)
print len(lncEntrpH)



for entrp in entrps:
    seqs = lncEntrpM[entrp].split()
    seqs = set(seqs)
    for seq in lncEntrpH[entrp].split():
        if seq in seqs:
            conserved.append(seq)


conserved = np.array(conserved)
np.save('conserved', conserved)









#for entrp in entrpH:
#    print entrp

#enterpIntersect = [x for x in entrp1 if x in entrp2]

#e1, e2 are sorted lists of doubles; return intersect of the 2 lists
'''
def getEntropyIntersect(e1, e2):
    intersect = []
    i1, i2 = 0, 0
    while i1 < len(e1) and i2 < len(e2):
        if e1[i1] == e2[i2]:
            intersect.append(e1[i1])
            i1 += 1
        elif e1[i1] > e2[i2]:
            i1 += 1
        else:
            i2 += 1

    return intersect
'''
#print len(getEntropyIntersect(entrpH, entrpM))
'''
for entrp1 in entrpH:
    for entrp2 in entrpM:
        if entrp2 < entrp1:
            break
        if entrp1 == entrp2:
            seqsM = lncEntrpM[entrp1].split()
            for seq in lncEntrpH[entrp2].split():
                if seq in seqsM:
                    print seq + ' ' + entrp1
'''