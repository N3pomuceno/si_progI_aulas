def ordem(vet):
    def posMenor(vector, inicio):

        return position
    #Aqui podemos fazer a referência tanto pela posição quanto pelo valor em si. e podemos criar um vetor de saída ou trabalhar com o próprio vet
    #Usaremos o vet para tentar diminuir o custo do programa
    for pos in range(len(vet)):
        posicao = posMenor(vet,pos)


    return vet

def escrever(num):
    vet = []
    for ind in range(num):
        n = int(input())
        vet.append(n)
    return vet

def mostrar(vet):
    for j in range(len(vet)):
        print("{}".format(vet[j]))
    print()
    return None

#Fazendo de duas formas para fazer esse cálculo, pode ser pela linha ou a cada enter, vou começar pelo segundo e depois vou fazer por linha.
#Ao mesmo tempo tem a possibilidade de fazer com um while que define a quantidade de valores na hora. ou definir de antemão qual é a quantidade de valores, vamos começar com o segundo também.

qtd = int(input("Quantidade de valores no vetor:"))
vetor = escrever(qtd)
vetorOrdenado = ordem(vetor)
mostrar(vetorOrdenado)
