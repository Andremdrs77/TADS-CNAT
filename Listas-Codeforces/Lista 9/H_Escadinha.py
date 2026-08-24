n = int(input())
v = list(map(int, input().split()))

if n <= 2:
    print(1)
else:
    qtd = 1
    diff = v[1] - v[0]

    for i in range(2, n):
        novo_diff = v[i] - v[i - 1]

        if novo_diff != diff:
            qtd += 1
            diff = novo_diff

    print(qtd)