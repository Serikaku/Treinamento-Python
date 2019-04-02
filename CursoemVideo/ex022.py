nome = str(input('Digite seu nome: '))

print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
espaco = nome.count(' ')
print('Seu nome tem ao todo {} letras'.format(len(nome)-espaco))
lista = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(lista[0], len(lista[0])))
