#Programa
#Subprograma
def hanoi(origem,temporario,destino, qtdD,pars):
    if qtdD == 0:
        return None
    else:
        hanoi(origem,temporario,destino,qtdD-1,pars)
        pars[0] += 1
        print("Mover disco de", origem, "para", temporario)
        hanoi(destino,temporario,origem,qtdD-1,pars)
        pars[0] += 1
        print("Mover disco de", temporario, "para", destino)
        hanoi(origem,temporario,destino,qtdD-1,pars)
        return None

#Principal
parametros = [0]
qtdDiscos = int(input())
hanoi("A","B","C",qtdDiscos,parametros)
print("Movimentos:", parametros[0])

"""
hanoi(1) = 2
hanoi(2) = 8
hanoi(3) = 26
...
hanoi(n) = 2+3*hanoi(n-1)
hanoi(n) = 3**n - 1
"""