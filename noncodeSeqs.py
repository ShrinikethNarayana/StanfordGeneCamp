#from collections import defaultdict
import anydbm
from Bio import SeqIO
'''
dict = {}
dict = defaultdict(lambda:0, dict)                                                  
'''
dict = anydbm.open('lncM', 'c')
count = 0
for lnc in SeqIO.parse('NONCODE2016_mouse.fa', 'fasta'):
    lnc = str(lnc.seq)
    subSeq = lnc[:24]
    for num in range(0, len(lnc) - 24):
        subSeq += lnc[num+24]
        if subSeq in dict:
            dict[subSeq] = str(int(dict[subSeq]) + 1)
        else:
            dict[subSeq] = '1'
        #print subSeq
        subSeq = subSeq[1:]

    count += 1
    print str(count)


print 'finished that part'
'''
printSeqs = open('lncSeqsH', 'w')

for key in dict.keys():
    printSeqs.write(key + ' ' + dict[key] + '\n')
'''