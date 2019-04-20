lista = []

while True:
    x = int(input('Digite um valor: '))
    if x in lista:
        print('Valor duplicado! Nao vou adicionar...')
    else:
        lista.append(x)
        print('Valor adicionado com sucesso...')
    c = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if c in 'N':
        break
lista.sort()
print(f'Voce digitou os valores {lista}')
