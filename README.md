# StanfordGeneCamp
A collection of all the python scripts I've written while working at Stanford Gene Camp

This code was made with the intention of finding highly conserved sequences in lnc RNA or intronic sequences that
held a high entropy in order to find possible binding site regulators or other important sequences in lnc RNA.

The data that I used to obtain intronic sequences was obtained from UCSC's database, and the lnc RNA from noncode.org

noncodeFind and noncodeSeqs.py are used to find the noncoding regions in the chromosomes and keep them in a file.

I then found 25-mers for each of these intronic sequences or lnc RNA.

My various scripts that begin with sort such as sortEntrp.py are about sorting my files with intronic regions, or 
lnc RNA based upon the entropy of the 25-mer. I used the pyEntrp module in order to perform this sort. 

My sortNarrow.py file cut off any 25-mers that didn't have high enough entropy.

I have scripts such as occurencesConv.py that counted the number of occurrences of my 25-mers, and used this in order
to help sort my 25-mers in order to obtain the most important ones. 
