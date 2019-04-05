from datetime import date

maior = 0
menor = 0

ano = date.today().year

for i in range(0, 7):
    nas = int(input('Digite o ano de nascimento de alguem: '))
    if ano-nas < 21:
        menor += 1
    else:
        maior += 1

print('Dessas pessoas, {} ja sao maiores e {} ainda nao atingiram a maioridade'.format(maior, menor))
