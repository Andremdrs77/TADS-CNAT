def dia_da_semana(h, d):
    dias = ('Domingo', 'Segunda-feira', 'Terca-feira', 
    'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado')

    index = dias.index(h)
    return dias[(index + d) % 7]
    