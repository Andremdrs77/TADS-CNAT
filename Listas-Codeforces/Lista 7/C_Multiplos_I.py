a, b = map(int, input().split())

for n in range(1, b + 1):
    if (a * n) <= b:
        print(a * n, end=' ')
    else:
        break