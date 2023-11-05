def área(larg, comp):
    area = largura * comprimento
    return area

largura = int(input('Insira a largura do terreno: '))
comprimento = int(input('Agora, seu comprimento: '))
area = área(largura, comprimento)

print(f'A área do terreno é igual á {area}m².')