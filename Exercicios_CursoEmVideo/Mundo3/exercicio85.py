numeros = []
pares = []
impares = []

for c in range(0,7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

pares.sort()
impares.sort()

numeros.append(pares)
numeros.append(impares)

print(f'Os valores pares digitados foram {numeros[0]}, e os pares foram {numeros[1]}')