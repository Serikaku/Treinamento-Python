lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um valor: ')))
    c = str(input('Deseja continuar? [S/N] ')).strip()
    if c in 'Nn':
        break

for v in lista:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(f'\nA lista completa e {lista}')
print(f'A lista de pares e {pares}')
print(f'A lista de impares e {impares}')