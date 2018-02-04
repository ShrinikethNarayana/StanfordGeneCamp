from Bio import SeqIO
from Bio.Seq import Seq


f = open('geneDataHuman', 'r')
f.readline()


f3 = open('sameGene', 'r')
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
f2 = open('intronHuman', 'w')


for gene in genes:
    f3 = open('intronic' + gene[:len(gene)-1].upper() + gene[len(gene)-1].lower() + 'Human', 'r')
    f2.write('gene: ' + gene + '\n')
    fline = f3.readline()
    while fline != '':
        f2.write(fline)
        fline = f3.readline()

f.close()
f2.close()