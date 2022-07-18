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
#Inicialização
valores = list (map(float, input())) # precisa da lista para ser identificado os valores, e não ter problema com o map como um objeto
if valores == []: #Forma de expressar que não tem nenhum valor, poderia ser por acaso ""
    print("Nenhum Número Foi Lido!!!") #resolvendo o problema de não ter um número no início do programa
else:
    maior = valores[0]
    for pos in range(1, len(valores)): #Comando len é para identifcar o tamanho da lista, que vem justo quando usamos list
        if valores[pos] > maior:
            maior = valores[pos]
        print("Maior Número Lido:", maior)
