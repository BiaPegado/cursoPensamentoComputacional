# Achar as melhores turmas no PES

ciencia_de_dados = {'aprendizado de maquina', 'ciencia de dados', 'etica e dados', 'probabilidade e inferencia'}
internet_das_coisas = {'ciencia de dados', 'introducao a internet das coisas', 'dispositivos para internet das coisas', 'plataformas de hardware para internet das coisas', 'aprendizado de maquina'}
informatica_educacional = {'avaliacao de software educacional', 'tecnologias educacionais', 'inteligencia artificial aplicada a educacao'}
inteligencia_artificial = {'probabilidade e inferencia', 'etica e dados', 'aprendizado de maquina', 'inteligencia artificial aplicada a educacao', 'aprendizado profundo', 'aprendizado por reforco'}
inteligencia_computacional = {'ciencia de dados', 'aprendizado de maquina', 'aprendizado por reforco', 'aprendizado profundo', 'inteligencia artificial aplicada a educacao'}

def uniao(setA: set, setB: set):
    return setA.union(setB)

def intersecao(conjuntos: list):
    setFinal = conjuntos[0]
    for conjunto in conjuntos:
       setFinal = setFinal.intersection(conjunto)
    return setFinal

def diferenca(setA: set, setB: set):
    return setA.difference(setB)

def printOperacao(setA):
    for indice, materia in enumerate(setA):
        print(f"{indice+1} - {materia}")

setUniao = uniao(ciencia_de_dados, inteligencia_artificial)

setIntersecao = intersecao([ciencia_de_dados, inteligencia_artificial, internet_das_coisas, inteligencia_computacional])

setDiferenca = diferenca(inteligencia_computacional, inteligencia_artificial)

print(f"União")
printOperacao(setUniao)


print(f"\nInterseção")
printOperacao(setIntersecao)


print(f"\nDiferença")
printOperacao(setDiferenca)
