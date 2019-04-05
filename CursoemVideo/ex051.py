primeiro = int(input('Digite o primeiro termo da progressao aritmetica: '))
razao = int(input('Digite a razao da progressao aritmetica: '))
decimo = primeiro + 10 * razao

for i in range(primeiro, decimo, razao):
    print('{} → '.format(i), end='')
print('Acabou')