import random

# Banco de dados das palavras:

banco = {'Animal': ['girafa', 'elefante', 'cachorro', 'baleia', 'tartaruga'],
         'Objeto': ['monitor', 'computador', 'estante', 'impressora'],
         'Time': ['fluminense', 'botafogo', 'vasco', 'flamengo']}

tema_escolhido = random.choice(list(banco.keys()))
escolha = random.choice(banco[tema_escolhido])

# Início do jogo:

quant_letras = len(escolha)
lacuna = []
vida = [3]

for j in range(0, quant_letras):      # Adiciona n lacunas para n letras da palavra escolhida
    lacuna.append('_')

print('--------------Bem-vindo ao jogo da forca!--------------')
print(f'Você tem {vida[0]} vidas!\nDica é um {tema_escolhido}.')
print('-------------------------------------------------------')
print(lacuna)                         # Printa a lista inicial

# Função criada para verificar se a letra informada pelo usuário se encontra na palavra
def substituicao(letra_escolhida, vida):
    antiga_lacuna = tuple(lacuna)
    if len(letra_escolhida) > 1:
        print('Só pode uma letra por vez!')
    for i in range(0, quant_letras):
        if letra_escolhida == escolha[i]:
            lacuna[i] = letra_escolhida
    if antiga_lacuna == tuple(lacuna):
        vida[0] = vida[0] - 1
        print(f'Não há letra {letra_escolhida} na palavra! Você perdeu uma vida, lhe restam {vida[0]}!')
    print('-------------------------------------------------------')
    return lacuna, vida

# Quando tiver mais de três lacunas, o usuário tem que chutar apenas uma letra por vez:

while lacuna.count('_') > 3:
    if vida[0] == 0:
        print('INFELIZMENTE, você não tem mais vidas.Tente novamente!')
        break
    letra_escolhida1 = input('QUAL LETRA VOCÊ ESCOLHE?')
    letra_escolhida = letra_escolhida1.lower()
    substituicao(letra_escolhida, vida)
    print(lacuna)

# Quando tiver faltando três lacunas, o usuário tem que informar a palavra que ele acha ser a correta

if lacuna.count('_') <= 3:
    print('----------------------------PRESTE ATENÇÃO------------------------')
    palavra_final = input('QUAL É A PALAVRA?')
    palavra_final_1 = palavra_final.lower()
    print('-------------------------------------------------------')
    if palavra_final_1 == escolha:
        print(f'PARABÉNS, VOCÊ VENCEU!')
    else:
        print(f'INFELIZMENTE, você errou a palavra, tente novamente!')
    print('-------------------------------------------------------')