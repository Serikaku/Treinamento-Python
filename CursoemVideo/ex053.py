frase = str(input('Digite uma frase para verificar se ela eh um palindromo: ')).strip().upper()

lista = frase.split()
junto = ''.join(lista)
inverso = ''

for i in range(len(junto)-1, -1, -1):
    inverso += junto[i]

if inverso == junto:
    print('Temos um palindromo')
else:
    print('A frase digitada nao eh um palindromo')

