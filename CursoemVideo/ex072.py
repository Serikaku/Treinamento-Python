tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
         'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
         'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    i = int(input('Digite um numero inteiro de zero a vinte: '))
    if 0 <= i <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Voce digitou o numero {tupla[i]}.')
