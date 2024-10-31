inventario = {}

# Adiciona itens ao inventário
def adicionar_item(item, quantidade):
    if item in inventario:
        inventario[item] += quantidade
    else:
        inventario[item] = quantidade

# Remove itens do inventário
def remover_item(item, quantidade):
    if item in inventario and inventario[item] >= quantidade:
        inventario[item] -= quantidade
        if inventario[item] == 0:
            del inventario[item]

# Lista itens e quantidades no inventário
def listar_inventario():
    for item, quantidade in inventario.items():
        print(f"Item: {item}, Quantidade: {quantidade}")

adicionar_item("maçã", 10)
adicionar_item("banana", 5)
remover_item("maçã", 3)
listar_inventario()
