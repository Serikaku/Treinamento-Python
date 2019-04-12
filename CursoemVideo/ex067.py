while True:
    n = int(input('Quer ver a tabuada de qual valor? (negativo para parar) '))
    if n < 0:
        break
    print('-'*20)
    for i in range(0, 11):
        print(f'{n} x {i} = {n*i}')
    print('-'*20)

print('Programa encerrado')
