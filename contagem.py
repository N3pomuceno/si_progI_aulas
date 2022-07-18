#Leia números de entrada padrão até que uma linha vazia seja digitado
#escreva na saída padrão qual doi o quantitativo de número e a soma dos números lidos

qtdNumeros=0
somaNumeros=0
numeroLido = float(input()) #primeiro número
while numeroLido != "":
    somaNumeros += numeroLido   #==== somaNumeros = somaNumeros+numeroLido
    qtdNumeros +=1
    numeroLido = float(input()) #próxima linha
print(qtdNumeros,somaNumeros)



