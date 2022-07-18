#Programa
# TODO estudar
#Subprograma
def achaMenorMaiorEQtd(nm):
    qt = 0
    dados = open(nm, "r")
    linha = dados.readline()
    if linha == "":
        oMenor = oMaior = None
    else:
        oMenor = oMaior = float(linha.split()[0])
        while linha != "":
            numeros = list(map(float, linha.split()))
            for num in numeros:
                qt += 1
                if num < oMenor:
                    oMenor = num
                elif num > oMaior:
                    oMaior = num

            linha = dados.readline()
    dados.close()
    return oMenor, oMaior, qt


# Principal


nome = input()
menor, maior, qtd = achaMenorMaiorEQtd(nome)
print("Dentro do Arquivo %s o Menor, o Maior e Quantidade são: %.2f, %.2f, %d"%(nome, menor, maior, qtd))
