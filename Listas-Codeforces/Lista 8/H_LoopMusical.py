while True:
    N = int(input())
    
    if N == 0:
        break
    
    H = list(map(int, input().split()))
    
    picos = 0
    
    for i in range(N):
        atual = H[i]
        
        if i == 0:
            anterior = H[N - 1]
            proximo = H[1]
        elif i == N - 1:
            anterior = H[N - 2]
            proximo = H[0]
        else:
            anterior = H[i - 1]
            proximo = H[i + 1]

        if (atual > anterior and atual > proximo) or (atual < anterior and atual < proximo):
            picos += 1
    
    print(picos)