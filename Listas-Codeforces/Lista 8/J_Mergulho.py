N, R = map(int, input().split())

voltaram = list(map(int, input().split()))

faltaram = []

for i in range(1, N + 1):
    if i not in voltaram:
        faltaram.append(i)

if len(faltaram) == 0:
    print("*")
else:
    for pessoa in faltaram:
        print(pessoa, end=" ")