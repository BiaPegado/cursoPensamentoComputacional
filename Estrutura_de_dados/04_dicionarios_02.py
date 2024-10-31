def contar_ocorrencias(texto):
    palavras = texto.split()        # Separa a string em palavras
    frequencia = {}
    
    for palavra in palavras:
        palavra = palavra.lower()   # Coloca todas as letra em lower case
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1
            
    return frequencia

texto = "Dicionários são extremamente úteis. Dicionários são legais."
dicionario = contar_ocorrencias(texto)

for key in dicionario:
    print(f"{key} - {dicionario[key]}")
