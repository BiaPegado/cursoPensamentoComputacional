lista_compras = {"arroz", "feijão", "macarrão", "maçã", "banana"}
frutas = {"maçã", "banana"}

uniao = list(lista_compras.union(frutas))
print(uniao)

inters = list(lista_compras.intersection(frutas))
print(inters)

dif = list(lista_compras.difference(frutas))
print(dif)

subset = lista_compras.issubset(frutas)
print(subset)

superset = lista_compras.issuperset(frutas)
print(superset)

dis = lista_compras.isdisjoint(frutas)
print(dis)
