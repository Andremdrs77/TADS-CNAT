N = int(input())
strings = []

for c in range(N):
    strings.append(list(map(str, input().split())))

for string in strings:
    string.sort(key=len, reverse=True)
    print(*string)