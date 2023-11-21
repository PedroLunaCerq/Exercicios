def notas(*notas, sit=False):
    """Esta função recebe notas de uma turma. Calcula sua média  e exibe sua situação."""

    notas1 = []
    for n in notas:
        nota = int((n))
        notas1.append(nota)

    #Quantidade de notas.
    quant_notas = len(notas1)

    #A maior e menor nota.
    notas1.sort()
    maior_nota = notas1[-1]
    menor_nota = notas1[0]

    #A média da turma.
    dividendo = 0
    for n in notas1:
        dividendo += n
    divisor = 0
    for n in range(len(notas1)):
        divisor += 1
    media = dividendo / divisor

    #A situação da turma.
    if media == 10:
        situacao = 'Perfeita.'
    elif media >= 6:
        situacao = 'Boa.'
    elif media < 6:
        situacao = 'Péssima.'

    #O dicionário para retornar.
    dicionario = dict()
    dicionario['quantidade'] = quant_notas
    dicionario['maior_nota'] = maior_nota
    dicionario['menor_nota'] = menor_nota
    dicionario['media'] = media
    if sit == True:
        dicionario['situacao'] = situacao
    
    #Prints.
    print(f"""
a) A quantidade de notas inseridas foi {dicionario['quantidade']}.
b) A maior nota foi {dicionario['maior_nota']}. E a menor foi {dicionario['menor_nota']}.
c) A média da turma, ao todo, é {dicionario['media']}""")
    if sit == True:
        print(f"c) A situação da turma é: {dicionario['situacao']}")

notas(4, 5, 8, 7)