from time import sleep


def contador(x, y, z):
    if z < 0:
        z = z * -1
    elif z == 0:
        z = 1
    print(f'Contagem de {x} ate {y} de {z} em {z}')
    if x < y:
        for j in range(x, y + 1, z):
            print(f'{j} ', end='')
            sleep(0.25)
    else:
        for j in range(x, y - 1, -z):
            print(f'{j} ', end='')
            sleep(0.25)
    print('FIM')
    print('-' * 40)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora e sua vez de personalizar a contagem')
i = int(input('Inicio: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contador(i, f, p)
