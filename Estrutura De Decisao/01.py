#Faça um Programa que peça dois números e imprima o maior deles.
n1 = int(input("Primeiro numero: "))
n2 = int(input("Segundo numero: "))

if n1 > n2:
    print('O maior numero e ',n1)
elif n2 > n1:
    print('O maior numero e ',n2)
else:
    print('Os dois numeros sao iguais ',n1," E ",n2)