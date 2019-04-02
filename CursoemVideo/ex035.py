x = float(input('Primeiro segmento : '))
y = float(input('Segundo segmento : '))
z = float(input('Terceiro segmento : '))

if x < y + z and y < x + z and z < x + y:
    print('Os segmentos podem formar um triangulo')
else:
    print('Os segmentos nao podem formar um triangulo')
