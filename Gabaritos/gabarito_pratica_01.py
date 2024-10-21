
# Adiciona livro à biblioteca
def adicionar_livro(nome: str, autor: str, preco: float, qtd: int, biblioteca: dict):
    biblioteca[nome] = [autor, preco, qtd]

# Lista livros disponíveis
def listar_livros(biblioteca: dict):
    print(" Listando livros ".center(50, '#'))
    for key in biblioteca:
        texto = f'''
            Nome do Livro: {key}
            Autor: {biblioteca[key][0]}
            Preço: R${biblioteca[key][1]}
            Quantidade: {biblioteca[key][2]}
              '''
        print(texto)
    print("".center(50, '#'))

# Remove um livro por meio do nome
def remover_livro(nome: str, biblioteca: dict):
    del biblioteca[nome]

# Dicionário de listas
biblioteca = {
    '1984': ['George Orwell', 30.0, 15],
    'Percy Jackson' : ['Rick Riordan', 35.0, 10]
    }
    
# Adicionando, removendo e listando livros
adicionar_livro('Cidade dos Etéreos', 'Ransom Riggs', 30.5, 12, biblioteca)
remover_livro('1984', biblioteca)
listar_livros(biblioteca)
