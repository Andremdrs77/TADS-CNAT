caso = 1

while True:
    try:
        N = int(input())

        valores = list(map(float, input().split()))

        teclas = []

        for i in range(10):
            teclas.append((i, valores[i]))

        teclas.sort(key=lambda x: (-x[1], x[0]))
        #sei que lambda parece muito avançado (por enquanto), mas só usei pq já tenho bastante experiência com python
        senha = ""

        for i in range(N):
            senha += str(teclas[i][0])

        print(f"Caso {caso}: {senha}")

        caso += 1

    except EOFError:
        break