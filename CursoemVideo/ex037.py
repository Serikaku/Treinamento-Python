x = int(input('Digite um numero inteiro: '))
y = int(input('Digite 1 para converter para binario, 2 para octal e 3 para hexadecimal: '))

if y == 1:
    print('O numero {} em binario eh: {}'.format(x, bin(x)[2:]))
elif y == 2:
    print('O numero {} em octal eh: {}'.format(x, oct(x)[2:]))
elif y == 3:
    print('O numero {} em hexadecimal eh: {}'.format(x, hex(x)[2:]))
else:
    print('Voce digitou um opcao invalida')
