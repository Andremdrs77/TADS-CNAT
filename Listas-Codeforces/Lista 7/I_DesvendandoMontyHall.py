n = int(input())

ganhos = 0

for i in range(n):
    porta = int(input())
    if porta != 1:
        ganhos += 1

print(ganhos)