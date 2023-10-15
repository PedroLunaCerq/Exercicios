
produtos = []
preços = 0
maior = 0
while True:
    produto = input('Informe um produto: ')
    produtos.append(produto)
    preço = int(input('Agora o seu preço: '))
    produtos.append(preço)
    preços += preço

    if preço > 1.000:
        maior += 1

    operar = input('Deseja continuar? [S/N]').upper()
    if operar == 'N':
        break

print(f'O total gasto na compra foi {preços}!')
print(f'O total de produtos que custam mais de R$1.000 é {maior}')