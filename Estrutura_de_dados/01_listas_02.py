lista = []

continua = True
while continua:
    print("Informe um número para somar ou digite '-1' para sair: ")
    numero = int(input())

    if numero > 0:
        lista.append(numero)
    else:
        continua = False

soma = 0

for numero in lista:
    soma += numero

print(f"A soma é {soma}")
