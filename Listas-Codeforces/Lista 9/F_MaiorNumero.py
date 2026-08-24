def raiz_digital(s):
    if s == "0":
        return 0

    soma = 0
    for c in s:
        soma += int(c)

    return 1 + (soma - 1) % 9


while True:
    n, m = input().split()

    if n == "0" and m == "0":
        break

    rn = raiz_digital(n)
    rm = raiz_digital(m)

    if rn > rm:
        print(1)
    elif rm > rn:
        print(2)
    else:
        print(0)