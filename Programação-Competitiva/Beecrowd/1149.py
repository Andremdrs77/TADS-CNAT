valores = list(map(int, input().split()))

A = valores[0]
aux = A

for valor in valores[1:]:
    if valor > 0:
        N = valor
        break
    
for c in range(N):
    if c == 0:
        A = A
    else:
        A = A + (aux + c)
        
print(A)