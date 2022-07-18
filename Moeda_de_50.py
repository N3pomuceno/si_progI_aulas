#Programa
#Subprograma
def construa(qtd, minimo, maximo):
    import random  #Tem outra forma de puxar bibilioteca só puxando um comando da bibliotexa
    vetNumsAleats = []
    for pos in range(qtd):
        valorAeatorio = random.randint(minimo, maximo)
        vetNumsAleats.append(valorAeatorio)
    return vetNumsAleats

def mostra(vetNumsAleats):
    print("Conteúdo do Vetor:")
    for valor in vetNumsAleats: #poderia usar uma tupla que enumera as posições para facilitar a visualização usando enumerate
        print(valor)
    print()
    return None

def localiza(vetNumsAleats):
    posMenor = posMaior = 0
    for pos in range(1,len(vetNumsAleats)):
        if vetNumsAleats[pos] < vetNumsAleats[posMenor]:
            posMenor = pos
        elif vetNumsAleats[pos] > vetNumsAleats[posMaior]:
            posMaior = pos
    return posMenor + 1, posMaior + 1




#Principal
qtdNums, valorMinimo, valorMaximo = map(int, input().split())
vetorDeNumerosAleatorios = construa(qtdNums, valorMinimo, valorMaximo)
mostra(vetorDeNumerosAleatorios)
posMenorValor, posMaiorValor = localiza(vetorDeNumerosAleatorios)
print("Posição de um menor valor:", posMenorValor)
print("Posição de um maior valor:", posMaiorValor)
