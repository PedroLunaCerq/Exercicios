matriz1 = []
matriz2 = []
matriz3 = []
matriz_total = []
soma = 0
soma_terceira = 0
maior_valor = 0

for i in range(0, 3):
    n = int(input('Insira um valor para a primeira coluna da matriz: '))
    matriz1.append(n)
    if n % 2 == 0:
        soma += n
for i in range(0, 3):
    n = int(input('Insira um valor para a segunda coluna da matriz: '))
    matriz2.append(n)
    if n % 2 == 0:
        soma += n
    if n >= maior_valor:
        maior_valor = n
for i in range(0, 3):
    n = int(input('Insira um valor para a terceira coluna da matriz: '))
    matriz3.append(n)
    if n % 2 == 0:
        soma += n
    soma_terceira += n

matriz_total.append(matriz1)
matriz_total.append(matriz2)
matriz_total.append(matriz3)

print('=' * 15)
for c in matriz_total:
    print(c)
print('-' * 10)
print(f'A soma de todos os valores pares é {soma}.')
print(f'A soma dos valores da terceira coluna é {soma_terceira}.')
print(f'O maior valor da segunda linha é {maior_valor}.')
print('=' * 15)