list = []
print('Digite [00] para parar!')
while True:
    n = int(input('Digite um número: '))
    if n not in list:
        list.append(n)
    if n == 00:
        break
print('=' * 15)
list.sort()
print(list)
print('=' * 15)