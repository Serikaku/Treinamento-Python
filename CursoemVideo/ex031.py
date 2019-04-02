x = int(input('Digite a distancia da viagem em km: '))

if x <= 200:
    print('A passagem custa R${:.2f}'.format(x*0.50))
else:
    print('A passagem custa R${:.2f}'.format(x*0.45))
