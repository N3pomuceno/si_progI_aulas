#programa
#Subprograma
def hanoi(orig,temp,dest,qD):
    if qD == 0:
        return 0
    else:
        return hanoi(orig, dest, temp, qD - 1) + 1 + hanoi(temp, orig, dest, qD -1 )

#Programa
import time
qtDisco = int(input())
antes = time.time()
qtdMovimentos = hanoi("A","B","C", qtDisco)
depois = time.time()
print(qtdMovimentos)
print("%.2f segundos"%(depois-antes))