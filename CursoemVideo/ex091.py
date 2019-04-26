from random import randint
from time import sleep
from operator import itemgetter

jog = {}
rank = []
for i in range(1, 5):
    jog[f'jogador{i}'] = randint(1, 6)

print('Valores sorteados:')
for c, v in jog.items():
    print(f'{c} tirou {v} no dado')
    sleep(0.5)

rank = sorted(jog.items(), key=itemgetter(1), reverse=True)

print(' == Ranking dos jogadores == ')
for i, v in enumerate(rank):
    print(f'  {i+1}º lugar: {v[0]} com {v[1]}')
