lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, len(lista)):
    for j in range(0, len(lista[i])):
        lista[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))

for i in range(0, len(lista)):
    for j in range(0, len(lista[i])):
        print(f'[{lista[i][j]:^5}]', end='')
    print()
