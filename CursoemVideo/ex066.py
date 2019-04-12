i = soma = 0
while True:
    n = int(input('Digite um numero (999 para parar): '))
    if n == 999:
        break
    soma += n
    i += 1
print(f'A soma dos {i} valores foi {soma}')
