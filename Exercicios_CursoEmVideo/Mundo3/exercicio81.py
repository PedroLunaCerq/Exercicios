lista = []

print('[00] para parar.')
while True:
    n = int(input('Insira um número: '))
    if n == 00:
        break
    else:
        lista.append(n)
    



print(f'1 - Foram inseridos {len(lista)} números na lista.')
lista.sort(reverse=True)
print(f'2 - Em ordem decrescente, a lista é: {lista})')
if 5 not in lista:
    print('O número 5 não foi inserido!')
else:
    print('O número 5 está na lista!')