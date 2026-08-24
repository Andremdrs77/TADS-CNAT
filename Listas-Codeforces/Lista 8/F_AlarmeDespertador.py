while True:
    H1, M1, H2, M2 = map(int, input().split())

    if H1 == 0 and H2 == 0 and M1 == 0 and M2 == 0:
        break

    atual = H1 * 60 + M1
    alarme = H2 * 60 + M2

    minutos = (alarme - atual) % (24 * 60)

    print(minutos)