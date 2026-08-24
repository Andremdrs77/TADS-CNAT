P, N = map(int, input().split())
Ni = list(map(int, input().split()))

for i in range(1, N):
    if Ni[i] - Ni[i - 1] > P or Ni[i - 1] - Ni[i] > P:
        print("GAME OVER")
        break
else:
    print("YOU WIN")

