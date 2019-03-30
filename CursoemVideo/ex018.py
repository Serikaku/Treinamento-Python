import cmath
grau = float(input('Digite um angulo: '))
ang = grau * 3.14159265 / 180
seno = cmath.sin(ang)
cosseno = cmath.cos(ang)
tangente = cmath.tan(ang)
print('O angulo {} possui seno {}, cosseno {} e tangente {}'.format(grau, seno, cosseno, tangente))