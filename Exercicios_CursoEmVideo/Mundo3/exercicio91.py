import random, time

jogador = {}
jogadas = []
jogadores = []

print('-' * 15)
for c in range(0, 4):
    jogada = random.randrange(1, 7)
    print(f'O {c + 1}° jogador tirou {jogada}.')
    jogadas.append(jogada)
    time.sleep(1)
print('-' * 15)
jogadas.sort()

jogador['jogador1'] = jogadas[0]
jogador['jogador2'] = jogadas[1]
jogador['jogador3'] = jogadas[2]
jogador['jogador4'] = jogadas[3]
jogadores.append(jogador.copy())

print(f"""Primeiro lugar: {jogador['jogador4']}
Segundo lugar: {jogador['jogador3']}
Terceiro lugar: {jogador['jogador2']}
Quarto lugar: {jogador['jogador1']}""")

print('''<<< O jogo acabou! >>>
''')