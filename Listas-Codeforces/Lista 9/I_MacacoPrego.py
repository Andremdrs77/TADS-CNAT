teste = 1

while True:
    n = int(input())

    if n == 0:
        break

    esq, topo, dir, base = map(int, input().split())

    for _ in range(n - 1):
        x, y, u, v = map(int, input().split())

        esq = max(esq, x)
        topo = min(topo, y)
        dir = min(dir, u)
        base = max(base, v)

    print(f"Teste {teste}")

    if esq <= dir and base <= topo:
        print(esq, topo, dir, base)
    else:
        print("nenhum")

    print()

    teste += 1