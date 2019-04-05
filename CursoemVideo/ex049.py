x = int(input('Digite um numero inteiro para saber sua tabuada: '))
for i in range(0, 11):
    print('{} x {:2} = {}'.format(x, i, x*i))
