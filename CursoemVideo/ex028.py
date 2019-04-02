from random import randint

x = randint(0, 5)
print(x)

y = int(input('Adivinhe um numero de 0 a 5: '))
if x == y:
    print('Acertou')
else:
    print('Errou')
