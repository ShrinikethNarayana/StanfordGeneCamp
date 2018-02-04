'''
This is supposed to be a less informative version of compareIntronic.py. I'm hoping to find a problem with my ability
to find conserved sequences.
'''
from collections import defaultdict
from sets import Set

f3 = open('sameGenes', 'r')
geneLine = f3.readline()
genes = list()
while 'chr1' in geneLine:
    genes.append(str.split(geneLine)[0])
    geneLine = f3.readline()

printTo = open('sharedSequences2', 'w')

for gene in genes:

    f1 = open("intronic" + gene + "Human", "r")
    f2 = open("intronic" + gene + "Mouse", "r")

    geneH = f1.readline()
    geneM = f2.readline()

    dictM = Set()

    dictH = Set()

    while not (geneH == ''):
        for num in range(0, len(geneH)-24):
            #print(num)
            #print(geneH[num:num+100])
            dictH.add(geneH[num:num+25])
        geneH = f1.readline()

    while not (geneM == ''):
        for num in range(0, len(geneM)-24):
            dictM.add(geneM[num:num+25])
        geneM = f2.readline()

    #print(keysH)
    #print(keysM)
    printTo.write(gene + '\n')
    hasIt = False
    for key in dictH:
        if(key in dictM):
            hasIt = True
            printTo.write(key + '\n')
            #printTo.write("Human instances: " + str(dictH[key]) + '\nMouse instances: ' + str(dictM[key]) + '\n')
    if not hasIt:
        printTo.write('\n\n\n')