N = int(input())

seq = [int(input()) for i in range(N)]

ultimo = 0
resposta = 0

for x in seq:
    if x != ultimo:
        resposta += 1
        ultimo = x

print(resposta)