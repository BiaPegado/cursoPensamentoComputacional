class Node:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

class Arvore:
    def __init__(self):
        self.raiz = None
    
    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = Node(valor)
        else:
            self.inserir_recursiva(self.raiz, valor)
    
    def inserir_recursiva(self, node, valor):
        if valor < node.valor:
            if node.left is None:
                node.left = Node(valor)
            else:
                self.inserir_recursiva(node.left, valor)
        else:
            if node.right is None:
                node.right = Node(valor)
            else:
                self.inserir_recursiva(node.right, valor)

    def pesquisar(self, valor):
        return self.pesquisar_recursiva(self.raiz, valor)
    def pesquisar_recursiva(self, node, valor):
        if node is None or node.valor == valor:
           return f"{node.valor} foi encontrado." if node else f"{valor} não foi encontrado."
        if valor < node.valor:
            return self.pesquisar_recursiva(node.left, valor)
        return self.pesquisar_recursiva(node.right, valor)

arvore = Arvore()
arvore.inserir(10)
arvore.inserir(5)
arvore.inserir(15)

print(arvore.pesquisar(5))
print(arvore.pesquisar(20))