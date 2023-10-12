#!/usr/bin/env python3

# 7. Sort the elements of the above list, then iterate through each element using a for loop and:
lista = [101,2,15,22,95,33,2,27,72,15,52]
lista.sort()

#Print each element
#Calculate two cumulative sums, one of all the even values and one of all the odd values.
#Print only the final two sums. The output from your script should be:
#Sum of even numbers: 150 
#Sum of odds: 286

soma_pares = 0
soma_impares = 0

for elemento in lista:
    if elemento % 2 == 0:
        soma_pares += elemento
    else:
        soma_impares += elemento

print(soma_pares)
print(soma_impares)
