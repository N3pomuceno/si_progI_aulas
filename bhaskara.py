def bhas(a,b,c):
    delta = b**2 - 4*a*c
    if a == 0:
        print("Tem somente uma raiz")
        x = -c/b
        print("{}".format(x))
    elif delta < 0:
        print("Há raízes imaginárias")
    elif delta == 0:
        print("Tem somente uma raiz")
        x = -b/(2 * a)
        print("{}".format(x))
    else:
        print("As duas raízes são:")
        x = (-b + (delta) ** (1 / 2)) / (2 * a)
        print("{}".format(x))
        x = (-b - (delta) ** (1 / 2)) / (2 * a)
        print("{}".format(x))
    return None

print("Coloque os coeficientes da fórmula quadrática")
coefa, coefb, coefc = map(int, input().split())
bhas(coefa,coefb,coefc)
