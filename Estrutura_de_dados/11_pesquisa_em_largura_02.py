from collections import deque

class grafo:

    def __init__(self, vertice: str, tem_jogo: bool):
        self.vertice = vertice
        self.tem_jogo = tem_jogo

    def getVertice(self):
        return self.vertice

    def getArestas(self):
        return self.arestas

    def getTemJogo(self):
        return self.tem_jogo
    
    def adicionarArestas(self, arestas):
        self.arestas = arestas
        
def pesquisa_em_largura(inicio):
    visitados = set()      
    fila = deque([inicio]) 

    while fila:
        vertice_atual = fila.popleft()
        if vertice_atual.getTemJogo():
            return vertice_atual.getVertice()
        
        if vertice_atual not in visitados:
            print(vertice_atual.getVertice())   
            visitados.add(vertice_atual)

            for vizinho in vertice_atual.getArestas():
                if vizinho not in visitados:
                    fila.append(vizinho)
    return 'ninguém'

A = grafo('A', False)
B = grafo('B', False)
C = grafo('C', False)
D = grafo('D', False)
E = grafo('E', False)
F = grafo('F', False)

A.adicionarArestas([B, C])
B.adicionarArestas([A, D, E])
C.adicionarArestas([A, F])
D.adicionarArestas([B])
E.adicionarArestas([B, F])
F.adicionarArestas([C, E])


print(f"Encontrei o jogo com {pesquisa_em_largura(A)}")
