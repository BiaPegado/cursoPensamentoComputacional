# Busca livro pelo nome
def buscar_livro_por_nome(nome: str, biblioteca: dict):
    if biblioteca.get(nome):
        print(" Livro encontrado ".center(50, '#'))
        print(f'''
            Nome do Livro: {nome}
            Autor: {biblioteca[nome][0]}
            Preço: R${biblioteca[nome][1]}
            Quantidade: {biblioteca[nome][2]}
              ''')
    else:
        print(f"{nome} não foi encontrado!\n")

# Busca livros pelo nome do autor
def buscar_livro_por_autor(autor: str, biblioteca: dict):
    print(f" Livros de {autor} ".center(50, '#'))
    for key in biblioteca:
        if biblioteca[key][0] == autor:
            print(f'''
            Nome do Livro: {key}
            Autor: {biblioteca[key][0]}
            Preço: R${biblioteca[key][1]}
            Quantidade: {biblioteca[key][2]}
              ''')

# Busca livros mais baratos que o preço máximo        
def buscar_livro_por_preco(preco_maximo: float, biblioteca: dict):
    print(f" Livros de até R${preco_maximo} ".center(50, '#'))
    for key in biblioteca:
        if biblioteca[key][1] <= preco_maximo:
            print(f'''
            Nome do Livro: {key}
            Autor: {biblioteca[key][0]}
            Preço: R${biblioteca[key][1]}
            Quantidade: {biblioteca[key][2]}
              ''')
    
            
# Código da prática 01
# Adiciona livro à biblioteca
def adicionar_livro(nome: str, autor: str, preco: float, qtd: int, biblioteca: dict):
    biblioteca[nome] = [autor, preco, qtd]

# Dicionário de listas
biblioteca = {
    '1984': ['George Orwell', 30.0, 15],
    'Percy Jackson' : ['Rick Riordan', 35.0, 10]
    }
    
# Adicionando, removendo e listando livros
adicionar_livro('Cidade dos Etéreos', 'Ransom Riggs', 30.5, 12, biblioteca)
buscar_livro_por_nome('1984', biblioteca)
buscar_livro_por_nome('O orfanato da Srta. Peregrine', biblioteca)
buscar_livro_por_autor('Rick Riordan', biblioteca)
buscar_livro_por_preco(32, biblioteca)

