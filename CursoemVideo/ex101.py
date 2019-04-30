def voto(x):
    from datetime import date
    idade = date.today().year - x
    if idade < 16:
        return f'Com {idade} anos: NAO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO'


ano = int(input('Em que ano voce nasceu? '))
print(voto(ano))
