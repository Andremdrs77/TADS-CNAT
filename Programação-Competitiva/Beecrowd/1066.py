pares = 0
impares = 0
positivos = 0
negativos = 0


for c in range(5):
    num = int(input())
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
        
    if (num % 2) == 0:
        pares += 1
    else:
        impares += 1
    
print(f"""{pares} valor(es) par(es)
{impares} valor(es) impar(es)
{positivos} valor(es) positivo(s)
{negativos} valor(es) negativo(s)""")