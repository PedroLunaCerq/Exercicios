import random
jogo = []
jogos = []

quantidade = int(input('Quantos jogos você irá fazer? '))
for i in range(quantidade):
    for c in range(0, 6):
        n = random.randrange(1, 60)
        jogo.append(n)
    jogos.append(jogo)
    jogo = []

print('Você pode fazer os seguintes jogos:')
for c in jogos:
    print(c)