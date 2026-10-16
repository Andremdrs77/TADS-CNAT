x, y, z = map(int, input().split())

numeros = [x, y, z]
numeros.sort()

print(*numeros, sep="\n")

print()

print(x)
print(y)
print(z)