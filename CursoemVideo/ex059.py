from time import sleep

x = float(input('Primeiro valor: '))
y = float(input('Segundo valor: '))

menu = int(0)

while menu != 5:
    print('''Opcoes:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa''')
    menu = int(input('Qual a opcao desejada? '))
    if menu == 1:
        print('{} + {} = {:.2f}'.format(x, y, x + y))

    elif menu == 2:
        print('{} x {} = {:.2f}'.format(x, y, x * y))

    elif menu == 3:
        if x > y:
            print('{} > {}'.format(x, y))
        else:
            print('{} > {}'.format(y, x))

    elif menu == 4:
        print('Digite os novos valores: ')
        x = float(input('Primeiro valor: '))
        y = float(input('Segundo valor: '))

    else:
        print('Opcao invalida.')
    sleep(2)
print('Fim do programa')
