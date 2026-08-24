N = int(input())
Ai = list(map(int, input().split()))

media = sum(Ai) / N
print(f'{media:.1f}')

acimaOuIgual = list()
abaixo = list()

for numero in Ai:
    if numero >= media:
        acimaOuIgual.append(numero)
    else:
        abaixo.append(numero)
        
print(len(abaixo), *abaixo)
print(len(acimaOuIgual), *acimaOuIgual)