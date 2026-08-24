def lista_troca_menor_primeiro(lista):
    trocas = 0
    ListaSort = sorted(lista)

    if lista[0] != ListaSort[0]:
        temp = lista[0]

        indice_menor = lista.index(ListaSort[0])

        lista[0] = ListaSort[0]
        lista[indice_menor] = temp

        trocas += 1

    return trocas