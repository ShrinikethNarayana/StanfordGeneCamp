from Bio import SeqIO
from Bio.Seq import Seq


f = open('geneDataHuman', 'r')
f.readline()


f3 = open('sameGenes', 'r')
geneLine = f3.readline()
genes = list()
while 'chr1' in geneLine:
    genes.append(str.split(geneLine)[0])
    geneLine = f3.readline()

chr1 = SeqIO.parse("chr1human.fa", "fasta")
chr1 = next(chr1)
#print(str(chr1.seq)[175914307:175916330])
line = f.readline()
#print(line, '\n')
while 'chr1' in line:
    lines = str.split(line)
    #print()
    if str.upper(lines[12]) in genes:
        numExons = int(lines[8])
        #print(numExons)
        lines[9] = lines[9][str.find(lines[9], ',') + 1:]
        f2 = open('intronic' + lines[12][0].upper() + lines[12][1:].lower() + 'Human', 'a')
        for num in range(0,numExons-1):
            #print(lines[9])
            #print(str(lines[9])[0:str.find(lines[9], ',')])
            #print(num)
            #print(str.find(lines[9], ','))
            #print('Line 9: ' + lines[9])
            #print('Line 10: ' + lines[10])
            #print(lines[10][:str.index(lines[10], ',')])
            #print(lines[10][:str.index(lines[9], ',')])
            f2.write(str(chr1.seq)[int(lines[10][:str.index(lines[10], ',')])+1:int(lines[9][:str.index(lines[9], ',')])])

            lines[9] = lines[9][str.find(lines[9], ',')+1:]
            lines[10] = lines[10][str.find(lines[10], ',') + 1:]
        f2.write('\n')
        #print(line)
    line = f.readline()

f.close()
f2.close()