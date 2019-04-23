lista = []
pessoa = []
pesado = leve = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(lista) == 0:
        pesado = leve = pessoa[1]
    else:
        if pessoa[1] > pesado:
            pesado = pessoa[1]
        if pessoa[1] < leve:
            leve = pessoa[1]
    lista.append(pessoa[:])
    pessoa.clear()
    cont = str(input('Deseja continuar? [S/N] ')).strip()
    if cont in 'Nn':
        break
print(f'{len(lista)} pessoas foram cadastradas.')
print(f'O maior peso foi de {pesado}Kg. Peso de ', end='')
for p in lista:
    if p[1] == pesado:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {leve}Kg. Peso de ', end='')
for p in lista:
    if p[1] == leve:
        print(f'[{p[0]}]', end=' ')
