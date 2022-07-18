#Subprogramas
def constroi(nm):

    matCels = list()
    dados = open(nm,"r")

    for linha in dados:
        linha = linha.strip("\n")
        novaLinhaCels = list()

        for c in linha:
            novaLinhaCels.append(c)

        matCels.append(novaLinhaCels)
    dados.close()
    return matCels


def mostrar(matCels):
    
    for linhaDeCels in matCels:
        print(linhaDeCels)
    print()
    return None


def mataVizinhas(pLin, pCol, matCs):

    for lin in [pLin-1, pLin, pLin+1]:      
        #pode usar range -> range(pLin-1, pLin+2)
        for col in [pCol-1, pCol, pCol+1]:

            if 0 <=lin < len(matCs) and 0<= col<len(matCs[0]) and matCs[lin][col] == "X":
                matCs[lin][col] = "0"
                mataVizinhas(lin,col,matCs)
                mostrar(matCs)              #mostra toda vez que apaga alguem da matriz (pode apagar se preferir)

    return None


def conta(matCels):

    total = 0
    for lin in range(len(matCels)):
        for cols in range(len(matCels[lin])):
            if matCels[lin][cols] == 'X':
                matCels[lin][cols] = "0"
                total+=1
                mataVizinhas(lin, cols, matCels)
                #mostrar(matCels) 
                input()           #Trava o programa

    return total 




# Principal
nomeArq = input()
matrizDeCelulas = constroi(nomeArq)
mostrar(matrizDeCelulas) 
qtdConstrucoes =  conta(matrizDeCelulas)
print(qtdConstrucoes)