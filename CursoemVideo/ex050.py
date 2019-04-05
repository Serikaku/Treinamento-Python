soma = 0
cont = 0

for i in range(1, 7):
    x = int(input('Digite o {}º valor: '.format(i)))
    if x % 2 == 0:
        soma += x
        cont += 1
print('Voce informou {} numeros pares e a soma foi {}'.format(cont, soma))
