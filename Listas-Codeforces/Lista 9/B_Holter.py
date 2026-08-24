N = int(input())

B = list()

for c in range(N):
    B.append(int(input()))

media = sum(B) // N

print(media)

limite_inferior = media * 90 // 100
limite_superior = media * 110 // 100

cont = 0

for batimento in B:
    if batimento < limite_inferior or batimento > limite_superior:
        cont += 1

print(cont)