print("Digite uma frase:")
frase = list(map(str, input().split()))
tamanho = len(frase)

print('')

for i in range(tamanho):
    print(*frase)
    frase.pop()
