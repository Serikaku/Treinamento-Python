tupla = ('Athletico-PR', 'Atlético-MG', 'Avaí', 'Bahia', 'Botafogo',
         'CSA', 'Ceará', 'Chapecoense', 'Corinthians', 'Cruzeiro',
         'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Grêmio',
         'Internacional', 'Palmeiras', 'Santos', 'São Paulo', 'Vasco')

print(f'Lista de times do brasileirao: {tupla}')
print('-='*30)
print(f'Os 5 primeiros sao: {tupla[0:5]}')
print('-='*30)
print(f'Os 4 ultimos sao: {tupla[-4:]}')
print('-='*30)
print(f'Times em ordem alfabetica: {sorted(tupla)}')
print('-='*30)
print(f'O Chapecoense esta na {tupla.index("Chapecoense")+1}ª posicao')
