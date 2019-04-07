primeiro = int(input('Digite o primeiro termo da progressao aritmetica: '))
razao = int(input('Digite a razao da progressao aritmetica: '))

i = 0
while i < 10:
    print('{} → '.format(primeiro + razao * i), end='')
    i += 1
print('Acabou')
