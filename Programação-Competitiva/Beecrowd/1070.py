X = int(input())

impares = []

while not len(impares) == 6:
    if X % 2 != 0:
        impares.append(X)
    X += 1
    
print(*impares, sep="\n")