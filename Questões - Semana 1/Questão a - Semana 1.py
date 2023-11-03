import random

rodadas = 5

lista_1 = ['pedra', 'papel', 'tesoura']
vitoria_usuario = 0
vitoria_pc = 0
print('--------------------Bem-vindo ao jogo--------------------')
while vitoria_usuario < rodadas and vitoria_pc < rodadas:
    usuario = input('Escolha uma opção, pedra, papel ou tesoura:')
    pc = random.choice(lista_1)
    
    if usuario == 'pedra' and pc == 'papel' or usuario == 'papel' and pc == 'tesoura' or usuario == 'tesoura' and pc == 'pedra':
        print(f'DERROTA, pois você escolheu {usuario} e o computador {pc}.')
        vitoria_pc += 1
    elif usuario == pc:
        print(f'EMPATE, pois ambos escolheram {pc}.')
    else:
        print(f'VITÓRIA, pois você escolheu {usuario} e o computador {pc}.')
        vitoria_usuario += 1
    print(f'Usuário {vitoria_usuario} X {vitoria_pc} PC')
    print('------------------------------------------------------')

if vitoria_usuario == rodadas:
    print(f'CAMPEÃO, parabéns!! Você merece!!')
else:
    print(f'Infelizmente, você perdeu. Não se preocupe, você já é um vencedor por existir!')
print('------------------------------------------------------')

