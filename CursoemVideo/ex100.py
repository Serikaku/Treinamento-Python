from random import randint
from time import sleep
numeros = list()


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        lista.append(randint(0, 10))
        print(numeros[i], end=' ')
        sleep(0.25)
    print('Pronto')


def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {lista}, temos {soma}')


sorteia(numeros)
somaPar(numeros)
