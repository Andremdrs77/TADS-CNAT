def sublista_sem_menor(lista):
    nova_lista = lista.copy()
    
    nova_lista.pop(nova_lista.index(min(nova_lista)))
    
    return nova_lista