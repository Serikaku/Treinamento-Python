from random import randint

x = randint(0, 10)
#print(x)
acerto = 0
i = 0

while acerto == 0:
    y = int(input('Adivinhe um numero de 0 a 10: '))
    i += 1
    if x == y:
        acerto = 1
    else:
        if x > y:
            print('Mais. Tente novamente.')
        else:
            print('Menos. Tente novamente.')
if i == 1:
    print('Acertou de primeira.')
else:
    print('Acertou. Foram necessarios {} palpites para vencer.'.format(i))
