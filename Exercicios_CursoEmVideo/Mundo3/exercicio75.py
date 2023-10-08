
n_9 = 0
numeros = []
pares = []
for c in range(0, 4):
    n = int(input('Insira um valor: '))
    numeros.append(n)
    if n == 9:
        n_9 += 1
    if n % 2 == 0:
        pares.append(n)
pos_3 = numeros.index(3) + 1
tupla = tuple(numeros)
print(f'''Os números inseridos foram {tupla}
O número 9 apareceu {n_9} vezes.
A primeira posição do 3 é {pos_3}
Os números pares foram {pares}''')