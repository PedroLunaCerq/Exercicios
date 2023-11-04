peso = int(input('Insira o peso, em KG: '))
excesso = 0
multa = 0


for n in range(50, peso):
    excesso += 1
for e in range(excesso):
    multa += 4

print(f'Você pescou {peso}kg hoje! Seu excesso é de {excesso}kg e a multa é de R${multa}')