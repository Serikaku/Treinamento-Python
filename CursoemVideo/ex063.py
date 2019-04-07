print('Sequencia de Fibonacci')

x = int(input('Digite quantos valores da sequencia deseja exibir: '))

m = 0
n = 1
a = 0
i = 0

while i < x:
    print(m, end='')
    a = m
    m = n
    n = n + a
    i += 1
    if i < x:
        print(' → ', end='')
