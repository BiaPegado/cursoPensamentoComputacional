def pesquisa_binaria(lista_ordenada, item):
    indice_baixo = 0
    indice_alto = len(lista_ordenada)-1
    while indice_baixo <= indice_alto:
        indice_meio = (indice_baixo+indice_alto)//2
        chute = lista_ordenada[indice_meio]
        if(chute == item):
            return indice_meio
        if(chute > item):
            indice_alto = indice_meio - 1
        else:
            indice_baixo = indice_meio + 1
    return None

lista_ordenada = [0, 2, 4, 6, 8, 10]
print(pesquisa_binaria(lista_ordenada, 9))  #None
print(pesquisa_binaria(lista_ordenada, 0))  #0
print(pesquisa_binaria(lista_ordenada, 8))  #4
print(pesquisa_binaria(lista_ordenada, 1))  #None
