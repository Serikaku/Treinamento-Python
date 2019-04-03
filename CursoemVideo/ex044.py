x = float(input('Digite o valor da compra: '))
y = int(input('''Forma de pagamento
    1   a vista dinheiro/cheque
    2   vista no cartao
    3   2x no cartao
    4   3x ou mais no cartao
    '''))

if y == 1:
    print('O valor a ser pago eh: R${:.2f}'.format(x*0.9))
elif y == 2:
    print('O valor a ser pago eh: R${:.2f}'.format(x*0.95))
elif y == 3:
    print('O valor a ser pago eh: R${:.2f}'.format(x))
elif y == 4:
    print('O valor a ser pago eh: R${:.2f}'.format(x*1.2))
else:
    print('Voce digitou um opcao invalida')
