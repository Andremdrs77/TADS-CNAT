n1, d1, v1 = map(int, input().split())
n2, d2, v2 = map(int, input().split())

if d1 * v2 < d2 * v1:
    print(n1)
else:
    print(n2)