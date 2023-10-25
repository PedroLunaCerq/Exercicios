import random
a1 = str(input('Insira o nome do primeiro integrante:'))
a2 = str(input('Insira o nome do segundo integrante:'))
a3 = str(input('Insira o nome do terceiro integrante:'))
a4 = str(input('Insira o nome do quarto integrante:'))
grupo = [a1, a2, a3, a4]
random.shuffle(grupo)
print('A ordem de apresentação será: ', grupo)