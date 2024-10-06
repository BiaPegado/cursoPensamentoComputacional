#Nó da lista
class Node:

    def __init__(self, valor):
        self.valor = valor
        self.next = None

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

            return
        
        node_atual = self.head

        while node_atual.next:
            node_atual = node_atual.next

        node_atual.next = novo_node

        return
    
    #Método para remover o primeiro valor
    def rm_inicio(self):
        self.head = self.head.next
        return

    def rm(self, indice):
        if indice < 0 or indice == self.len():
            return None
        indice_atual = 0
        node_atual = self.head
        node_anterior = None

        while node_atual:
            if indice_atual == indice:
                node_anterior.next = node_atual.next
                return
            node_anterior = node_atual
            node_atual = node_atual.next
            indice_atual+=1
    
    #Método para ler
    def getNode(self, indice):
        if indice < 0 or indice == self.len():
            return None
        indice_atual = 0
        node_atual = self.head

        while node_atual:
            if indice_atual == indice:
                return node_atual.valor
            node_atual = node_atual.next
            indice_atual+=1

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
print(f"Primeiro valor na lista: {lista_encadeada.getNode(0)}")                 #1
lista_encadeada.rm_inicio()
print(f"Primeiro valor na lista após remoção: {lista_encadeada.getNode(0)}")    #2

lista_encadeada.rm(1)
print("Removendo Segundo valor na lista...")

print(f"Segundo valor na lista após remoção: {lista_encadeada.getNode(1)}")     #4

print(f"lista_encadeada = {lista_encadeada.print()}")                                         #len = 2


