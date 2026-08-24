N = int(input())

I = list(map(int, input().split()))

A = False
B = False

for click in I:
    if click == 1:
        A = not(A)
    elif click == 2:
        A = not(A)
        B = not(B)
        
if A:
    print(1)
else:
    print(0)
    
if B:
    print(1)
else:
    print(0)