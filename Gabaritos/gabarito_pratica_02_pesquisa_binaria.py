'''
Note que para fazer a busca por meio do nome do autor ou preço do livro são necessárias poucas modificações
Linha 11: mudar o índice de 0 para 1 ou 2 (mudar para autor ou preço)
Linha 29: mudar o índice para ordenar com base no autor ou no preço
Linha 33: modificar o nome do livro pelo nome do autor ou preço
'''
# Pesquisa binária para busca por título do livro
def pesquisa_binaria(lista_ordenada, item):
    indice_baixo = 0
    indice_alto = len(lista_ordenada) - 1

    while indice_baixo <= indice_alto:
        indice_meio = (indice_baixo + indice_alto) // 2
        chute = lista_ordenada[indice_meio][0]  # Comparar com o título do livro
        if chute == item:
            return indice_meio
        if chute > item:
            indice_alto = indice_meio - 1
        else:
            indice_baixo = indice_meio + 1
    return None

# Lista de livros
biblioteca = [
    ['1984', 'George Orwell', 30.0, 15],
    ['Percy Jackson', 'Rick Riordan', 35.0, 10],
    ['Cidade dos Etéreos', 'Ransom Riggs', 30.5, 12]
]

# Ordenar a biblioteca pelos títulos dos livros.
biblioteca.sort(key=lambda livro: livro[0])

# Procurar o livro "Percy Jackson"
indice = pesquisa_binaria(biblioteca, 'Percy Jackson')
if indice is not None:
    print(" Livro encontrado ".center(50, '#'))
    print(f'''
        Nome do Livro: {biblioteca[indice][0]}
        Autor: {biblioteca[indice][1]}
        Preço: R${biblioteca[indice][2]}
        Quantidade: {biblioteca[indice][3]}
            ''')
else:
    print("Livro não encontrado!")
