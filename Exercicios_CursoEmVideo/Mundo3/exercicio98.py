from time import sleep
def contador(inicio, fim, passo):
    for n in range(inicio, fim + 1, passo):
        print(n)
        sleep(0.3)

#de 1 em 1
print('-' * 20)
print('De 0 à 10!')
for n in range(0, 11):
    print(n),
    sleep(0.3)
print('-' * 20)

#ao  contrário e de 2 em 2
print('De 10 à 0, com passo de 2!')
lista = []
for n in range(0, 12, 2):
    lista.append(n)
lista.sort(reverse=True)
for i in lista:
    print(i)
    sleep(0.3)
print('-' * 20)

#personalizado
print('Agora é sua vez de personalizar!')
start = int(input('Início: '))
end = int(input('Fim: '))
step = int(input('Passo: '))
contador(start, end, step)