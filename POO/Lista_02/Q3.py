num = []

for c in range(4):
    num.append(int(input()))
    if num[c] in num[:c]:
        print("ERRO: Número repetido. Digite outro número.")
        break
    
maior = max(num)
menor = min(num)
soma = sum(num) - maior - menor

print(f"""
Maior valor = {maior}
Menor valor = {menor}
A soma do segundo maior valor com o segundo menor = {soma}""")