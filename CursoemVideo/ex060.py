x = int(input('Digite um valor: '))
print('{}! = '.format(x), end='')
fatorial = 1

while x != 1:
    print(x, end=' x ')
    fatorial *= x
    x -= 1
print("1 = {}".format(fatorial))
