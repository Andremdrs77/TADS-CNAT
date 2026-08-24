print("Digite três valores:")

a = int(input())
b = int(input())
c = int(input())

if a <= b and a <= c:
    menor = a
    if b <= c:
        segundo_maior = b
        maior = c
    else:
        segundo_maior = c
        maior = b

elif b <= a and b <= c:
    menor = b
    if a <= c:
        segundo_maior = a
        maior = c
    else:
        segundo_maior = c
        maior = a

else:
    menor = c
    if a <= b:
        segundo_maior = a
        maior = b
    else:
        segundo_maior = b
        maior = a

print(f"{menor}, {segundo_maior}, {maior}")