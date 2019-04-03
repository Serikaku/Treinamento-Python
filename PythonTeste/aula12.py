nome = str(input('Qual e o seu nome? '))
if nome == 'Rafael':
    print('Que nome bonito')
elif nome == 'Augusto':
    print('Que nome bosta')
elif nome in 'Ana Jessica Juliana':
    print('Belo nome')
else:
    print('Seu nome e bem normal')
print('Tenha um bom dia {}'.format(nome))
