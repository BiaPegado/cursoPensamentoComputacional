from collections import deque

def pesquisa_em_largura(grafos, inicio):
    visitados = set()
    fila = deque([inicio])

    while fila:
        grafo_atual = fila.popleft()

        if grafo_atual not in visitados:
            print(grafo_atual)
            visitados.add(grafo_atual)

            for vizinho in grafos[grafo_atual]:
                if vizinho not in visitados:
                    fila.append(vizinho)

grafos = {
    'A': ['B', 'C'],     
    'B': ['A', 'D', 'E', 'G'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
    'G': ['A']
}

pesquisa_em_largura(grafos, 'A')