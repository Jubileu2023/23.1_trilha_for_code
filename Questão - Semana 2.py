

escolha = 'elefante'

quant_letras = len(escolha)
lacuna = []

for j in range(0, quant_letras):
    lacuna.append('_')

print(lacuna)

def substituicao(letra_escolhida):
    for i in range(0, quant_letras):
        if letra_escolhida == escolha[i]:
            lacuna[i] = letra_escolhida
    return lacuna

while lacuna.count('_') > 3:
    letra_escolhida = input('Qual letra você escolhe?')
    substituicao(letra_escolhida)
    print(lacuna)

if lacuna.count('_') == 3:
    palavra_final = input('Qual a palavra?')
    if palavra_final == escolha:
        print(f'Parabéns, você acertou!')
    else:
        print(f'Infelizmente não é essa!')
        print(f'Infelizmente não é essa!')