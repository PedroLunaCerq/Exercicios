#Variáveis.
operar = 'S'
pessoas = []
pessoa = {}

#Cadastrar pessoas.
while operar != 'N':
    pessoa['nome'] = input('Insira o nome: ')
    pessoa['genero'] = input('Insira o gênero [M/F]: ')
    pessoa['idade'] = int(input('Insira a idade: '))
    pessoas.append(pessoa.copy())
    pessoa = {}
    operar = input('Deseja continuar? [S/N] ').upper

#Total de pessoas
total = 0
for pessoa in pessoas:
    total += 1

#Idade média das pessoas.
idade_total = 0
for c, pessoa in enumerate(pessoas):
    idade_total += pessoa['idade']
media = idade_total / c

#Uma lista com todas as mulheres e pessoas com idade acima da média.
lista_fem = []
lista_idade = []
for pessoa in pessoas:
    if pessoa['genero'] == 'F':
        lista_fem.append(pessoa['nome'])
    if pessoa['idade'] > media:
        lista_idade.append(pessoa['nome'])