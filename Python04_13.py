#!/usr/bin/env python3

# 13. Modify the script from #11 so that you also print out the number (postion in the list) of each sequence (i.e., "1\t4\tACGT\n")

lista = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
posicao = 1

for elemento in lista:
    length = len(elemento)
    print(f'{posicao}\t{length}\t{elemento}')
    posicao += 1
