"""
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
maior = None  #Definindo as variáveis inicialmente mas não definindo um valor para elas.
qtdLidos = 0
#Processamento
numero = float(input())
while numero >= 0:
    qtdLidos += 1
    if maior == None or numero >maior:  #Primeira condição é para alterar inicialmente o None que aparece, para substituir logo
        maior = numero    #a variável maior recebe a informação do numero, caso seja maior ou maior seja None
    numero = float(input())  #novo número para ver se ainda está dentro do while, condição necessária para sair do while
#Finalização
if maior == None:
    print("Nenhum Número Válido Foi Lido!!!")  #Condição que pode ser colocada inicialmente.
else:
    print("Maior Número Lido:", maior)
    print("Quantidade de Números Lidos:", qtdLidos)
