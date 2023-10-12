#!/usr/bin/env python3

# 6. Iterate through each element of this list using a for loop: [101,2,15,22,95,33,2,27,72,15,52]
#Print out only the values that are even (hint: use the modulus operator).

lista = [101,2,15,22,95,33,2,27,72,15,52]

for elemento in lista:
    if elemento % 2 == 0:
        print(elemento)
