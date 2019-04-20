lista = []

for i in range(0, 5):
    x = int(input('Digite um valor: '))
    if i == 0 or x > lista[-1]:
        lista.append(x)
        print('Numero inserido na ultima posicao')
    else:
        pos = 0
        while pos < len(lista):
            if x <= lista[pos]:
                lista.insert(pos, x)
                print(f'Numero inserido na posicao {pos} da lista...')
                break
            pos += 1
print(f'Os valores digitados foram {lista}')
