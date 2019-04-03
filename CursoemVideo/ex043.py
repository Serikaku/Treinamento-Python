peso = float(input('Digite seu peso: (kg) '))
altura = float(input('Digite sua altura: (m) '))

imc = peso / (altura**2)
print('Seu IMC eh {:.1f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade Morbida')
