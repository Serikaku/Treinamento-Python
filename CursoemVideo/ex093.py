jogador = dict()
gols = list()
linha = '-'*35

jogador['nome'] = str(input('Nome do jogador: '))
total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(0, total):
    gols.append(int(input(f'  Quantos gols na partida {i}? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print(linha)
print(jogador)
print(linha)
for c, v in jogador.items():
    print(f'O campo {c} tem o valor {v}')

print(linha)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f' -> Na partida {i}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')
