N = int(input())

sapos = 0
coelhos = 0
ratos = 0

for c in range(N):
    qtd, tipo = input().split()
    qtd = int(qtd)

    if tipo == 'C':
        coelhos += qtd
    elif tipo == 'R':
        ratos += qtd
    else:
        sapos += qtd

total = sapos + coelhos + ratos

print(f"""Total: {total} cobaias
Total de coelhos: {coelhos}
Total de ratos: {ratos}
Total de sapos: {sapos}
Percentual de coelhos: {(coelhos * 100/total):.2f} %
Percentual de ratos: {(ratos * 100/total):.2f} %
Percentual de sapos: {(sapos * 100/total):.2f} %""")

