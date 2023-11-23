def pyhelp(funcao):
    resp = help(funcao)
    return resp

texto = 'Bem vindo ao sistema de ajuda PyHelp!'
texto_cent = texto.center(20)
print('=' * 20)
print(texto_cent)
print('=' * 20)
while True:
    arg = input('Qual função deseja ver a docstring? ').lower()
    if arg == 'fim':
        break
    else:
        resp = pyhelp(arg)
        print('-' * 20)