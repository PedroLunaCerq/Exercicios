alt = float(input('Insira sua altura: '))
gen = input('Agora, seu gênero: [H/M] ').upper()

if gen == 'H':
    peso = (72.7 * alt) - 58

elif gen == 'M':
    peso = (62.1 * alt) - 44.7

print(f'Seu peso ideal é {peso}')