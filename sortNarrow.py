import anydbm
from pyentrp import entropy as ent
import numpy as np
import time

dict1 = anydbm.open('lncH', 'r')

#dict3 = open('sortedlncH', 'w')
'''

for key in dict:
    print key
'''
entrps = []
dict2 = anydbm.open('lncEntrpH', 'n')
count = 0
#keys = dict1.keys()
time1 = time.time()
for key in dict1:
#time1 = time.time()
#for num in range(0, 22619):
    if int(dict1[key]) >= 4:
        entrp = ent.shannon_entropy(key.lower())
        if entrp >= 1.7:
            entrps.append(entrp)
            try:
                dict2[str(entrp)] += ' '+ str(key)
            except KeyError:
                dict2[str(entrp)] = key
    count += 1
    print str(count) + ' ' + str(time.time()-time1)


print 'done with first part'
#print entrps
#print time.time()-time1
entrps.sort(reverse = True)

entrps = np.array(entrps)
np.save('lncEntropiesH', entrps)
print 'done with Entropy Sort'
'''
for entrp in entrps:
    for seq in dict2[entrp]:
        dict3.write(str(seq) + ' ' + str(dict1[seq]) + ' ' + str(entrp) + '\n')

'''