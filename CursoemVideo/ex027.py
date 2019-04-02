nome = str(input('Difite o nome: ')).strip()

lista = nome.split()

print('Primeiro nome: {}'.format(lista[0]))
print('Ulrimo nome: {}'.format(lista[len(lista)-1]))
