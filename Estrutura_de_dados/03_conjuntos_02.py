lista_compras = {"arroz", "feijão", "macarrão", "maçã", "banana"}
frutas = {"maçã", "banana"}

uniao = list(lista_compras.union(frutas))
print(uniao, end="\n")

inters = list(lista_compras.intersection(frutas))
print(inters, end="\n")

dif = list(lista_compras.difference(frutas))
print(dif, end="\n")

subset = lista_compras.issubset(frutas)
print(subset, end="\n")

superset = lista_compras.issuperset(frutas)
print(superset, end="\n")

dis = lista_compras.isdisjoint(frutas)
print(dis, end="\n")
