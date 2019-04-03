valor = float(input('Qual o valor do imovel? R$'))
salario = float(input('Qual o seu salario? R$'))
anos = int(input('Em quantos anos quer financiar? '))

prestacao = valor/(anos*12)

print('Para pagar uma casa de R${:.2f} em {} anos, o valor da prestacao mensal sera de R${:.2f}'.format(valor, anos, prestacao))

if prestacao > salario * 0.3:
    print('Emprestimo negado')
else:
    print('Emprestimo pode ser concedido')
