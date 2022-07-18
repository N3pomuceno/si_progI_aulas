"""
Utilizando subprogramação, leia número até que um número negativo seja digitado.
Mantenha todos os números lidos em uma lista, exceto o negativo.
Mostre o conteúdo da lista produzida.
Calcule e escreva a média de todos os números lidos.
Escreva todos os números acima da média calculada.

Teste:
Entradas:
43
41
2
32
13
32.34
33.1
-1

Saídas Correspondentes:
Conteúdo do lista produzida:
43.00
41.00
2.00
32.00
13.00
32.34
33.10
-1.00

Média dos Números: 28.06

Número Acima da Média:
43.0
41.00
32.00
32.34
33.10


"""
#Programa
#Subprograma
def lerNumeros():
    nums = []
    valor = float(input())  #pega o primeiro
    while valor >= 0:
        nums.append(valor)   #"Anexar no fim de uma lista é usar o append"// poderia ser nums.insert(0,valor) insere no primeiro endereço! o 0 está associado a posição, poderia ser uma variável tbm!
        valor = float(input())   #Pega o próximo
    return nums

def mostra(nums):
    print("Conteúdo da lista produzida:")
    for x in nums:
        print("%.2f"%x)
    print()
    return None

def calculaMedia(nums):
    if nums == []:
        return None
    else:
        quantidade = len(nums)
        sumaDosNumeros = 0
        for x in nums:
            somaDosNumeros = somaDosNumeros + x
        return somaDosNumeros/quantidade

def listaAcima(limite, nums, msg):
    print("Números Acima da", msg+":")
    for x in nums:
        if x >= limite:
            print("%.2f"%x)
    return None


#Principal
numeros = lerNumeros()
if numeros == []:
    print("Não existe média - Nenhum número lido maior ou igual a zero foi digitado!!!")
else:
    mostra(numeros)
    media = calculaMedia(numeros)
    print("Média dos Números: %.2f\n"%media)
    listaAzima(media, numeros,"Média mais 20%")




"""
Explicação do programa




Função SEMPRE retorna um valor print(x), procedure não necessariamente retorna  - mostra(numeros)
"""