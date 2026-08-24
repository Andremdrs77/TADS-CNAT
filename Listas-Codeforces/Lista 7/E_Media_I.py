N = int(input())
Ai = list(map(int, input().split()))

media = sum(Ai) / N
print(f'{media:.1f}')

acimaOuIgual = 0
abaixo = 0

for numero in Ai:
    if numero >= media:
        acimaOuIgual += 1
    else:
        abaixo += 1
        
print(abaixo)
print(acimaOuIgual)