

nome = (input('Digite o nome de sua cidade:')).strip()
print(nome[:5].upper() == 'SANTO')

#nome = str(input('Digite o seu nome:')).strip()
#print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))

#frase = str(input('Insira uma frase:'))
#print('A letra A aparece um total de {} vezes'.format(frase.count('A')))
#print('Aparece pela primeira vez na posição {}'.format(frase.find('A')))
#print('E aparece pela última vez na posição {}'.format(frase.find('A':-1)))

#(errado)
#nome = str(input('Digite seu nome:')).strip()
#n = nome.split()
#print('{}'.format(n[0]))
#print('{}'.format(nome[len(nome)-1]))

#n1 = float(input('Digite a primeira nota:'))
#n2 = float(input('Digite a segunda nota:'))
#m = (n1 + n2) / 2
#print('A sua nota final foi {:.1f}!'.format(m))
#if m >= 6:
#    print('Você foi aprovado! Parabéns!')
#else:
#    print('Você foi reprovado! Estude mais.')



#import random
#n = random.randrange(0, 5)
#chute = int(input('Esclha um número de 0 a 5:'))
#if chute == n:
#     print('Parabéns! Você acertou.')
#else:
#    print('Vish, você errou.')

#v = float(input('Insira a sua velocidade atual:'))
#if v <= 80:
#    print('Você não levou multas.')
#else:
#    print('Você levou uma multa de {}'.format((v - 80) * 7))


#n = int(input('Insira um número:'))
#if n % 2 == 0:
#    print('Seu número é par.')
#else:
#    print('Seu número é ímpar.')

#d = float(input('Insira a distância em km:'))
#if d <= 200:
#    print('O preço da viagem custará R${}.'.format(d * 0.5))
#else:
#    print('O preço da viagem custará R${}.'.format(d * 0.45))

#ano = int(input('Insira um ano:'))
#if ano % 4 == 0:
#    print('O ano {} é bissexto.'.format(ano))
#else:
#    print('O ano {} não é bissexto.'.format(ano))

#n_ord = []
#n1 = int(input('Insira um número: '))
#n2 = int(input('Insira outro número: '))
#n3 = int(input('Insira um terceiro número: '))
#n_ord.append(n1)
#n_ord.append(n2)
#n_ord.append(n3)
#n_ordenado = n_ord.sort()
#n_maior = n_ord[2]
#n_menor = n_ord[0]
#print('O maior número do conjunto \033[7m{}\033[m é \033[1m{}\033[m e o menor é \033[1m{}\033[m.'.format(n_ord, n_maior, n_menor))

#s = float(input('Insira seu salário: '))
#if s > 1.250:
#    s1 = (10 / 100) * s
#    salario2 = s + s1
#    print('Parabéns! Seu aumento salarial é de {} para {:.2f}.'.format(s, salario2))
#else:
#    s2 = (15 / 100) * s
#    salario1 = s + s2
#    print('Parabéns! Seu aumento salarial é de {} para {:.2f}.'.format(s, salario1))

# mundo 2

#salario = float(input('Insira seu salário: '))
#valor_casa = float(input('Insira o valor de sua casa: '))
#tempo = int(input('E em quanto tempo pretende pagar? Em meses. '))
#trinta = (30/100) * salario
#emprestimo = valor_casa / tempo
#if emprestimo > trinta:
#    print('Desculpe, mas seu pedido foi recusado!')
#else:
#    print('O valor que você irá pagar é {:.3f} durante {:.3f}!'.format(emprestimo, tempo))

#n1 = int(input('Insira um número: '))
#n2 = int(input('Insira um segundo número: '))
#if n1 > n2:
#    print('Neste caso, {} é maior do que {}'.format(n1, n2))
#elif n2 > n1:
#    print('Neste caso, {} é maior do que {}'.format(n2, n1))
#else:
#    print('Não há diferença, {} e {} são iguais.'.format(n1, n2))

#ano = int(input('Insira o ano em que você nasceu: '))
#idade = 2023 - ano
#faltante = 18 - idade
#if idade == 18:
    #print('Está na hora de se alistar.')
#elif idade < 18:
    #print('Ainda faltam {} anos para se alistar'.format(faltante))
#else:
    #print('Seu tempo de alistamento já passou.')

#n1 = float(input('Insira a primeira nota: '))
#n2 = float(input('Insira a segunda nota: '))
#nf = (n1 + n2) / 2
#if nf < 5:
#    print('Você está de reprovado com a média {:.1f}.'.format(nf))
#elif nf > 5 and nf < 6:
#    print('Você está de recuperação com a média {:.1f}.'.format(nf))
#elif nf > 6:
#    print('Você está aprovado com a média {:.1f}.'.format(nf))

#ano = int(input('Insira o ano de nascimento do atleta: '))
#idade = 2023 - ano
#if idade <= 9:
#    print('A categoria de um atleta de {} anos é mirim.'.format(idade))
#elif idade <=14:
#    print('A categoria de um atleta de {} anos é infantil.'.format(idade))
#elif idade <= 19:
#    print('A categoria de um atleta de {} anos é júnior.'.format(idade))
#elif idade <= 20:
#    print('A categoria de um atleta de {} anos é sênior.'.format(idade))
#elif idade > 20:
#    print('A categoria disputada por um atleta de {} anos é master.'.format(idade))

#peso = float(input('Insira seu peso: '))
#altura = float(input('Insira sua altura: '))
#imc = peso / altura**2
#if imc < 18.5:
#    print('Seu IMC é de {:..1f} e você está abaixo do peso!'.format(imc))
#elif imc < 25:
#    print('Seu IMC é de {:.1f} e você está no peso ideal.'.format(imc))
#elif imc < 30:
#    print('Seu IMC é de {:.1f} e você está acima do peso.'.format(imc))
#elif imc < 40:
#    print('Seu IMC é de {:.1f} e você se encontra em obesidade!'.format(imc))
#elif imc > 40:
#    print('Seu IMC se encontra em {:.1f} e você se encontra em obesidade mórbida!!!'.format(imc))

#preço = float(input('Insira o valor do produto em R$: '))
# = int(input('Qual seu método de pagamento? Insira 1 para dinheiro, 2 para cartão, 3 para parcelar em 2x  4 para parcelar em 3x: '))
#dinheiro = preço - (10/100) * preço
#cartao = preço - (5/100) * preço
#juros = (20/100) * preço + preço
#if metodo == 1:
#    print('Pagar no dinheiro oferece desconto de 10%, totalizando R${}.'.format(dinheiro))
#elif metodo == 2:
#    print('Pagar no cartão oferece desconto de 5%, totalizando R${}.'.format(cartao))
#elif metodo == 3:
#    print('Parcelar 2x no cartão oferece o preço normal, totalizando R${}.'.format(preço))
#elif  metodo == 4:
#    print('Parcelar em 3x ou mais há 20% de juros, totalizando R${}.'.format(juros))

#desafio 45: fazer um jogo de jokenpo
#from random import randint
#from time import sleep
#itens = ('Pedra', 'Papel', 'Tesoura')
#computador = randint(0, 2)
#print('Suas opções são:')
#print('[0] Pedra')
#print('[1] Papel')
#print('[2] Tesoura')
#jogador = int(input('Qual a sua jogada? '))
#print('Jo')
#sleep(1)
#print('Ken')
#sleep(1)
#print('Pô!')
#print('-=' * 11)
#print('Computador jogou {}.'.format(itens[computador]))
#print('Você jogou {}.'.format(itens[jogador]))
#print('-=' * 11)
#if computador == 0: #Computador jogou PEDRA
#    if jogador == 0:
#        print('Empate!')
#    elif jogador == 1:
#        print('Jogador vence!')
#    elif jogador == 2:
#        print('Computador vence!')
#    else:
#        print('JOGADA INVÁLIDA!')
#elif computador == 1: #Computador jogou PAPEL
#    if jogador == 0:
#        print('Computador vence!')
#    elif jogador == 1:
#        print('Empate!')
#    elif jogador == 2:
#        print('Jogador vence!')
#    else:
#        print('JOGADA INVÁLIDA!')
#elif computador == 2: #Computador jogou TESOURA
#    if jogador == 0:
#        print('Jogador vence!')
#    elif jogador == 1:
#        print('Computador vence!')
#    elif jogador == 2:
#        print('Empate!')
#    else:
#        print('JOGADA INVÁLIDA!')

#i = 900
#n = 999
#for c in range(i, n, 10):
#    print(c)
#print('fim')

#from time import sleep
#contagem = 0
#for c in range(10, 0, -1):
#    contagem = 0 + c
#    print('Restam {} segundos para os fogos!'.format(contagem))
#    sleep(1)
#print('Os fogos explodiram!')

#for c in range(1, 50, 2):
#    print(c+1)

#s = 0
#for c in range(1, 500):
#        if c % 3 == 0:
#            s += c
#print(s)

#n = int(input('Escolha um número para ver sua tabuada: '))
#for c in range(1, 11):
#   m = n*c
#   print('{} x {} = {}'.format(n, c, m))

#soma = 0
#for c in range(1, 7):
#    n = int(input('Digite um número: '))
#    if n % 2 == 0:
#        soma += n
#print(soma)

#n = int(input('digite um número: '))
#l = 1
#for c in range(2, n):
#    if n % c == 0:
#        l = 0
#if l == 0:
#        print('{} não é um número primo.'.format(n))
#else:
#    print('{} é um número primo!'.format(n))

#frase = str(input('Digite uma frase: ')).strip().upper()
#palavras = frase.split()
#tj = ''.join(palavras)
#inverso = ''
#for letra in range(len(tj) -1, -1, -1):
#    inverso += tj[letra]
#if tj == inverso:
#    print('{} e {} são iguais! Ambos são pallíndromos'.format(tj, inverso))
#else:
#    print('Não são palíndromos.')

#maiores = []
#menores = []
#for c in range(1, 8):
#    ano = int(input('Insira um ano de nascimento: '))
#    if 2023 - ano >= 21:
#        maiores.append(ano)
#    else:
#        menores.append(ano)
#print('Os maiores de idade são os nascidos em {} e os menores nascidos em {}'.format(maiores, menores))

#tabela = []
#for c in range(1, 6):
#    peso = float(input('Insira um peso: '))
#    tabela.append(peso)
#tabela.sort()
#print('O menor peso listado é {} e o maior, {}.'.format(tabela[1],))
##arrumar o final##

#somaidade = 0
#maioridadehomem = 0
#nomemaisvelho = ''
#for p in range(1,5):
#    print('————— {}° pessoa —————'.format(p))
#    nome = str(input('Nome: ')).strip()
#    idade = int(input('Idade: '))
#    sexo = str(input('Sexo [M/F]: ')).strip
#    somaidade += idade
#    if p == 1 and sexo == 'M' or 'm':
#        maioridadehomem = idade
#        nomemaisvelho = nome
#    if sexo == 'M' or 'm' and idade > maioridadehomem:
#        maioridadehomem = idade
#        nomemaisvelho = nome
#mediaidade = somaidade / 4
#print('A média de idade do grupo é de {} anos.'.format(mediaidade))
#print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomemaisvelho))
##Arrumar o 2° print##

#masculino = 'M'
#feminino = 'F'
#s = 0
#while s != masculino and s != feminino:
#    s = str(input('Insira seu sexo [M/F]: ')).upper()
#    if s == 'M':
#        print('Você é um homem!')    
#    elif s == 'F':
#        print('Você é mulher!')
#print('Gg!')

#tentativas = []
#tentativastrue = 0
#jogador = 0
#import random
#bot = str(random.randrange(1, 10))
#while jogador != bot:
#    jogador = str(input('Digite um número de 1 a 10: '))
#    if jogador != bot:
#        tentativas += jogador
#for c in tentativas:
#    tentativastrue = tentativastrue + 1
#print('Gg!')
#print('Você tentou um total de {} vezes.'.format(tentativastrue+1))

#numeros = []
#valor1 = int(input('Insira um valor: '))
#valor2 = int(input('Insira outro valor: '))
#numeros += valor1, valor2
#print('Certo. Agora insira a operação desejada:')
#print('[1] Somar.')
#print('[2] Multiplicar.')
#print('[3] Maior.')
#print('[4] Novos Números.')
#print('[5] Sair do Programa.')
#opcao = str(input('Insira a opção: '))
#if opcao == '1':
#    print('A soma dos valores {} e {} é {}.'.format(valor1, valor2, valor1 + valor2))
#if opcao == '2':
#    print('O produto de {} e {} é igual à {}.'.format(valor1, valor2, valor1 * valor2))
#if opcao == '3':
#    print('O maior numero entre {} e {} é {}'.format(valor1, valor2, numeros[1]))
#if opcao == '4':
##    print('Certo! Insira novos números.')
#    valor1 = int(input('Insira um valor: '))
#    valor2 = int(input('Insira outro valor: '))
#if opcao == '5':
#    print('O programa foi encerrado.')

#opcao = 0
#while opcao != '5':
#    numeros = []
#    valor1 = int(input('Insira um valor: '))
#    valor2 = int(input('Insira outro valor: '))
#    numeros += valor1, valor2
#    print('Certo. Agora insira a operação desejada:')
#    print('[1] Somar.')
#    print('[2] Multiplicar.')
#    print('[3] Maior.')
#    print('[4] Novos Números.')
#    print('[5] Sair do Programa.')
#    opcao = str(input('Insira a opção: '))
#    if opcao == '1':
#        soma = valor1 + valor2
#        print(f'A soma dos valores {valor1} e {valor2} é {soma}.')
#    if opcao == '2':
#        print('O produto de {} e {} é igual à {}.'.format(valor1, valor2, valor1 * valor2))
#    if opcao == '3':
#        numeros.sort()
#        print('O maior numero entre {} e {} é {}'.format(valor1, valor2, numeros[1]))
#    if opcao == '4':
#        print('Certo! Insira novos números.')
#        valor1 = int(input('Insira um valor: '))
#        valor2 = int(input('Insira outro valor: '))
#    if opcao == '5':
#        print('O programa foi encerrado.')
#print('Estou aqui.')

#from math import factorial
#n = int(input('Digite um número para ver seu fatorial: '))
#fatorial = factorial(n)
#print(f'O fatorial de {n} é {fatorial}.')

#n = 0
#soma = 0
#s = []
#while n != 999:
#    n = int(input('Digite um número [999 para parar]: '))
#    str_n = str(n)
#    s += str_n
#    if n != 999:
#        soma += n
#s.remove('9')
#s.remove('9')
#s.remove('9')
#print(f'A soma dos valores que você escreveu é {soma} e os números foram {s}')

#n = soma = numeros = 0
#while True:
#    n = int(input('Digite um valor para somar [999 para parar]: '))
#    if n != 999:
#        soma += n
#        numeros += 1
#    if n == 999:
#        break
#print(f'A soma dos {numeros} números digitados é {soma}.')

#n = tabuada = 0
#while True:
#    n = int(input('Quer ver a tabuada de qual valor? [Números negativos para encerrar!] '))
#    if n >= 0:
#        print('-'*10)
#        for i in range(1, 11):
#            print(f'{n} x {i} = {n * i}')
#    elif  n < 0:
#        break
#print('Programa tabuada encerrado! Volte sempre!')

#vitorias_consecutivas = aa = 0
#import random
#while True:
#    escolha = str(input('Par ou Ímpar? [P/I]: ')).upper()
#    if escolha == 'P':
#        aa = 90
#    bot = random.randrange(1, 10)
#    n = int(input('Agora um número de 1 a 10: '))
#    resultado = n + bot
#    print(f'Você escolheu {escolha} e jogou {n}. O computador jogou {bot} e o resultado é {resultado}.')
#    if resultado % 2 == 0:
#        if aa == 90:
#            vitorias_consecutivas += 1
#            print('Você ganhou! Vamos jogar novamente!')
#        else: 
#            break
#    else:
#        break
#print(f'Você perdeu! e ganhou {vitorias_consecutivas} vezes.')

#pessoas_18 = homens = mulheres_abaixo = 0
#while True:
#    print('-' * 10)
#    idade = int(input('Insira a idade: '))
#    if idade > 18:
#        pessoas_18 += 1
#    sexo = input('Insira o sexo [H/M]: ').upper()
#    if sexo == 'H':
#        homens += 1
#    z = input('Quer encerrar? [S/N] ').upper()
#    if sexo == 'M' and idade < 20:
#        mulheres_abaixo += 1
#    if z == 'S':
#        break
#print(f'''O número de pessoas com +18 anos é {pessoas_18}.
#      Os homens cadastrados são {homens}.
#      As mulheres com -20 anos são {mulheres_abaixo}.''')

#quant_produtos = valor_total = 0
#print('====================================')
#print('        LOJA SUPER BARATÃO          ')
#print('====================================')
#while True:
#    nome = input('Insira o nome do produto: ')
#    preço = float(input('Agora, o seu preço: '))
#    quant_produtos += 1
#    valor_total += preço
#    escolha = input('Deseja comprar mais? [S/N]: ').upper()
#    if escolha == 'N':
#        break
#print(f'Você comprou {quant_produtos} e o preço total é R${valor_total}.')
###ESCREVER TAMBÉM QUAL O PRODUTO MAIS BARATO E O SEU VALOR

#sacar = int(input('Qual valor você quer sacar? '))
#cedulas50 = sacar / 50
#troco50 = sacar % 50
#cedulas20 = troco50 / 20
#troco20 = cedulas20 % 20
#cedulas10 = troco20 / 10
#troco10 = cedulas10 % 10
#cedulas5 = troco10 / 5
#troco5 = cedulas5 % 5
#cedulas1 = troco5 % 1
#print(f'''     Total de {cedulas50:.0f} de R$50
#      Total de {cedulas20:.0f} de R$20
#      Total de {cedulas10:.0f} de R$10
#      Total de {cedulas5:.0f} de R$5
#      Total de {cedulas1:.0f} de R$1''')
##ARRUMAR A EXECUÇÃO