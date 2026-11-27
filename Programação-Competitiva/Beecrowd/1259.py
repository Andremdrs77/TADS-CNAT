N = int(input())

pares = []
impares = []

for c in range(N):
    n = int(input())

    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

pares.sort()
impares.sort(reverse=True)

for par in pares:
    print(par)
for impar in impares:
    print(impar)

#print('\n'.join(par))
#print('\n'.join(impar))