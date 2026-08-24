A, B, C, D = map(int, input().split())

if A + B > C and A + C > B and B + C > A:
    print('S')
elif A + B > D and A + D > B and B + D > A:
    print('S')
elif A + C > D and A + D > C and C + D > A:
    print('S')
elif B + C > D and B + D > C and C + D > B:
    print('S')
else:
    print('N')