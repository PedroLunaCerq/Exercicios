#Crie um programa com uma tupla com várias palavras. Depois disso, deve mostrar para cada palavra, as suas vogais.

tupla = ('Monitor', 'Mouse', 'Celular', 'Computador', 'Controle')
for item in tupla:
    print(f'\nNa palavra {item} temos as vogais ', end = '')
    for letra in item: 
        if letra.upper() in 'AEIOU':
            print(letra.upper(), end = '')