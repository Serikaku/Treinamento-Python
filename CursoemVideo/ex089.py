boletim = []
linha = '-'*22

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    cont = str(input('Deseja continuar? [S/N] '))
    if cont in 'Nn':
        break
print(linha)

print(f'{"No.":<4}{"Nome":<10}{"Media":>8}')
print(linha)
for i in range(0, len(boletim)):
    print(f'{i:<4}{boletim[i][0]:<10}{boletim[i][2]:>8.1f}')

while True:
    x = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if x == 999:
        break
    print(f'As notas de {boletim[x][0]} sao [{boletim[x][1]}]')
    print(linha)
