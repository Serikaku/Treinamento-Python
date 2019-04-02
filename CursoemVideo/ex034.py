x = float(input('Digite o salario do funcionario: R$'))

if x > 1250:
    print('O novo salario eh R${:.2f}'.format(x * 1.1))
else:
    print('O novo salario eh R${:.2f}'.format(x * 1.15))
