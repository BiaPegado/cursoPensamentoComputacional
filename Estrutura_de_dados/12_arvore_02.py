class Node:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None
        self.altura = 1  # A altura começa em 1, pois o nó é inicialmente uma folha

class ArvoreAVL:
    def obter_altura(self, node):
        return node.altura if node else 0

    def obter_balanceamento(self, node):
        return self.obter_altura(node.esquerda) - self.obter_altura(node.direita) if node else 0

    def rotacao_direita(self, y):
        x = y.esquerda
        T2 = x.direita

        x.direita = y
        y.esquerda = T2

        y.altura = 1 + max(self.obter_altura(y.esquerda), self.obter_altura(y.direita))
        x.altura = 1 + max(self.obter_altura(x.esquerda), self.obter_altura(x.direita))

        return x 

    def rotacao_esquerda(self, x):
        y = x.direita
        T2 = y.esquerda

        # Realiza a rotação
        y.esquerda = x
        x.direita = T2

        # Atualiza as alturas
        x.altura = 1 + max(self.obter_altura(x.esquerda), self.obter_altura(x.direita))
        y.altura = 1 + max(self.obter_altura(y.esquerda), self.obter_altura(y.direita))

        return y 

    def inserir(self, node, chave):
        if not node:
            return Node(chave)
        elif chave < node.chave:
            node.esquerda = self.inserir(node.esquerda, chave)
        else:
            node.direita = self.inserir(node.direita, chave)

        node.altura = 1 + max(self.obter_altura(node.esquerda), self.obter_altura(node.direita))

        balanceamento = self.obter_balanceamento(node)

        # Casos de desbalanceamento:
        # Rotação à R
        if balanceamento > 1 and chave < node.esquerda.chave:
            return self.rotacao_direita(node)

        # Rotação à L
        if balanceamento < -1 and chave > node.direita.chave:
            return self.rotacao_esquerda(node)

        # Rotação dupla à RL
        if balanceamento > 1 and chave > node.esquerda.chave:
            node.esquerda = self.rotacao_esquerda(node.esquerda)
            return self.rotacao_direita(node)

        # Rotação dupla à LR
        if balanceamento < -1 and chave < node.direita.chave:
            node.direita = self.rotacao_direita(node.direita)
            return self.rotacao_esquerda(node)

        return node 

    def pre_ordem(self, node):
        if node:
            print(f"{node.chave} ", end="")
            self.pre_ordem(node.esquerda)
            self.pre_ordem(node.direita)


arvore = ArvoreAVL()
raiz = None

# Inserindo valores na árvore AVL
for chave in [10, 20, 30, 40, 50, 25]:
    raiz = arvore.inserir(raiz, chave)

# Impressão em pré-ordem da árvore balanceada
print("Percurso em pré-ordem da árvore AVL:")
arvore.pre_ordem(raiz)
