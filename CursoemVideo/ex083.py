lista = []

expr = str(input('Digite uma expressao: '))

for simb in expr:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista)>0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) == 0:
    print('Expressao correta')
else:
    print('Expressao errada')
