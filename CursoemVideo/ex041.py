from datetime import date

ano = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - ano
print('Categoria: ')
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 25:
    print('Senior')
else:
    print('Master')
