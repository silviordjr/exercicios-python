def remove_repetidos(lista):
    lista.sort()
    lista_suporte = []
    for i in range(0, len(lista)):
        if lista[i] != lista[i-1]:
            lista_suporte.append(lista[i])
    return lista_suporte
