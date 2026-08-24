B = int(input())
T = int(input())

area_esquerda = (B + T) * 70

if area_esquerda > 11200:
    print(1)
elif area_esquerda < 11200:
    print(2)
else:
    print(0)