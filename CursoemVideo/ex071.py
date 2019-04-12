
print('-' * 20)
print('{:^20}'.format('ATM'))
print('-' * 20)

valor = int(input('Que valor deseja sacar? R$'))

cedula = 50
n = 0

while True:
    quantidade = valor//cedula
    if quantidade > 0:
        print(f'Total de {quantidade} cedulas de R${cedula}')
    valor -= quantidade*cedula
    if cedula == 50:
        cedula = 20
    elif cedula == 20:
        cedula = 10
    elif cedula == 10:
        cedula = 1
    if valor == 0:
        break
print('-' * 20)
print('Volte sempre')
