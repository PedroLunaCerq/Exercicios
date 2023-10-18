matriz1 = []
matriz2 = []
matriz3 = []
matriz_total = []

for i in range(0, 3):
    n = int(input('Insira um valor para a primeira coluna da matriz: '))
    matriz1.append(n)
for i in range(0, 3):
    n = int(input('Insira um valor para a segunda coluna da matriz: '))
    matriz2.append(n)
for i in range(0, 3):
    n = int(input('Insira um valor para a terceira coluna da matriz: '))
    matriz3.append(n)

matriz_total.append(matriz1)
matriz_total.append(matriz2)
matriz_total.append(matriz3)

print('=' * 15)
for c in matriz_total:
    print(c)
print('=' * 15)