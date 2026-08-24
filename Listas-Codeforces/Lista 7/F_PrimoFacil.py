n = int(input())

if n < 2:
    print("Nao")
else:
    primo = True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            primo = False
            break

    if primo:
        print("Sim")
    else:
        print("Nao")