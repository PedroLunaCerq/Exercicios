def ficha(nome, gols):
    print(f'O nome é {nome} e fez {gols} gols.')

name = input('Insira o nome do jogador: ')
if len(name) < 1:
    name = '<desconhecido>'
points = input('Insira quantos gol(s) foram feitos: ')
if len(points) < 1:
    points = '<indefinido>'

ficha(name, points)