def escreva(str):
    print('~' * (len(str) + 4))
    print(str.center(len(str) + 4))
    print('~' * (len(str) + 4))

texto = input('Insira seu texto: ')
escreva(texto)