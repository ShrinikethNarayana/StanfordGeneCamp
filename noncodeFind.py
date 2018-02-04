from Bio import SeqIO
noncoding = SeqIO.parse('NONCODE2016_human.fa', 'fasta')
#noncode = next(noncode)
genomes = SeqIO.parse('bosTau8.fa', 'fasta')
#genome = next(genome)
write = open('conservedLNC', 'w')

lncSub = list()

'''
def subLen25 (string):
    lncSub = list()
    sub = string[:24]
    for num in range(0, len(string)-24):
        sub += string[num+24]
        lncSub.append(sub)
        sub = sub[1:]
'''


#loops each lncRNA
for noncode in noncoding:
    noncode = noncode.seq
    #write.write(noncode.id + '\n')
    #subLen100(noncode)

    for genome in genomes:
        genome = genome.seq
        gen = noncode[:24]
        #print len(genome)
        num2 = 0
        #length = len(genome) - len(noncode) + 1
        length = len(noncode)-24
        while num2 < length:
            gen = gen + noncode[num2+24]
            #print gen + '\n'
            #for lnc in lncSub:
                #lnc = lnc.seq
            print "before comparison"
            if gen in genome:v
                write.write(lnc + ' ' + num + '\n')
                print "found match"
            print "after comparison"
            #print gen
            gen = gen[1:]
           # print gen
            num2 += 1
    print 'round done,\n'