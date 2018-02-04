from Bio import SeqIO
'''
count1 = 0
count2 = 0
for lnc in SeqIO.parse('NONCODE2016_human.fa', 'fasta'):
    count1 += 1

    count2 += len(lnc)

print 'transcripts: ' + str(count1)
print 'bases: ' + str(count2)
'''

f = open('geneDataHuman', 'r')
f.readline()

line = f.readline()
count3 = 0
while 'chr' in line:

    lines = str.split(line)
    numExons = int(lines[8])
    lines[9] = lines[9][str.find(lines[9], ',') + 1:]
  #  print(numExons)
    for num in range(0,numExons-1):
        #count3 += (int(lines[10][:str.index(lines[10], ',')]) - int(lines[9][:str.index(lines[9], ',')])+1)
        count3 += int(lines[9][:str.index(lines[9], ',')]) + 1 - (int(lines[10][:str.index(lines[10], ',')]))
        lines[9] = lines[9][str.find(lines[9], ',')+1:]
        lines[10] = lines[10][str.find(lines[10], ',') + 1:]
    line = f.readline()
print count3

f = open('geneDataHuman', 'r')
f.readline()

line = f.readline()
count4 = 0
while 'chr' in line:

    lines = str.split(line)
    numExons = int(lines[8])
    #lines[9] = lines[9][str.find(lines[9], ',') + 1:]
  #  print(numExons)
    for num in range(0,numExons):
        count4 += (int(lines[10][:str.index(lines[10], ',')]) - int(lines[9][:str.index(lines[9], ',')])+1)
        #count3 += int(lines[9][:str.index(lines[9], ',')]) + 1 - (int(lines[10][:str.index(lines[10], ',')]))
        lines[9] = lines[9][str.find(lines[9], ',')+1:]
        lines[10] = lines[10][str.find(lines[10], ',') + 1:]
    line = f.readline()
print count4
'''
int(lines[10][:str.index(lines[10], ',')])
int(lines[9][:str.index(lines[9], ',')]))
'''