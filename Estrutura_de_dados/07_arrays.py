import array as arr

array1 = arr.array('i', [1, 2, 3])

print(array1)

array2 = arr.array('d', [2.5, 3.2, 3.3])

print("Os itens da array2 são:")
for i in range(0, len(array2)):
    print(array2[i], end=" ")

#array3 = arr.array('i', [1, 2, 3, 'ola'])
#print(array3)