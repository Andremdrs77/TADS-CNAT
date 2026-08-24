n = int(input())
s = input().strip()

resp = 0
i = 0

while i < n:
    j = i

    while j < n and s[j] == s[i]:
        j += 1

    tamanho = j - i

    if s[i] == 'a' and tamanho >= 2:
        resp += tamanho

    i = j

print(resp)