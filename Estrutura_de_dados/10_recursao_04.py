def pesquisa_binaria(lista_ordenada, indice_baixo, indice_alto, item):
    meio = (indice_baixo + indice_alto) // 2

    if indice_baixo > indice_alto:
        return None
    if lista_ordenada[meio] == item:
        return meio
    elif lista_ordenada[meio] > item:
        return pesquisa_binaria(lista_ordenada, indice_baixo, meio - 1, item)
    else:
        return pesquisa_binaria(lista_ordenada, meio + 1, indice_alto, item)
    
lista_ordenada = [0, 2, 4, 6, 8, 10]
print(pesquisa_binaria(lista_ordenada, 0, len(lista_ordenada)-1, 8))
