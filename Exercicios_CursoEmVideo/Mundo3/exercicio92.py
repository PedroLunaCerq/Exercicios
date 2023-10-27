pessoa = {}

pessoa['nome'] = input('Insira seu nome: ').title()
ano_de_nascimento = int(input('Insira seu ano de nascimento: '))
pessoa['idade'] = 2023 - ano_de_nascimento
pessoa['ctps'] = int(input('Insira sua carteira de trabalho: '))
if pessoa['ctps'] != 0:
    pessoa['ano_de_contratacao'] = int(input('Insira o ano de contratação: '))
    pessoa['salario'] = int(input('Insira o salário: '))
    pessoa['aposentadoria'] = ((pessoa['ano_de_contratacao'] + 35) - 2023) + pessoa['idade']

print('-' * 15)

if pessoa['ctps'] != 0:
    print(f"""O nome é {pessoa['nome']} e possui {pessoa['idade']} anos.
    Sua CTPS é {pessoa['ctps']}, foi contratado em {pessoa['ano_de_contratacao']}, recebe {pessoa['salario']} e se apoosenta com {pessoa['aposentadoria']}.""")

else:
    print(f"O nome é {pessoa['nome']} e possui {pessoa['idade']} anos.")

print('''<<< Programa encerrado! >>>''')
print()