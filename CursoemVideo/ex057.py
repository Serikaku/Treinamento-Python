sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()

while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Digite seu sexo [M/F]: ')).strip().upper()
print('Sexo {} registrado com sucesso'.format(sexo))
