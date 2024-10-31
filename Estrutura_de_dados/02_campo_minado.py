import random
#Campo minado

def pega_coordenadas():
    coordenada = input()
    coordenada_sem_virgula = coordenada.replace(",", "")
    coordenada_sem_virgula = coordenada_sem_virgula.split()
    return coordenada_sem_virgula

campo_minado = [[0 for j in range(10)] for i in range(10)]
campo_bombas = []

def imprimirCampo(campo):
    for linha in campo:
        print(linha)

def criar_bombas(campo_bombas):
    quantidade_bombas = 10
    campo_bombas = [(random.randint(0, 9), random.randint(0, 9)) for _ in range(quantidade_bombas)]
    return campo_bombas

campo_bombas = criar_bombas(campo_bombas)
rodando = True
print(f"coordenadas das bombas: {campo_bombas}")

imprimirCampo(campo_minado)
while rodando:
    print("Escolha uma coordenada: ")
    coordenadas = pega_coordenadas()
    x, y = coordenadas

    if (int(x), int(y)) in campo_bombas:
        rodando = False
        print("GAME OVER!!!")
    else:
        campo_minado[int(x)][int(y)] = 1
        imprimirCampo(campo_minado)