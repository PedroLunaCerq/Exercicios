tupla = ('Botafogo', 'Bragantino', 'Grêmio', 'Palmeiras', 'Flamengo', 'Fluminense', 'Atlético - MG', 'Athlético - PR', 
'Fortaleza', 'São Paulo', 'Cuiabá', 'Cruzeiro', 'Corinthians', 'Internacional', 'Santos', 'Goiás', 'Vasco da Gama', 
'Bahia', 'América - MG', 'Coritiba')

print('=' * 15)
print(f'Os cinco primeiros times colocados no brasileirão foram:')
for c in range(0, 5):
    print(f'{tupla[c]}, em {c + 1} lugar.')

print('_' * 10)

print(f'Os últimos quatro foram:')
print(f"""{tupla[-1]}, em 17° lugar.
{tupla[-2]}, em 18° lugar.
{tupla[-3]}, em 19° lugar.
{tupla[-4]}, em 20° lugar.""")

print('_' * 10)

lista = list(tupla)
lista_alfabetica = sorted(lista)
print('Em ordem alfabética, os times são:')
for time in lista_alfabetica:
    print(time)

print('_' * 10)