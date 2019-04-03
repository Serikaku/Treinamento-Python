x = float(input('Digite a primeira nota: '))
y = float(input('Digite a segunda nota: '))

media = (x + y) / 2

print('Media: {:.1f}'.format(media))
if media < 5:
    print('\033[31mReprovado\033[m!')
elif media >= 7:
    print('Aprovado')
else:
    print('Recuperacao')
