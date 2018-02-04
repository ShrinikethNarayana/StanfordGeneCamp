from Bio import SeqIO
from Bio.Seq import Seq

f = open('testGeneData', 'r')
f.readline()

f2 = open('testExonOutput', 'w')

chr1 = SeqIO.parse("chr1human.fa", "fasta")
chr1 = next(chr1)

line = f.readline()
print(line, '\n')
while 'chr1' in line:

    lines = str.split(line)
    numExons = int(lines[8])
  #  print(numExons)
    for num in range(0,numExons):
        #print(lines[9])
        #print(str(lines[9])[0:str.find(lines[9], ',')])
        #print(num)
        #print(str.find(lines[9], ','))
      #  print('Line 9: ' + lines[9])
      #  print('Line 10: ' + lines[10])
        f2.write(str(chr1.seq)[int(lines[9][:str.index(lines[9], ',')]):int(lines[10][:str.index(lines[10], ',')])] + '\n\n')

        lines[9] = lines[9][str.find(lines[9], ',') + 1:]
        lines[10] = lines[10][str.find(lines[10], ',') + 1:]
    f2.write('\n\n\n\nNext Gene\n\n\n\n')
    #print(line)
    line = f.readline()

f.close()
f2.close()