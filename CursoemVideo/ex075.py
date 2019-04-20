tupla = (int(input('Digite o primeiro valor: ')),
         int(input('Digite o segundo valor: ')),
         int(input('Digite o terceiro valor: ')),
         int(input('Digite o quarto valor: ')))
print(f'Voce digitou os valores {tupla}')
print(f'O numero 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O numero 3 foi digitado pela primeira vez na {tupla.index(3)+1}ª posicao')
else:
    print(f'O numero 3 nao foi digitado nenhuma vez')

print('Os numero pares foram: ', end='')
for c in tupla:
    if c % 2 == 0:
        print(f'{c} ', end='')
