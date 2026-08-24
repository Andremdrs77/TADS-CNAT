J, R = map(int, input().split())

rodadas = list(map(int, input().split()))
pontuacoes = [0] * J

cont = 0

for pontuacao_rodada in rodadas:
    pontuacoes[cont] += pontuacao_rodada
    
    cont += 1
    if cont == J:
        cont = 0
    
maior = max(pontuacoes)

vencedor = J - pontuacoes[::-1].index(maior)

print(vencedor)
