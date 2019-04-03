from datetime import date

x = int(input('Digite seu ano de nascimento: '))
y = date.today().year
idade = y - x
print('Quem nasceu em {} tem {} anos em {}'.format(x, idade, y))
if idade < 18:
    print('Ainda faltam {} anos para o alistamento no servico militar'. format(18 - idade))
    print('Seu alistamento sera em {}'.format(x+18))
elif idade == 18:
    print('Esta na hora de se alistar')
else:
    if idade-18 == 1:
        print('Ja passou {} ano do tempo de alistamento'.format(idade - 18))
    else:
        print('Ja passaram {} anos do tempo de alistamento'.format(idade-18))
    print('Seu alistamento foi em {}'.format(x+18))
