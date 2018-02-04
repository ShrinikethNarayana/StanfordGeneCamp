'''
Compares the intronic sequences of every gene separately in the human and mouse genome.
Every gene is tested against itself and not other intronic regions of other regions.
'''
from collections import defaultdict


f3 = open('sameGene', 'r')
geneLine = f3.readline()
genes = list()
while 'chr1' in geneLine:
    genes.append(str.split(geneLine)[0])
    geneLine = f3.readline()

printTo = open('sharedSequences', 'w')

for gene in genes:

    f1 = open("intronic" + gene + "Human", "r")
    f2 = open("intronic" + gene + "Mouse", "r")

    geneH = f1.readline()
    geneM = f2.readline()

    dictM = {}
    dictM = defaultdict(lambda:0, dictM)

    dictH = {}
    dictH = defaultdict(lambda:0, dictH)

    while not (geneH == ''):
        for num in range(0, len(geneH)-99):
            #print(num)
            #print(geneH[num:num+100])
            dictH[geneH[num:num+100]] += 1
        geneH = f1.readline()
    print(len(dictH))
    while not (geneM == ''):
        for num in range(0, len(geneM)-99):
            dictM[geneM[num:num+100]] += 1
        geneM = f2.readline()

    keysH = dictH.keys()
    keysM = dictM.keys()
    #print(keysH)
    #print(keysM)

    printTo.write(gene + '\n')
    hasIt = False
    for key in keysH:
        if dictM.has_key(key):
            hasIt = True
            printTo.write(key + '\n')
            printTo.write("Human instances: " + str(dictH[key]) + '\nMouse instances: ' + str(dictM[key]) + '\n')
    if not hasIt:
        printTo.write('\n\n\n')