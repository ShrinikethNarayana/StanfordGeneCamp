import anydbm

lncH = anydbm.open('lncH', 'r')

for seq in lncH:
    print seq + ' ' + str(lncH[seq])