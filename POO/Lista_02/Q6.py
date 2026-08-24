i = int(input())
f = int(input())

cont = 0
for c in range(i, f + 1):
    if cont % 2 == 0:
        print(c)
    else:
        print(-c)
    cont += 1