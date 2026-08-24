a11, a21 = map(int, input().split())
a12, a22 = map(int, input().split())
p1, p2 = map(int, input().split())

soma_pesos = p1 + p2

m1 = (a11 * p1 + a21 * p2) // soma_pesos
m2 = (a12 * p1 + a22 * p2) // soma_pesos

if m1 >= m2:
    print(1)
else:
    print(2)