import anydbm

lncH = anydbm.open('lncH', 'c')
lncM = anydbm.open('lncM', 'c')

numLncH = anydbm.open('numLncH', 'n')
numLncM = anydbm.open('numLncM', 'n')
'''
lncEntrpH = anydbm.open('lncEntrpH', 'c')
lncEntrpM = anydbm.open('lncEntrpM', 'c')


lncEntrpFake = anydbm.open('lncEntrpFake', 'c')
lncEntrpFake['3.0'] = 'AGGGttAAAAAGGtccCCcGaaTcA'
lncEntrpFake['3.0'] = str.lower(lncEntrpFake[entrp])
for entrp in lncEntrpFake:
    print lncEntrpFake[entrp]

numItems = 0
numChanged = 0
for entrp in lncEntrpH:
    print entrp
    temp = lncEntrpH[entrp]
    numItems += 1
    lncEntrpH[entrp] = str.lower(lncEntrpH[entrp])
    if lncEntrpH[entrp] != temp:
        numChanged += 1
        print numChanged
        #print lncEntrpH[entrp]
        #print temp
    
    temp2 = lncEntrpM[entrp]
    lncEntrpM[entrp] = lncEntrpM[entrp].lower()
    if lncEntrpM[entrp] != temp:
        #print lncEntrpH[entrp]
        #print temp2

topr = "Changes: " + str(numChanged) + " / " + str(numItems)
print topr
'''
print 'started'
for seq in lncH:
    try:
        numLncH[str.lower(seq)] = str(int(numLncH[str.lower(seq)]) + int(lncH[seq]) + 1)
    except KeyError:
        numLncH[str.lower(seq)] = lncH[seq] + 1

print 'finished human'

print 'started mouse'
for seq in lncM:
    try:
        numLncM[str.lower(seq)] = str(int(numLncM[str.lower(seq)]) + int(lncM[seq]) + 1)
    except KeyError:
        numLncM[str.lower(seq)] = lncM[seq] + 1

print 'finished mouse'