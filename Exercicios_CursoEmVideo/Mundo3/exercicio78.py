numbers = []
for c in range(0, 5):
    numbers.append(input('Insira um número: '))
numbers.sort(reverse=True)
print('=' * 15)
print(f'O maior valor dos numeros citados foi {numbers[0]} e o menor foi {numbers[4]}.')
print('=' * 15)