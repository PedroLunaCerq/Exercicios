preço = float(input('Insira o preço do produto:'))
desconto = int(input('Insira a porcentagem do desconto'))
valor_descontado = (desconto / 100) * preço
valor_final = preço - valor_descontado
print('O valor de desconto de tal produto é igual à', valor_final)