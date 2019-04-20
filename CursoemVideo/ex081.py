lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    c = str(input('Deseja continuar? [S/N] ')).strip()
    if c in 'Nn':
        break

print(f'Voce digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente sao {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 nao faz parte da lista!')
