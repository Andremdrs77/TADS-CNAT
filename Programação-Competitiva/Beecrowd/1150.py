X  = int(input())
    
while True:
    Z = int(input())
    
    if Z > X:
        break
    
seq = 1
soma = X
prox = X
    
while True:
    soma += prox
    seq += 1
    prox += 1
    
    if soma > Z:
        break
        
print(seq)