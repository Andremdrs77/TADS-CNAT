s, m = map(int, input().split())

Ts = 0

while m >= 0.5:
    m = m / 2
    Ts += s

print(f'{Ts // 86400} dias {Ts % 86400 // 3600:02d}:{Ts % 3600 // 60:02d}:{Ts % 60:02d}')