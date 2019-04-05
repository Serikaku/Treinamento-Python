maior = 0
menor = 0

for i in range(0,5):
    x = float(input('Digite o peso de uma pessoa: '))
    if i == 0:
        menor = x
        maior = x
    if maior < x:
        maior = x
    if menor > x:
        menor = x

print('O maior peso foi {}Kg e o menor foi {}Kg'.format(maior, menor))
