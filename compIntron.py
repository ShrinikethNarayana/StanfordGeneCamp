"""
Compares intronic sequences of a certain length in the mouse and human chromosome 1 in order to
find conserved regions. This program doesn't only compare intronic sequences from specific genes
together, but the entire chromosome 1 against the other.
"""

import anydbm

f3 = open('sameGene', 'r')

geneLine = f3.readline()
genes = list()
while 'chr1' in geneLine:
    genes.append(str.split(geneLine)[0])
    geneLine = f3.readline()

printTo = open('sharedSeq', 'w')

dbmH = anydbm.open('dbmH', 'n')
dbmM = anydbm.open('dbmM', 'n')

#try to split up into two different loops so I can divide the amount of space the dict will take up


for gene in genes:

    f1 = open("intronic" + gene + "Human", "r")
    f2 = open("intronic" + gene + "Mouse", "r")

    geneH = f1.readline()
    geneM = f2.readline()

    while not (geneH == ''):
        hundredSeq = geneH[0:99]
        for num in range(0, len(geneH)-99):
            hundredSeq += geneH[num+99]
            if not geneH[num:num+100] in dbmH:
                dbmH[hundredSeq] = 1
            else:
                dbmH[hundredSeq] = dbmH[hundredSeq] + 1
            hundredSeq = hundredSeq[1:]
        geneH = f1.readline()

    while not (geneM == ''):
        for num in range(0, len(geneM)-99):
            if not geneH[num:num+100] in dbmH:
                dbmM[geneM[num:num+100]] = '1'
            else:
                dbmM[geneM[num:num+100]] = str(int(dbmM[geneM[num:num+100]]) + 1)
        geneM = f2.readline()

keysH = dbmH.keys()


for key in keysH:
    if dbmM.has_key(key):
        printTo.write(key + '\n')
        printTo.write("Human instances: " + str(dictH[key]) + '\nMouse instances: ' + str(dictM[key]) + '\n')
