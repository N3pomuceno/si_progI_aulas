"""
Lear as dimentsões de uma matriz bidimensional na primeira linha.
Nas linhas seguintes os números de cada célula da matriz serão lidos, um por linha.
Construa a matriz e, ao final, mostre que seu conteúdo de forma amigável.

teste:
3 2
13.2
-23.4
1.0
.5
7
9

"""

#Programa
#Subprograma
def produz (qLins,qCols):
    vals = []
    for lin in range(qlins):
        novaLinhaDeValores = []
        for col in range(qCols):
            novaLinhaDeValores.append(int(input()))
        vals.append(novaLinhaDeValores)
    return vals

def mostra(vals,formato):
    print("matriz de Valores:")
    for linhaDeValores in vals:
        for valor in linhaDeValores:
            print(formato%valor, end="")
        print()
    print()
    return None

def achaMaiorString(vals):
    maiorTamanho = 0
    for linhaDeValores in vals:
        for valor in linhaDeValores:
            if int(len(str(valor))) > maiorTamanho:
                maiorTamanho = int(len(str(valor)))
    return None

#Principal
qtdLinhas, qtdColuna = map(int, input().split())
valores = produz(qtdLinhas,qtdColuna)
maiorString = achaMaiorString(valores)
formatoIdentificado = "%"+str(maiorString+1)+"d"
mostra(valores, formatoIdentificado)

"""
Partindo para a analise, começamos notando a estrutura do programa, 3 subprogramas, e o corpo principal.
o suprograma produz monta a matriz, mostra é um print para a matriz, e achaMaiorString é para definir o maior inteiro e
formato direito a matriz.



"""

