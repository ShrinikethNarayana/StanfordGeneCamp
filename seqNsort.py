from collections import defaultdict
from Bio import SeqIO
import time
from pyentrp import entropy as ent
import numpy as np

dict1 = {}
dict1 = defaultdict(lambda:0, dict1)


count = 0
for lnc in SeqIO.parse('notNONCODE2016_human.fa', 'fasta'):
    lnc = str(lnc.seq)
    subSeq = lnc[:24]
    for num in range(0, len(lnc) - 24):
        subSeq += lnc[num+24]

        dict1[subSeq] += 1
        subSeq = subSeq[1:]

    count += 1
    print str(count)


print 'finished that part'
'''
printSeqs = open('lncSeqsH', 'w')

for key in dict.keys():
    printSeqs.write(key + ' ' + dict[key] + '\n')
'''



dict3 = open('sortlncH', 'w')
'''

for key in dict:
    print key
'''
entrps = []
dict2 = dict()
count = 0

time1 = time.time()
for key in dict1:
    entrp = ent.shannon_entropy(key)
    entrps.append(entrp)
    try:
        dict2[entrp].append(key)
    except KeyError:
        dict2[entrp] = [key]
    count += 1
    print count
print 'done with first part'
print time.time()-time1
print len(dict1)
entrps.sort(reverse = True)

for entrp in entrps:
    for seq in dict2[entrp]:
        dict3.write('seq: ' + str(seq) + ' occurences: ' + str(dict1[seq]) + ' entropy: ' + str(entrp) + '\n')

