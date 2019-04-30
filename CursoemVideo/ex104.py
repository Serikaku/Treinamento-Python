def leiaInt(texto):
    while True:
        x = str(input(texto))
        if x.isnumeric():
            x = int(x)
            return x
        else:
            print('\033[0;31mERRO! Digite um numero inteiro valido.\033[m')


n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')
