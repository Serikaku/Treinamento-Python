def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um numero
    :param n: O numero a ser calculado
    :param show: (opcional) Mostrar ou nao a conta
    :return: o valor do Fatorial de um numero n
    """
    f = 1
    for i in range(n, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= i
    return f


print(fatorial(5, True))
help(fatorial)
