def busca_menor_indice(arr):
    menor = arr[0]
    menor_indice = 0

    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordenacao_por_selecao(arr):
    aux_arr = []

    for i in range(1, len(arr)):
        menor_indice = busca_menor_indice(arr)
        aux_arr.append(arr.pop(menor_indice))
        
    return aux_arr

arr = [9, 8, 2, 4, 0, 5, 10]

print(ordenacao_por_selecao(arr))