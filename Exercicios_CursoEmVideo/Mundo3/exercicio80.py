lista = []

n1 = int(input('Insira um valor: '))
lista.append(n1)

n2 = int(input('Insira um segundo valor: '))
if n2 >= n1:
    lista.append(n2)
else:
    lista.insert(0, n2)


n3 = int(input('Insira um terceiro valor: '))
if n3 > n2:
    lista.insert(lista.index(n2) + 2, n3)
elif n3 == n2:
    lista.insert(lista.index(n2) + 1, n3)
else:
    lista.insert(lista.index(n2) - 1, n3)


n4 = int(input('Insira um quarto valor: '))
if n4 > n3:
    lista.insert(lista.index(n3) + 2, n4)
elif n4 == n3:
    lista.insert(lista.index(n3) + 1, n4)
else:
    lista.insert(lista.index(n1) - 1, n4)

n5 = int(input('Insira um último valor: '))
if n5 > n4:
    lista.insert(lista.index(n4) + 2, n5)
elif n4 == n3:
    lista.insert(lista.index(n4) + 1, n5)
else:
    lista.insert(lista.index(n1) - 1, n5)

print('=' * 15)
print(lista)
print('=' * 15)