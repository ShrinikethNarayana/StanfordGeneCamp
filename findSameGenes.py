from Bio import SeqIO
from Bio.Seq import Seq

f = open('geneDataHuman', 'r')
f.readline()

f2 = open('geneDataMouse', 'r')
# f2 = open('testGeneData', 'r')
f2.readline()

f4 = open('geneDataCow', 'r')
f4.readline()

f5 = open('geneDataPig', 'r')
f5.readline()

f3 = open('sameGenes', 'w')

line = f.readline()
line2 = f2.readline()
line4 = f4.readline()
line5 = f5.readline()

names1 = list()
names2 = list()
names4 = list()
names5 = list()

names1.append(str.split(line)[12] + ' in ' + str.split(line)[2])
line = f.readline()
while 'chr' in line:
    lines = str.split(line)
    #lines[12]
    if names1[len(names1) - 1] != (lines[12] + " in " + lines[2]):
        names1.append(lines[12] + " in " + lines[2])
        # print("working")
    # f3.write(lines[1] + '\n')
    line = f.readline()

f3.write('\n')

names2.append(str.split(line2)[12] + ' in ' + str.split(line2)[2])
line2 = f2.readline()
while 'chr' in line2:
    lines2 = str.split(line2)
    if names2[len(names2) - 1] != (lines2[12] + " in " + lines2[2]):
        names2.append(lines2[12] + " in " + lines2[2])
        # print("working")
    # f3.write(lines2[1] + '\n')
    line2 = f2.readline()
#------------------------------------------------
names4.append(str.split(line4)[12] + ' in ' + str.split(line4)[2])
line4 = f4.readline()
while 'chr' in line4:
    lines4 = str.split(line4)
    if names4[len(names4) - 1] != (lines4[12] + " in " + lines4[2]):
        names4.append(lines4[12] + " in " + lines4[2])
        # print("working")
    # f3.write(lines2[1] + '\n')
    line4 = f4.readline()

names5.append(str.split(line5)[12] + ' in ' + str.split(line5)[2])
line5 = f5.readline()
while 'chr' in line5:
    lines5 = str.split(line5)
    if names5[len(names5) - 1] != (lines5[12] + " in " + lines5[2]):
        names5.append(lines5[12] + " in " + lines5[2])
        # print("working")
    # f3.write(lines2[1] + '\n')
    line5 = f5.readline()
newList1 = list()
for name1 in names1:
    for name2 in names2:

        #print("Name1: " + name1)
        #print("Name2: " + name2)
        if str.lower(name1) == str.lower(name2):
            newList1.append(name1)
#print newList1
newList2 = list()
#print names4
#print names5
for name4 in names4:90
    for name5 in names5:
        if str.lower(name4)[:len(name4)-3] == str.lower(name5)[:len(name4)-3]:
            newList2.append(name4)
#print newList2
for name10 in newList1:
    for name20 in newList2:
        if str.lower(name10)[:len(name10)-3] == str.lower(name20)[:len(name20)-3]:
            f3.write(name10 + '\n')
f.close()
f2.close()
f3.close()
