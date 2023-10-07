import random
aluno1 = str(input('Insira o nome do primeiro aluno:'))
aluno2 = str(input('Insira o nome do segundo aluno:'))
aluno3 = str(input('Insira o nome do terceiro aluno:'))
aluno4 = str(input('Insira o nome do quarto aluno:'))
sorteio = [aluno1, aluno2, aluno3, aluno4]
aluno_sorteado = random.choice(sorteio)
print('Entre os alunos(as) {}, o(a) escolhido(a) para apagar o quadro foi... {}!'.format(sorteio, aluno_sorteado))