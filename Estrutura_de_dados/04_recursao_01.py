def loop_infinito(x): 
    if x == 10: return      # Este é o caso-base, comente essa linha para criar um loop infinito.
    
    print(f"O número escolhido é {x}")

    return (loop_infinito(x+1))

loop_infinito(0)