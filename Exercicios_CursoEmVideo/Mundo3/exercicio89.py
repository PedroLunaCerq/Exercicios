ficha = []

while True:
    nome = input('Insira o nome: ')
    n1 = float(input('Insira a primeira nota: '))
    n2 = float(input('Insira a segunda nota: '))
    media = (n1 + 2) / 2
    ficha.append([nome, n1, n2, media])
    resp = input('Quer continuar? [S/N] ').upper()
    if resp == 'N':
        break
print('=-' * 20)
print(f'{"No.":4<}{"Nome":<10}{"Média":>8}')
print('-' * 18)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 Interrompe).  '))
    if opc == 999:
        print('Finalizando...')
        break
if opc <= len(ficha) - 1:
    print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< Volte Sempre! >>>')