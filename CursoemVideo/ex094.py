pessoa = dict()
lista = list()
soma = idade = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Por favor digite apenas M ou F')

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    lista.append(pessoa.copy())
    while True:
        cont = str(input('Quer continuar? [S/N] ')).upper()[0]
        if cont in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if cont == 'N':
        break
print(f'Ao todo temos {len(lista)} pessoas cadastradas')
print(f'A media de idade e de {soma / len(lista):.2f} anos')
print(f'As mulheres cadastradas foram ', end='')
for i in lista:
    if i['sexo'] == 'F':
        print(i['nome'], end=' ')
print()
print('Lista das pessoas que estao acima da media: ', end='')
for i in lista:
    if i['idade'] >= soma / len(lista):
        print(i['nome'], end=' ')
