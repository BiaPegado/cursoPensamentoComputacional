def pesquisa_binaria(lista_ordenada, item):
    baixo = 0
    alto = len(lista_ordenada)-1
    while baixo <= alto:
        meio = (baixo+alto)//2
        chute = lista_ordenada[meio]
        if(chute == item):
            return meio
        if(chute > item):
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

lista_ordenada = [0, 2, 4, 6, 8, 10]
print(pesquisa_binaria(lista_ordenada, 9))  #None
print(pesquisa_binaria(lista_ordenada, 0))  #0
print(pesquisa_binaria(lista_ordenada, 8))  #4
print(pesquisa_binaria(lista_ordenada, 1))  #None