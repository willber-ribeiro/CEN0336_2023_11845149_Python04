#!/usr/bin/env python3

# 10.1. Write a new script that takes the start and end values from the command line. If you call your script like this count.py 3 10 it will print the numbers from 3 to 10.

import sys

primeiro_valor = int(sys.argv[1])
segundo_valor = int(sys.argv[2])

for numero in range(primeiro_valor, segundo_valor + 1):
    print(numero)
