C = int(input())

saldo = 100
maior_premio = 100

for i in range (1, C + 1):
    V = int(input())
    saldo += V
    
    if saldo > maior_premio:
        maior_premio = saldo
        
print(maior_premio)