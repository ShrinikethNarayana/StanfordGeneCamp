'''
Compares intronic sequences of a certain length in the mouse and human chromosome 1 in order to
find conserved regions. This program doesn't only compare intronic sequences from specific genes
together, but the entire chromosome 1 against the other.
'''

from collections import defaultdict
import anydbm
import time
#from set import Set
f3 = open('sameGene', 'r')
geneLine = f3.readline()
genes = list()
while 'chr1' in geneLine:
    genes.append(str.split(geneLine)[0])
    geneLine = f3.readline()

printTo = open('sharedSeq', 'w')

'''
#dictM = anydbm.open('dictM', 'n')
dictM = {}
dictM = defaultdict(lambda:0, dictM)

#dictH = anydbm.open('dictH', 'n')
dictH = {}
dictH = defaultdict(lambda:0, dictH)
dictH2 = {}
dictH2 = defaultdict(lambda:0, dictH)
dbmH = anydbm.open('dbmHmine', 'n')
dbmM = anydbm.open('dbmMmine', 'n')
'''
dictM = set()
dictH = set()
#try to split up into two different loops so I can divide the amount of space the dict will take up
count = 0
for gene in genes:
    count += 1
    print count

    f1 = open("intronic" + gene + "Human", "r")

    geneH = f1.readline()

    start = time.time()
    while not (geneH == ''):
        for num in range(0, len(geneH)-99):
            #print(num)
            #print(geneH[num:num+100])
            dictH.add(geneH[num:num+100])
        geneH = f1.readline()
    print time.time()-start
    #finish doing all genes for human then move to mouse. Need to fix. Will improve speed.
'''
print("moving human to dbm")
for key in dictH.keys():
    if key in dbmH:
        dbmH[key] = str(int(dbmH[key])+dictH[key])
    else:
        dbmH[key] = str(dictH[key])
dictH = None
'''
count = 0
for gene in genes:
    count += 1
    print count
    geneM = f2.readline()

    f2 = open("intronic" + gene + "Mouse", "r")

    while not (geneM == ''):
        for num in range(0, len(geneM)-99):
            dictM.add(geneM[num:num + 100])
        geneM = f2.readline()
'''
print("moving mouse to dbm")
for key in dictM.keys():
    if key in dbmM:
        dbmM[key] = str(int(dbmM[key])+dictM[key])
    else:
        dbmM[key] = str(dictM[key])
dictM = None
'''
keysH = list(dictH)
#keysM = dictM.keys()
#print(keysH)
#print(keysM)
print 'about to compare'
#printTo.write(gene + '\n')
#hasIt = False
for key in keysH:
    if key in dictM:
        #hasIt = True
        printTo.write(key + '\n')
        printTo.write("Human instances: " + str(dbmH[key]) + '\nMouse instances: ' + str(dbmM[key]) + '\n')
# if not hasIt:
    # printTo.write('\n\n\n')
