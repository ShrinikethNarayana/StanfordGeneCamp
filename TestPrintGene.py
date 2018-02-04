'''
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Alphabet.IUPAC import unambiguous_dna
from Bio.Alphabet import generic_dna

my_seq = Seq('GATTACA', 'IUPAC.unambiguous_dna')

for seq_record in my_seq:
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))
'''
#theSeq = Seq(str(SeqIO.parse("chr1.fa", "fasta")), "IUPAC.unambiguous_dna")
#for seq_record in SeqIO.parse("chr1.fa", "fasta"):
#   print(repr(seq_record.seq))
from Bio import SeqIO
from Bio.Seq import Seq

#name = SeqIO.parse("my_orchid.fa", "fasta")
#print(repr(next(name).seq))

count = 1;
for seqrec in SeqIO.parse("chr1.fa", "fasta"):
#print(repr(next(name).id))
#print(len(name[0]))
    if count < 5:
         # print(dir(seqrec))
          str1 = seqrec.__str__()
          print(str1)
          print(str(seqrec.seq))
          count+=1
#print(repr(name.seq))