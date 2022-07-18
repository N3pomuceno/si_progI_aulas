# TODO estudar
#programa - lisp(list processing - programação funcional)
#Subprogramas
#Funções primitivas
def vazia(lista):
    return lista == []

def car(lista):
    return lista[0]

def cdr(lista):
    return lista[1:]

def cons(valor, lista):
    return [valor] + lista

#Nossas funções (Easy first - o mais fácil primeiro)
def soma(lista):
    if vazia(lista):
        return 0
    else:
        return car(lista) + soma(cdr(lista))

def pertence(valor, lista):
    if vazia(lista):
        return False
    else:
        if valor == car(lista):
            return True
        else:
            return pertence(valor, cdr(lista))

def conjunto(lista):
    if vazia(lista):
        return []
    else:
        if pertence(car(lista), cdr(lista)):
            return conjunto(cdr(lista))
        else:
            return cons(car(lista), conjunto(cdr(lista)))

def intersecao(lista1,lista2):
    if vazia(lista1):
        return []
    else:
        if pertence(car(lista1), lista2):
            return cons(car(lista1), intersecao(cdr(lista1), lista2))
        else:
            return intersecao(cdr(lista1), lista2)

def insereOrdenado(valor, lista):
    if vazia(lista):
        return cons(valor, [])
    else:
        if valor < car(lista):
            return cons(valor, lista)
        else:
            return cons(car(lista), insereOrdenado(valor, cdr(lista)))

def ordena(lista): #insertion sort
    if vazia(lista):
        return []
    else:
        return insereOrdenado(car(lista), ordena(cdr(lista)))


#Principal
valores = [34.44, 54.13, 1, 0.3333, 2.7, -1.99, 2.7, 1 , 54.13]
print(soma(valores))
print(pertence(1, valores))
print(conjunto(valores))
print(intersecao(conjunto(valores), [3, 4, 5, 1, 2.7]))
print(insereOrdenado("Josivaldo", ["Ana", "Arthur", "Maria José", "Olímpio"]))
print(ordena(valores))
