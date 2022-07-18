"""
3 pinos, e um número definido de discos tem que passar de um para o outro, sempre respeitando que o disco de
 diametro menor estando em cima do diametro maior.


"""
#Recursão! Chamando a si próprio para resolver o problema
def hanoi(origem,temporario,destino, qtdD,pars):
    if qtdD == 0:
        return None
    else:
        hanoi(origem,destino,temporario,qtdD-1,pars)
        pars[0] += 1
        print("Mover disco de", origem, "para", destino)
        hanoi(temporario, origem, destino,qtdD-1,pars)
        return None

#Principal
parametros = [0]
qtdDiscos = int(input())
hanoi("A","B","C",qtdDiscos,parametros)
print("Movimentos:", parametros[0])

"""
hanoi(1) = 1
hanoi(2) = 3
hanoi(3) = 7
hanoi(4) = 15
hanoi(5) = 31
...
hanoi(n) = 1+2*hanoi(n-1)
hanoi(n) = 2**hanoi(n) - 1

"""