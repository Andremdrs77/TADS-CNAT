A, N = map(int, input().split())

while not N > 0:
    N = int(input())

for i in range(N):
    A = A + i

print(A)