n = int(input())
k = int(input())

notas = [int(input()) for _ in range(n)] #versão beeeeem abreviada de um for que atribui elementos a uma lista

notas.sort(reverse=True)

corte = notas[k - 1]

classificados = 0

for nota in notas:
    if nota >= corte:
        classificados += 1

print(classificados)