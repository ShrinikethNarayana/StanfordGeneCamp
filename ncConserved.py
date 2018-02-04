import anydbm
import numpy as np

dictH1 = anydbm.open('lncH', 'c')

dictH2 = anydbm.open('lncEntrpH', 'c')

dictM1 = anydbm.open('lncM', 'c')

dictM2 = anydbm.open('lncEntrpM', 'c')

entrps = np.load('entrps')


