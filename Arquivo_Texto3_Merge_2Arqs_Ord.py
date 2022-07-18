#Programa Mistura - Merge
# TODO estudar
#Subprogramas
def mistura(nmA, nmB, nmAB):
    dadosA = open(nmA, "r")
    dadosB = open(nmB, "r")
    dadosAB = open(nmAB, "w")
    linhaA = dadosA.readline()
    linhaB = dadosB.readline()
    while linhaA != "" and linhaB != "":
        numA = float(linhaA)
        numB = float(linhaB)
        if numA <= numB:
            dadosAB.write(linhaA)
            linhaA = dadosA.readline()
        else:
            dadosAB.write(linhaB)
            linhaB = dadosB.readline()
    while linhaA != "":
        dadosAB.write(linhaA)
        linhaA = dadosA.readline()
    while linhaB != "":
        dadosAB.write(linhaB)
        linhaB = dadosB.readline()
    dadosA.close()
    dadosB.close()
    dadosAB.close()
    return

def mostra(nm):
    print(nm+":")
    dados = open(nm, "r")
    for linha in dados:
        print(linha, end="")
    dados.close()
    print()
    return None

#Principal

nomeA, nomeB, nomeMisturaAComB = input().split()
mistura(nomeA,nomeB,nomeMisturaAComB)
mostra(nomeA)
mostra(nomeB)
mostra(nomeMisturaAComB)
