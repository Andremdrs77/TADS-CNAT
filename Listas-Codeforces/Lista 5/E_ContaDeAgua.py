N = int(input())

if N <= 10:
    print(7)
if N > 10 and N <= 30:
    print(7 + (N - 10))
if N > 30 and N <= 100:
    print(7 + 20 + (N - 30) * 2)
if N > 100:
    print(7 + 20 + 140 + (N - 100) * 5)
    