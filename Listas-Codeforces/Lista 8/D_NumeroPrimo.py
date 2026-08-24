n = int(input())
nv = max(2, n + 1)

while True:
    primo = True
    
    for i in range(2, int(nv ** 0.5) + 1):
        if nv % i == 0:
            primo = False
            break
    if primo:
        print(nv)
        break
        
    nv += 1