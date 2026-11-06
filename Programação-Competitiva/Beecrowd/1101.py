while True:
    M, N = map(int, (input().split()))
    
    if M <= 0 or N <= 0:
        break
    
    Sum = 0
    
    for c in range (min(M, N), max(M, N) + 1):
        Sum += c
        
        print(c, end=' ')
    
    print(f'Sum={Sum}')