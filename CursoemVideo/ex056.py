nomevelho = ''
velho = 0
media = 0
mulheres = 0

for i in range(0, 4):
    nome = str(input('Digite o nome da pessoa {}: '.format(i+1)))
    idade = int(input('Digite a idade da pessoa {}: '.format(i+1)))
    sexo = int(input('''Selecione o sexo da pessoa
    [ 1 ] Feminino
    [ 2 ] Masculino
    '''))
    media += idade
    if sexo == 2 and idade > velho:
        velho = idade
        nomevelho = nome
    if sexo == 1 and idade < 20:
        mulheres += 1

media = media / 4

print('A media de idade do grupo eh {}'.format(media))
print('O nome do homem mais velho eh {} e ele tem {} anos'.format(nomevelho, velho))
print('{} mulheres tem menos de 20 anos'.format(mulheres))
