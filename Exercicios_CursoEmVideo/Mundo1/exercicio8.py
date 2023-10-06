n1 = float(input('Insira a primeira nota:'))
n2  = float(input('Insira a segunda nota:'))
n3 = (n1+n2) / 2
if n3 >= 6:
    print('Parabéns, você foi aprovado com a média \033[34m{}\033[m!'.format(n3))
else:
    print('Vish, você reprovou com a média \033[31m{}\033[m!'.format(n3))