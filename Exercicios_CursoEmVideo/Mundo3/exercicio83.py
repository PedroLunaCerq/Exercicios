exp = input('Insira uma expressão: ')
pilha = []

for c in exp:
    if c == '(':
        pilha.append('(')
    elif c == ')':
        pilha.pop()

if len(pilha) > 0:
    print('Sua expressão é inválida!')
else:
    print('Sua expressão está válida!')