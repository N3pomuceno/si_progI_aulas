#Leia números inteiros da entrada padrão até que um número negativo
# seja digitado. Para cada número lido, exceto para o negativo, escreva na saída padrão
#se aquele número é primo ou não.

#Definição: um número inteiro é primo se e somente se for maior que um e for apensar divisível por ele mesmo.

#programa Primos ou não

#Subprogramas
def ehPrimo(num)
    for divisor in range (2, int(num**0.5+1)):
        if num % divisor == 0:
            return False
    return num > 1

#fazendo o subprograma retorna uma variável booleana, true ou false, o for tem um break natural, com o return false
# e depois do return no fim tem uma condição que vai definir se vai ser true ou false, pois é a condição para ser primo.

#Principal
entradaLida = int(input()) #pega primeiro
while entradaLida >= 0:
    if ehPrimo(entradaLida):
        print (entradaLida, "é primo")
    else:
        print(entradaLida, "não é primo")

    entradaLida = int(input())
