from random import randint

print("Jokenpo")
print('-'*30)

itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
vc = int(input('''Suas opcoes:
0 - Pedra
1 - Papel
2 - Tesoura
Qual e a sua jogada? '''))

print('-'*30)

print('Computador jogou {}'.format(itens[pc]))

print('Jogador jogou {}'.format(itens[vc]))

print('-'*30)

if pc == 0:
    if vc == 0:
        print('Empate')
    elif vc == 1:
        print('Jogador ganhou')
    elif vc == 2:
        print('Computador ganhou')
    else:
        print('Jogada invalida')
elif pc ==1:
    if vc == 0:
        print('Computador ganhou')
    elif vc == 1:
        print('Empate')
    elif vc == 2:
        print('Jogador ganhou')
    else:
        print('Jogada invalida')
elif pc ==2:
    if vc == 0:
        print('Jogador ganhou')
    elif vc == 1:
        print('Computador ganhou')
    elif vc == 2:
        print('Empate')
    else:
        print('Jogada invalida')
