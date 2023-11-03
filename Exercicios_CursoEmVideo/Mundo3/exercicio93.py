jogadores = []
jogador = {}

while True:
    gols = []
    total = 0
    jogador.clear()
    jogador['nome'] = input('Insira o nome do jogador: ').title()
    partidas = int(input('Insira quantas partidas ele jogou no campeonato: '))
    jogador['partidas'] = partidas
    for c in range(partidas):
        a = int(input(f'Quantos gols foram marcados na {c + 1}° partida? '))
        gols.append(a)
        total += a
    jogador['gols'] = gols[:]
    jogador['total'] = total
    jogadores.append(jogador.copy())
    operar = input('Deseja continuar? [S/N] ')
    if operar in 'Nn':
        break

print('-' * 15)
for c, jogador in enumerate(jogadores):
    print(f"{c + 1}° - {jogadores[c]['nome']}")
print()
while True:
    operar = int(input('Deseja ver as informações de qual jogador? [0 Cancela]: '))
    if operar == 0:
        break
    print(jogadores[operar - 1])
print('<<Programa Encerrado!>>')