T = int(input())

for c in range(T):
    D, N = map(int, input().split())
    precos = list(map(float, input().split()))
    
    maior_troco = 0.0
    
    for preco in precos:
        qtd = int(D // preco)

        if qtd >= 1:
            troco = D - qtd * preco
            maior_troco = max(maior_troco, troco)
            
    print(f'{maior_troco:.2f}')