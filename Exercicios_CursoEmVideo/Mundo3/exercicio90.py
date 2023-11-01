alunos = []
aluno = {}
a = '-'

while True:
    aluno['nome'] = input('Insira o nome do estudante: ').title()
    aluno['media'] = int(input('Insira a média do mesmo: '))
    if aluno['media'] < 6:
        aluno['situacao'] = 'Reprovado.'
    else:
        aluno['situacao'] = 'Aprovado.'
    alunos.append(aluno.copy())
    operar = input('Deseja continuar? [S/N] ').upper()
    if operar == 'N':
        break

print(f'{a}' * 15)
for aluno in alunos:
    print(f"Estudante: {aluno['nome']}, Situação: {aluno['situacao']}")
print(f"""{a * 15}
<< Programa encerrado! >>
""")