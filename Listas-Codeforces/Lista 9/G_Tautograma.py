while True:
    frase = input().strip()

    if frase == "*":
        break

    palavras = frase.split()
    inicial = palavras[0][0].lower()

    tautograma = True

    for palavra in palavras:
        if palavra[0].lower() != inicial:
            tautograma = False
            break

    print("Y" if tautograma else "N")