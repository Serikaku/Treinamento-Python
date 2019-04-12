from random import randint

vitoria = 0
print('Par ou impar')
print('-'*20)

while True:
    pc = randint(0, 5)
    #print(pc)
    n = int(input('Digite um valor: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Impar? [P/I] ')).strip().upper()
    print('-'*20)
    resultado = "Par" if (n+pc)%2 == 0 else "Impar"
    print(f'Voce jogou {n} e o computador {pc}. Total de {n+pc} deu {resultado}')
    if escolha in resultado[0]:
        print('Voce venceu. \nVamos jogar novamente...')
        print('-'*20)
        vitoria += 1
    else:
        print('Voce perdeu')
        break
print(f'Voce venceu {vitoria} vezes.')
