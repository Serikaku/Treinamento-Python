from time import sleep
c = ('\033[m',          # 0 - sem cores
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7;30m',   # 6 - branco
     )


def titulo(texto, cor=0):
    print(c[cor], end='')
    print('-' * (len(texto)+4))
    print(f'  {texto}')
    print('-' * (len(texto)+4))
    print(c[0], end='')
    sleep(1)


def PyHELP():
    while True:
        titulo('Sistema de Ajuda PyHELP', 2)
        x = str(input('Funcao ou Biblioteca > ')).strip()
        if x.upper() == 'FIM':
            titulo('Ate logo!', 1)
            break
        titulo(f'Acessando o manual do comando \'{x}\'', 4)
        print(c[6], end='')
        help(x)
        print(c[0], end='')
        sleep(2)


PyHELP()
