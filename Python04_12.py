#!/usr/bin/env python3

# 12. Use list comprehension to generate a list of tuples. The tuples should contain sequences and lengths from the previous problem. Print out the length and the sequence (i.e., "4\tATGC\n"). A list of tuples looks like this [(4,'ATGC'),(2,'GC')].

lista = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

lista_de_tuplas = [(len(elemento), elemento) for elemento in lista]
for item in lista_de_tuplas:
    print(item[0], "\t", item[1])
