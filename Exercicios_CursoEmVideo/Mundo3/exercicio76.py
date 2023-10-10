#crie uma tupla única com uma lista de produtos e seus respectivos preços, na sequência. No final,
#mostre os preços acompanhado de seus produtos, em forma tabular.


produtos = []
preços = []
tupla = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90)
produtos.append(tupla[0:len(tupla):2])
preços.append(tupla[1:len(tupla):2])

print('=' * 15)
for produto in produtos:
    print(produto)
print('=' * 15)