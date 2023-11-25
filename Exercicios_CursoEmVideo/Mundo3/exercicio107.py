import moeda

operar = input('O que deseja fazer? [AUMENTAR/DIMINUIR/DOBRAR/DIVIDIR] ').upper()

if operar == 'AUMENTAR':
    n = input('Insira um valor: ')
    a = moeda.aumentar(n)
    print(f'Um número maior que {n} é {a}.')

if operar == 'DIMINUIR':
    n = int(input('Insira um valor: '))
    a = moeda.diminuir(n)
    print(f'Um número menor que {n} é {a}.')

if operar == 'DOBRAR':
    n = int(input('Insira um valor: '))
    a = moeda.dobro(n)
    print(f'O dobro de {n} é {a}')

if operar == 'DIVIDIR':
    n = int(input('Insira um valor: '))
    a = moeda.metade(n)
    print(f'A metade de {n} é {a}')