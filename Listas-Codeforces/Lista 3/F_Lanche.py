c, q = map(int, input().split())

precos = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}

total = precos[c] * q

print(f"Total: R$ {total:.2f}")