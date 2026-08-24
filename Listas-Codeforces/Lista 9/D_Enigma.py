mensagem = input().strip()
crib = input().strip()

n = len(mensagem)
m = len(crib)

resposta = 0

for i in range(n - m + 1):
    valido = True

    for j in range(m):
        if mensagem[i + j] == crib[j]:
            valido = False
            break

    if valido:
        resposta += 1

print(resposta)