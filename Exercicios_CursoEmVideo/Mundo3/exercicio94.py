galera = []
pessoa = {}
soma = media = 0

print('-' * 15)
while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['genero'] = input('Insira o gênero: [M/F] ').upper()[0]
        if pessoa['genero'] in 'MF':
            break
        print('Erro! Por favor, [M/F]!')    
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = input('Quer continuar? [S/N] ').upper()[0]
        if resp in 'SN':
            break
        print('Erro! Por favor, [S/N]')
    if resp == 'N':
        break

media = soma / len(galera)
print('-' * 15)
print(f'A) O total de pessoas cadastradas é {len(galera)}!')
print(f'B) A média de idade das pessoas cadastradas é {media:5.2f}!')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['genero'] in 'Ff':
        print(f"{p['nome']}, ", end='')
print('D) Lista das pessoas de idade acima da média: ', end='')
print()
for p in galera:
    if p['idade'] >= media:
        print(f"{p['nome']},", end='')
print()
print('=' * 15)
print('<<Encerrado!>>')