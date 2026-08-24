A, B, C = map(int, input().split())

a, b, c = sorted([A, B, C])

if a + b <= c:
    print('n')
else:
    if a*a + b*b == c*c:
        print('r')
    elif a*a + b*b > c*c:
        print('a')
    else:
        print('o')