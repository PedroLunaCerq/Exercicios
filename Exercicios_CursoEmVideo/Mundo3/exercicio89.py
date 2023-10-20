alunos = []
notas = []
medias = []

while True:
    nome = input('Insira o nome: ')
    alunos.append(nome)
    nota_individual = []
    n1 = int(input('Insira a primeira nota: '))
    nota_individual.append(n1)
    n2 = int(input('Insira a segunda nota: '))
    nota_individual.append(n2)
    operar = input('Deseja continuar? [S/N]').upper()
    if operar == 'N':
        break

for nota in notas:
    media = (nota[1] + nota[2]) / 2
    medias.append(media)