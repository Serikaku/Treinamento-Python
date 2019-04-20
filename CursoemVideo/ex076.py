lista = ('Lapis', 1.75, 'Borracha', 2, 'Caderno', 15.9,
         'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)

linha = '-'*40
print(linha)
print(f'{"Listagem de precos":^40}')
print(linha)
for i in range(0, len(lista), 2):
    print(f'{lista[i]:.<30}R${lista[i+1]:>8.2f}')

print(linha)
