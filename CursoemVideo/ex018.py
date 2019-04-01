import math
grau = float(input('Digite um angulo: '))
ang = math.radians(grau)
seno = math.sin(ang)
cosseno = math.cos(ang)
tangente = math.tan(ang)
print('O angulo {} possui seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(grau, seno, cosseno, tangente))