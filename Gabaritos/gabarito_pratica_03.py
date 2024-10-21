
def adicionar_livro_carrinho(nome, carrinho, biblioteca):
    if biblioteca.get(nome):
        carrinho.append([nome, biblioteca[nome][1]])
        print(f"{nome} foi adicionado ao carrinho!")
    else:
        print("Livro não disponível!")

def remover_livro_carrinho(nome, carrinho, biblioteca):
    carrinho.remove([nome, biblioteca[nome][1]])
    print(f"{nome} foi removido do carrinho!")

# Calculando soma dos preços dos livros no carrinho por meio de recursão
def calcular_total(carrinho):
    # Caso base: se o carrinho estiver vazio, retorna 0
    if not carrinho:
        return 0
    # Soma o preço do primeiro livro ao total da recursão dos livros restantes
    return carrinho[0][1] + calcular_total(carrinho[1:])

# Dicionário de listas
biblioteca = {
    '1984': ['George Orwell', 30.0, 15],
    'Percy Jackson' : ['Rick Riordan', 35.0, 10],
    'Cidade dos Etéreos': ['Ransom Riggs', 30.5, 12]
    }

# Carrinho de compras. Deve conter [nome, preço]
carrinho = []

adicionar_livro_carrinho('1984', carrinho, biblioteca)
adicionar_livro_carrinho('1984', carrinho, biblioteca)
adicionar_livro_carrinho('Percy Jackson', carrinho, biblioteca)
adicionar_livro_carrinho('Cidade dos Etéreos', carrinho, biblioteca)

remover_livro_carrinho('1984', carrinho, biblioteca)

print(f"Total: {calcular_total(carrinho)}")
