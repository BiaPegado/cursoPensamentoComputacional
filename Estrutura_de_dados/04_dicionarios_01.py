dicionario = {'felipe': 84987654321, 'maria': 84987654322}
dicionario2 = {x: x ** 2 for x in range(10)}
dicionario3 = dict()    #ou dict([('felipe', 84987654321), ('maria': 84987654322)])    

print(dicionario['maria'])  # 84987654322
print(dicionario2)          # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
