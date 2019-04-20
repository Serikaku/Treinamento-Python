lista = []
maior = menor = 0

for i in range(0, 5):
    lista.append(int(input(f'Digite o valor na posicao {i}: ')))
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]
print(f'Voce digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posicoes ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi {menor} nas posicoes ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end='')
