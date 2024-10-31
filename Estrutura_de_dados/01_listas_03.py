palavra_normal = []
palavra_invertida = []

print("Informe a palavra: ")
palavra = input()
palavra_normal = list(palavra)
print(palavra_normal)
palavra_invertida = list(palavra)
palavra_invertida.reverse()
print(palavra_invertida)

if palavra_invertida == palavra_normal:
    print("É UM PALINDROMO!!!")

else:
    print("Não é :(")