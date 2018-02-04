from pyentrp import entropy as ent
import numpy as np

fread = open('sharedSequences', 'r')
fwrite = open('entrpSorted', 'w')

f3 = open('sameGene', 'r')
geneLine = f3.readline()
genes = list()
while 'chr1' in geneLine:
    genes.append(str.split(geneLine)[0])
    geneLine = f3.readline()
# print('ready to read stuff')
fread.readline()
#print(line)
#print(genes)
'''
counter = 1
while not 'SDCCAG8' in line:
    line = fread.readline()
#print(line + '\n')
line = fread.readline()
print('in position')
'''

for ind in range(0, 367):#len(genes)):
    seqEnt = dict()
    ents = list()
    # print('worked')
    line = fread.readline()
    #print genes[ind + 1] + " " + str(ind)
    if line[:len(line)-1] != '':
        print "new loop: " + line[:len(line)-1]
    if line[:len(line)-1] != '':
        while (ind != 366
               and not genes[ind+1] in line) or (ind == 366 and line != ''):
            #print(str(ind)+'line: ' + line + ' gene: ' + genes[ind+1])

            entropy = ent.shannon_entropy(line)
            seqEnt[entropy] = line
            ents.append(entropy)
            # print(line[:len(line)-9])
            # print(line[:len(line)-9].upper() == 'RFWD2')
            fread.readline()
            fread.readline()
            line = fread.readline()
            print "during loop: " + line + "the next gene: " + genes[ind+1]
            print ind
        ents.sort()
        seqs = list()
        for entr in ents:
            seqs.append(seqEnt[entr])

        fwrite.write("gene: " + genes[ind] + '\n')
        '''   
        for seq in reversed(seqs):
            #print(seq + '\n')
            fwrite.write(seq + " entropy: " + )'''
        for num in range(len(seqs)-1, -1, -1):
            fwrite.write(seqs[num] + "entropy: " + str(ents[num]) + '\n',)
    else:
        fread.readline()
        fread.readline()
        line = fread.readline()