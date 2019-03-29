dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos kms o carro rodou? '))
total = (dias * 60) + (km * 0.15)
print('Preco total a pagar: R${:.2f}'.format(total))
