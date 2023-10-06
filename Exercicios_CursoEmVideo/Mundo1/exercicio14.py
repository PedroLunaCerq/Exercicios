salario = float(input('Insira seu salário:'))
aumento = int(input('Insira a porcentagem que seu salário foi aumentado:'))
porcentagem_aumento = (aumento / 100) * salario
salario_atual = salario + porcentagem_aumento
print('O seu aumento foi de', aumento, 'por cento! Seu novo salário agora é', salario_atual)