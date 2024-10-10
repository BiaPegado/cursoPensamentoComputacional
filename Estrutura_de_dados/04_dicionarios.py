'''Usar uma lista de pares key: value separados por vírgula com chaves: {'jack': 4098, 'sjoerd': 4127} ou {4098: 'jack', 4127: 'sjoerd'}

Usar uma compreensão de dicionário: {}, {x: x ** 2 for x in range(10)}

Usar o construtor de tipo: dict(), dict([('foo', 100), ('bar', 200)]), dict(foo=100, bar=200)'''

dicionario = {'felipe': 84987654321, 'maria': 84987654322}
dicionario2 = {x: x ** 2 for x in range(10)}
dicionario3 = dict()    #ou dict([('felipe', 84987654321), ('maria': 84987654322)])    

print(dicionario['maria'])
print(dicionario2)