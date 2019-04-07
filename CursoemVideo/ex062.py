primeiro = int(input('Digite o primeiro termo da progressao aritmetica: '))
razao = int(input('Digite a razao da progressao aritmetica: '))

i = 0
mais = 1
termos = int(10)
while mais != 0:
    while i < termos:
        print('{} → '.format(primeiro + razao * i), end='')
        i += 1
    print('Pausa')
    mais = int(input('Deseja mostrar mais quantos termos? '))
    termos = termos + mais
print('Progressao finalizada com {} termos mostrados.'.format(termos))
