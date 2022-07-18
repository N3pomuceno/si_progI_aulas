"""
MESMA COISA SÓ QUE FAZENDO DE UMA OUTRA FORMA:
Leia números da entrada padrão até que um número negativo seja digitado NUMA LINHA.
Identifique qual o maior número lido e quantos doram os números lidos,
O número negativo não deve ser contado.

Teste 1
Entradas:
1432
842.2354
47327
434
-1

Saída correspondente:
Maior número lido: 47327.0
Quantidade de números lidos: 4

Teste 2
-1
Saída correspondente:
Nenhum número válido foi lido!!!

"""
#Programa Maior lido e quantos
#Subprogramas
#Principal
qtdLidos = 0
maiorLido = None
numLido = float(input())
while numLido >= 0:
    qtdLidos += 1
    if maiorLido == None or numLido > maiorLido:    #1ª condição é o caso inicial, a segunda são para os seguintes
        maiorLido = numLido
    numLido = float(input())
if qtdLidos == 0:       #Condição que implica hein nenhum número válido foi lido, código nunca entra no while.
    print("Nenhum Número Válido Foi Lido!!!")
else:
    print("Maior Numero Lido:", maiorLido)
    print("Quantidade de Números Lidos", qtdLidos)