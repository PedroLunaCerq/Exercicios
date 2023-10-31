jogador = {}
gols = []
total = 0

jogador['nome'] = input('Insira o nome do jogador: ').title()
partidas = int(input('Insira quantas partidas ele jogou no campeonato: '))
jogador['partidas'] = partidas
for c in range(partidas):
    a = int(input(f'Quantos gols foram marcados na {c + 1}° partida? '))
    gols.append(a)
    total += a
jogador['gols'] = gols[:]
jogador['total'] = total

print(f"O nome do jogador é {jogador['nome']}, jogou {jogador['partidas']} partidas e no total fez {jogador['total']} gols.")
print('-' * 15)
for c, gol in enumerate(jogador['gols']):
    print(f'Na {c + 1}° partida fez {gol} gols.')
print(f'Foi um total de {total} gols')
print('-' * 15)
print('<<Programa encerrado!>>')
print()