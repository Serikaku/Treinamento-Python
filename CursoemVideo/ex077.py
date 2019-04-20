lista = ('mercado', 'olar', 'josefina', 'python',
         'curso', 'gratis', 'estudar', 'praticar',
         'trabalhar', 'mercado', 'programador')

for i in lista:
    print(f'\nNa palavra {i} temos ', end='')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
