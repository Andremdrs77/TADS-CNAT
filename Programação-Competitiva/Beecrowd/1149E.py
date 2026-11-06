valores = list(map(int, input().split()))
A = valores[0]

for valor in valores[1:]:
    if valor > 0:
        N = valor

for i in range(N):
    if i > 0:
        A = A + A + i

print(A)