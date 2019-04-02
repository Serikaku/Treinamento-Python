frase = str(input('Digite uma frase: ')).strip()

print('A letra a aparece {} vezes na frase'.format(frase.lower().count('a')))
print('A letra a aparece pela primeira vez na posicao {}'.format(frase.lower().find('a')+1))
print('A letra a aparece pela ultima vez na posicao {}'.format(frase.lower().rfind('a')+1))
