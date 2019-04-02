x = int(input('Primeiro valor: '))
y = int(input('Segundo valor: '))
z = int(input('Terceiro valor: '))

menor = x

if y < z and y < x:
    menor = y
if z < x and z < y:
    menor = z

print('O menor valor foi {}'.format(menor))

maior = x

if y > z and y > x:
    maior = y
if z > x and z > y:
    maior = z

print('O maior valor foi {}'.format(maior))
