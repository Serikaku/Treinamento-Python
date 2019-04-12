maiores = homens = mulheres = i = 0

while True:
    print('-' * 20)
    print('Cadastre uma pessoa')
    print('-' * 20)
    i = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 20)
    if i > 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and i < 20:
        mulheres += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break

print('-' * 20)
print('Fim do programa')
print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')
