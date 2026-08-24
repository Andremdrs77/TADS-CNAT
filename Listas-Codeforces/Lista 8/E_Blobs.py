N = int(input())

Ci = list()

for inputs in range(0, N):
    Ci.append(float(input()))

for qtd in Ci:
    n = qtd
    cont = 0
    
    while n > 1:
        n = n / 2
        cont += 1
        
    print(f'{cont} dias')