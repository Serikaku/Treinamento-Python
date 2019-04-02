x = float(input('Digite a velocidade de um carro: '))

if x > 80:
    print('Voce foi multado em R${:.2f}'.format((x-80)*7))
