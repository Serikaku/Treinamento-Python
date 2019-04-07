x = int(0)
soma = 0
i = 0
x = int(input('Digite um valor inteiro [999 para parar]: '))
while x != 999:
    soma += x
    i += 1
    x = int(input('Digite um valor inteiro [999 para parar]: '))
print('Foram digitados {} numeros e a soma entre eles foi {}.'.format(i, soma))
