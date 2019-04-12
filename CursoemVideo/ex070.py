total = caros = baratov = i = 0
barato = ' '

print('-' * 20)
print('{:^20}'.format('Loja'))
print('-' * 20)

while True:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preco: R$'))
    total += preco
    if preco > 1000:
        caros += 1
    if i == 0 or preco < baratov:
        barato = nome
        baratov = preco
        i = 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break

print('{:-^40}'.format('Fim do programa'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {caros} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${baratov:.2f}')
