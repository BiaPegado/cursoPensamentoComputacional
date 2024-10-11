lista_compras = ['arroz', 'feijão', 'carne', 'frango']
tuple_compras = ('maçã', 'limão', 'beterraba', 'miojo', 'carne')

lista_fatiada = lista_compras[2:4]
tuple_fatiada = tuple_compras[2:4:1]
tuple_fatiada2 = tuple_compras[::2]

print(lista_fatiada)        #['carne', 'frango']
print(tuple_fatiada)        #('beterraba', 'miojo')
print(tuple_fatiada2)       #('maçã', 'beterraba', 'carne')