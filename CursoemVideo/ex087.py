lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

somapar = maior = somacol = 0

for i in range(0, len(lista)):
    for j in range(0, len(lista[i])):
        lista[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))

for i in range(0, len(lista)):
    for j in range(0, len(lista[i])):
        print(f'[{lista[i][j]:^5}]', end='')
        if lista[i][j] % 2 == 0:
            somapar += lista[i][j]
        if j == 2:
            somacol += lista[i][j]
    print()

print(f'A soma dos valores pares e {somapar}')
print(f'A soma da terceira coluna e {somacol}')

for i in range(0, 3):
    if i == 0:
        maior = lista[1][i]
    elif lista[1][i] > maior:
        maior = lista[1][i]
print(f'O maior valor da segunda linha e {maior}')