from sets import Set

f = open('sameGenes', 'r')

allGenes = Set()
gene = f.readline()
while gene != '':
    allGenes.add(gene)
    gene = f.readline()

f2 = open('sameGene', 'w')

for gen in allGenes:
    f2.write(gen)