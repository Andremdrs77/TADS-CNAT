C = int(input())
D = int(input())
T = int(input())

necessario = D / C
compra = necessario - T

if compra < 0:
    compra = 0

print(f"{compra:.1f}")