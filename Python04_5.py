#!/usr/bin/env python3

# Write a script that uses a while loop to calculate the factorial of 1000.

numero = 1
fatorial = 1

while numero <= 1000:
    fatorial *= numero
    numero += 1

print(fatorial)
