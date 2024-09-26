def fatorial(x):
    if(x==1):
        return 1
    else:
        return x * fatorial(x-1)

x = 3
print(f"O fatorial de {x} é {fatorial(x)}") #O fatorial de 3 é 6