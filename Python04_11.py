#!/usr/bin/env python3

# 11. Write a new script to create a list with the following data ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']. Use a for loop to iterate through each element of this list and:

# Print out each element.
# Print out the length and the sequence, separated by a tab. The output should look like:
# 14	ATGCCCGGCCCGGC
# 25	GCGTGCTAGCAATACGATAAACCGG
# 12	ATATATATCGAT
# 8	ATGGGCCC

lista = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

for elemento in lista:
    length = len(elemento)
    print(f'{length}\t{elemento}')
