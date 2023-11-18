def fatorial(n, show=False):
    resultado = 1
    for n in range(1, n + 1):
        resultado *= n
    return resultado

num = int(input('Insira o número para ver seu fatorial: '))
fat = fatorial(num)
print(f'{num}! é {fat}')
