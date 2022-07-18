"""
MESMA COISA SÓ QUE FAZENDO DE UMA OUTRA FORMA:
Leia números da entrada padrão até que um número negativo seja digitado.
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
#Inicialização
numero = float(input())
if numero < 0:
    print("Nenhum Número Válido Foi Lido!!!") #If colocado inicialmente para cortar a possibilidade de começar com um negativo.
else:
    maior = numero
    qtdLidos = 0
    while numero >= 0:
        qtdLidos += 1
        if numero > maior:
            maior = numero
        numero = float(input())
    print("Maior Número Lido:", maior)
    print("Quantidade de  Número Lidos:", qtdLidos)