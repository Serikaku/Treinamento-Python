from datetime import date

x = int(input('Digite um ano (coloque 0 para analisar o ano atual): '))

if x == 0:
    x = date.today().year

if (x % 4) == 0 and x % 100 != 0 or x % 400 == 0:
    print('Ano {} eh bissexto'.format(x))
else:
    print('Ano {} nao eh bissexto'.format(x))