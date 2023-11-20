def leiaint(n):
    if n not in '0123456789':
        while True:
            n = input('Erro! Digite um número inteiro: ')
            if n in '0123456789':
                break
    print(f'Você digitou {n}.')


n = input('Digite um número inteiro: ')
leiaint(n)