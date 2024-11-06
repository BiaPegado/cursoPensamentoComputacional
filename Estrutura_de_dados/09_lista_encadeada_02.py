#Nó da lista
class Node:

    def __init__(self, valor):
        self.valor = valor
        self.next = None
        self.prev = None

#Lista encadeada
class ListaEncadeada:

    #Construtor
    def __init__(self):
        self.head = None

    #Método para adicionar valor
    def append(self, valor):
        novo_node = Node(valor)

        if(self.head == None):
            self.head = novo_node
            self.tail = novo_node
        else:
            novo_node.prev = self.tail
            self.tail.next = novo_node
            self.tail = novo_node
        return
    
    #Método para remover o primeiro valor
    def rm_inicio(self):
        if self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None

    def rm(self, indice):
        if indice == 0:
            self.rm_inicio()
        node_atual = self.getNode(indice)

        if node_atual:
            if node_atual.next:
                node_atual.next.prev = node_atual.prev
            if node_atual.prev:
                node_atual.prev.next = node_atual.next
            if node_atual == self.tail:
                self.tail = node_atual.prev
            return
    
    # Método para achar um node
    def getNode(self, indice):
        if indice < 0 or indice >= self.len():  
            return None
        
        meio = self.len() // 2
        if indice <= meio: 
            indice_atual = 0
            node_atual = self.head
            while node_atual:
                if indice_atual == indice:
                    return node_atual
                node_atual = node_atual.next
                indice_atual += 1
        else:  
            indice_atual = self.len() - 1
            node_atual = self.tail
            while node_atual:
                if indice_atual == indice:
                    return node_atual
                node_atual = node_atual.prev
                indice_atual -= 1

    #Método para saber o tamanho da lista encadeada
    def len(self):
        if self.head == None:
            return 0
        node_atual = self.head
        tam = 0

        while node_atual:
            tam+=1
            node_atual = node_atual.next

        return tam
    #Método que retorna uma lista com os valores da lista encadeada
    def print(self):
        if self.head == None:
            return None
        node_atual = self.head
        lista = []

        while node_atual:
            lista.append(node_atual.valor)
            node_atual = node_atual.next

        return lista
    
lista_encadeada = ListaEncadeada()
lista_encadeada.append(1)
lista_encadeada.append(2)
lista_encadeada.append(3)
lista_encadeada.append(4)

print(f"lista_encadeada = {lista_encadeada.print()}")                                         #len = 4
print(f"Primeiro valor na lista: {lista_encadeada.getNode(0).valor}")                 #1
lista_encadeada.rm_inicio()
print(f"Primeiro valor na lista após remoção: {lista_encadeada.getNode(0).valor}")    #2

lista_encadeada.rm(1)
print("Removendo Segundo valor na lista...")

print(f"Segundo valor na lista após remoção: {lista_encadeada.getNode(1).valor}")     #4

print(f"lista_encadeada = {lista_encadeada.print()}")                                         #len = 2
