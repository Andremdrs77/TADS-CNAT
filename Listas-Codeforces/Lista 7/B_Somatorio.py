n = int(input())
s = 0

for x in range(1, n + 1):
    s += 1/x
    
print(f"{s:.4f}")