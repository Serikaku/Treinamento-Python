x = int(input('Digite um numero inteiro: '))

primo = 0

for i in range(1, x + 1):
    if x % i == 0:
        print('\033[33m', end='')
        primo += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')

print('\033[m')
if primo == 2:
    print('Numero Primo')
else:
    print('Numero Nao Primo')
