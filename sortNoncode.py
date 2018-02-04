import anydbm
from pyentrp import entropy as ent
import numpy as np
import time

dict1 = anydbm.open('lncH', 'r')

dict3 = open('sortedlncH', 'w')
'''

for key in dict:
    print key
'''
entrps = []
dict2 = dict()
count = 0
#keys = dict1.keys()
time1 = time.time()
for key in dict1:
#time1 = time.time()
#for num in range(0, 22619):
    entrp = ent.shannon_entropy(key)
    entrps.append(entrp)
    try:
        dict2[entrp].append(key)
    except KeyError:
        dict2[entrp] = [key]
    count += 1
    print str(count) + ' ' + str(time.time()-time1)


print 'done with first part'
#print entrps
#print time.time()-time1
entrps.sort(reverse = True)
print 'done with Entropy Sort'

for entrp in entrps:
    for seq in dict2[entrp]:
        dict3.write('seq: ' + str(seq) + ' occurences: ' + str(dict1[seq]) + ' entropy: ' + str(entrp) + '\n')

