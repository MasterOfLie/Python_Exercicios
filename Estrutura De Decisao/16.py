# 16 - Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

#     Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#     Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#     Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#     Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário; 
import sys
a = float(input("Informe o valor de A: "))
if a == 0:
    print("A não pode ser igual a zero")
    print("Encerrando...")
    sys.exit(0)
else:
    b = float(input("Informe o valor de B: "))
    c = float(input("Informe o valor de C: "))
    delta = b**2 - 4*a*c
    if delta < 0:
        print("A equação não possui raizes reais")
        print("Encerrando...")
        sys.exit(0)
    elif delta == 0:
        print("A equação possui apenas uma raiz real")
        x = ( -b / (2*a) )
        print("A raiz é: ", x)
    else:
        print("A equação possui duas raizes reais")
        x1 = (-b + delta**(1/2)) / (2*a)
        x2 = (-b - delta**(1/2)) / (2*a)
        print("A primeira raiz é: ", x1)
        print("A segunda raiz é: ", x2)