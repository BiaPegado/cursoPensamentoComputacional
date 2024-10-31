tupla = ('arroz', 'feijão', 'carne')

for el in tupla:
    print(f"{tupla.index(el)} - {el}")

print("")

for indice, el in enumerate(tupla):
    print(f"{indice} - {el}")
