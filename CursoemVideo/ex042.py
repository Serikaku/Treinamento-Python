x = float(input('Primeiro segmento : '))
y = float(input('Segundo segmento : '))
z = float(input('Terceiro segmento : '))

if x < y + z and y < x + z and z < x + y:
    print('Os segmentos podem formar um triangulo', end='')
    if x == y == z:
        print(' equilatero')
    elif x == y != z or x == z != y or y == z != x:
        print(' isoceles')
    else:
        print(' escaleno')

else:
    print('Os segmentos nao podem formar um triangulo')
