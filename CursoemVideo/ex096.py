def area(x, y):
    area = x * y
    print(f'A area de um terreno{x:.1f}x{y:.1f} e de {area:.1f}m²')


print('  Controle de Terrenos')
print('-' * 20)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
