import anydbm
from pyentrp import entropy as ent
import numpy as np


dict1 = anydbm.open('lncH', 'r')

dict3 = open('sortedNotlncH', 'w')
'''

for key in dict:
    print key
'''
entrps = []
dict2 = anydbm.open('lncEntrpH', 'n')
count = 0
for key in dict1:
    entrp = ent.shannon_entropy(key)
    entrps.append(str(entrp))
    try:
        dict2[str(entrp)] += ' ' + key
    except KeyError:
        dict2[str(entrp)] = key
    count += 1
    print count
print 'done with first part'
#print entrps
entrps.sort(reverse = True)

for entrpn in entrps:
    for seq in str.split(dict2[str(entrpn)]):
        dict3.write('seq: ' + str(seq) + ' occurences: ' + str(dict1[seq]+1) + ' entropy: ' + str(entrpn) + '\n')