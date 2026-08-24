n = int(input())

for d in range(1, n + 1):
    if n % d == 0:
        print(d, end=' ')
