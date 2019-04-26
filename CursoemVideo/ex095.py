jogadores = list()
jogador = dict()
gols = list()
linha = '-'*35
while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range(0, total):
        gols.append(int(input(f'  Quantos gols na partida {i+1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    while True:
        cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if cont in 'SN':
            break
        print('Erro! Responda apenas S ou N')
    if cont == 'N':
        break

print(linha)

print(f'{"cod":<4} {"nome":<15} {"gols":<15} {"total":<15}')
for i, v in enumerate(jogadores):
    print(f'{i:<4} {v["nome"]:<15} {str(v["gols"]):<15} {v["total"]:<15}')

while True:
    print(linha)
    qual = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if qual == 999:
        break
    if qual < len(jogadores):
        print(f'Levantamento do jogador {jogadores[qual]["nome"]}')
        for i, v in enumerate(jogadores[qual]['gols']):
            print(f'  No jogo {i+1} fez {v} gols')
    else:
        print(f'Erro! nao existe jogador com o codigo {qual}')
print('Volte sempre')
