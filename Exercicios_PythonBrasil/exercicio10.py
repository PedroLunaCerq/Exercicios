n1 = int(input('Insira um número inteiro: '))
n2 = int(input('Insira outro inteiro: '))
n3 = int(input('Agora, um número real: '))

r1 = (n1 * 2) + (n2 / 2)
r2 = (n1 * 3) + n3
r3 = n3 * n3 * n3

print(f"""A soma do dobro do primeiro com metade do terceiro é igual à {r1}
A soma do triplo do primeiro com o terceiro é igual à {r2}
O terceiro ao cubo é igual à {r3}.
""")