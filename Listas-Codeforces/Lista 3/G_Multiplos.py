a = int(input())
b = int(input())

maior = max(a, b)
menor = min(a, b)

if maior % menor == 0:
    print("Multiplos")
else:
    print("Nao multiplos")