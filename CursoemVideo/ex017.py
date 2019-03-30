from math import sqrt

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
h = sqrt(ca**2 + co**2)
print('Em um triangulo retangulo de catetos de tamanhos {} e {}, o comprimento da hipotenusa e {}'.format(co, ca, h))
