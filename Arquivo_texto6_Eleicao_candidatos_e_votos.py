#Programa Eleições 2022
#TODO estudar
#Para rodar esse programa precisa de dois arquivos, um de 'candidatos' e um de 'votos';
#candidatos com a formatação: NOME DO CANDIDATO # NUMERO DO CANDIDATO \n
#votos com a formatação: NUMERO DO VOTO




#Subprogramas
def zeraVotacao(nm):
    listaCsNumsVts = [["Nulo", "-1", 0], ["Brancos", "0", 0]]
    dados = open(nm, "r", encoding="utf-8")
    for linha in dados:
        cand, numero = linha.strip("\n").split(" # ")
        listaCsNumsVts.append([cand, numero, 0])
    dados.close()
    return listaCsNumsVts

def mostraResultados(listaCsNumsVts):
    print("Resultados Finais da Eleição:")
    for cand, num, vts in listaCsNumsVts:
        print("%30s %3s %5d"%(cand, num, vts))
    print()
    return None

def localiza(numCandVotado, listaCsNumsVts):
    for i in range(len(listaCsNumsVts)):
        if numCandVotado == listaCsNumsVts[i][1]:
            return i
    return -1  #-1 é usado não dizer que não foi localizado, mas o python está trazendo o endereço de trás para frente da lista

def apura(listaCsNumsVts, nm):
    dados = open(nm, "r")
    for voto in dados:
        voto = voto.strip("\n")
        onde = localiza(voto, listaCsNumsVts)
        if onde == -1:
            print(voto, "Candidato inexistente - Urna Corrompida!!!")
        else:
            listaCsNumsVts[onde][2] += 1
    dados.close()
    return None

#Principal
nomeArqCands = input()
listaCandsNumerosVotos = zeraVotacao(nomeArqCands)
nomeArqVotos = input()
apura(listaCandsNumerosVotos, nomeArqVotos)
mostraResultados(listaCandsNumerosVotos)


