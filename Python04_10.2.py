#!/usr/bin/env python3

# 10.2. Modify your script so that it will only print the number if it is odd.

import sys

primeiro_valor = int(sys.argv[1])
segundo_valor = int(sys.argv[2])

for numero in range(primeiro_valor, segundo_valor+1):
    if numero % 2 != 0:
        print(numero)
