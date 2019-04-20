from random import randint

tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print('Os valores sorteados foram:', end=' ')
for i in tupla:
    print(f'{i}', end=' ')
print(f'\nO maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')
