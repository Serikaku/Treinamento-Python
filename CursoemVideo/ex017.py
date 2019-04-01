from math import hypot

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
h = hypot(co, ca)
print('Em um triangulo retangulo de catetos de tamanhos {} e {}, o comprimento da hipotenusa e {:.2f}'.format(co, ca, h))
