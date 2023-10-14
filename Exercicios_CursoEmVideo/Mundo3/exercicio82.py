lista = []
lista_par = []
lista_impar = []

print('[0] para parar!')
while True:
    n = int(input('Insira um número: '))
    if n == 0:
        break
    lista.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)

print(f'''A lista completa é {lista}
a lista de números pares é {lista_par}
e a lista de números ímpares é {lista_impar}''')