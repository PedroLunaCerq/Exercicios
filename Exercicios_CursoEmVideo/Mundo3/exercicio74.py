import random

numeros = []
for c in range(0, 5):
    n = random.randrange(1, 100)
    numeros.append(n)
numeros_org = numeros.sort()
numeros = tuple(numeros)
print(f'Os números gerados foram {numeros}. O menor valor foi {numeros[0]}, e o maior {numeros[4]}')