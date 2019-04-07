soma = 0
i = 0
continua = 0
while continua == 0:
    x = int(input('Digite um valor inteiro: '))
    soma += x
    i += 1
    if i == 1:
        maior = x
        menor = x
    else:
        if x > maior:
            maior = x
        if x < menor:
            menor = x
    resposta = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if 'N' in resposta:
        continua = 1
media = soma / i
print('Voce digitou {} numero e a media entre eles eh {}'.format(i, media))
print('O maior valor foi {} e o menor {}'.format(maior, menor))