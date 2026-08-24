d = int(input())
a, l, p = map(int, input().split())

if d <= a and d <= l and d <= p:
    print("S")
else:
    print("N")