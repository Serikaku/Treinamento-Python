from time import sleep


def maior(* n):
    print('-' * 30)
    tam = len(n)
    big = 0
    print('Analisando os valores passados...')
    for i in n:
        if big == 0 or i > big:
            big = i
        print(f'{i} ', end='')
        sleep(0.25)
    print(f'Foram informados {tam} valores ao todo')
    print(f'O maior valor informado foi {big}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
