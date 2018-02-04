import anydbm
from pyentrp import entropy as ent
import numpy as np
import time

entrpH = np.load('lncEntropiesH.npy')
entrpM = np.load('lncEntropiesM.npy')

dict2 = anydbm.open('lncEntrpM', 'c')

keys = dict2.keys()
keys.sort(reverse=True)

keys = np.array(keys)

np.save('lncEntropies', keys)


