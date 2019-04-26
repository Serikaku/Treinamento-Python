from datetime import date
ano = date.today().year
pessoa = dict()

pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = ano - int(input('Ano de nascimento: '))
pessoa['ctps'] = int(input('Carteira de trabalho (0 nao tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Ano de contratacao: '))
    pessoa['salario'] = float(input('Salario: R$'))
    pessoa['aposentadoria'] = (pessoa['contratacao'] + 35 - ano) + pessoa['idade']
print('-' * 30)
for c, v in pessoa.items():
    print(f'  - {c} tem o valor {v}')
