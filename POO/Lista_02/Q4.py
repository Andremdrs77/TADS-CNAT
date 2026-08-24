data = input()

dia, mes, ano = map(int, data.split('/'))

def validarData(dia, mes, ano):
    if mes < 1 or mes > 12:
        return False
    
    if ano < 1900 or ano > 2100:
        return False
    
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia > 31:
            return False
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia > 30:
            return False
    elif mes == 2:
        if dia > 29:
            return False
    return True
    
if validarData(dia, mes, ano):
    print("Data válida")
else:
    print("Data inválida")