# 7 - Faça um Programa que leia três números e mostre o maior e o menor deles. 
n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
n3 = float(input("Digite o terceiro numero: "))

if n1 == n2 and n1 == n3:
    print(f"Os numeros sao iguais")
else:
    #Maior numero
    if n1 > n2 and n1 > n3:
        print(f"O {n1} e o maior numero")
    elif n2 > n1 and n2 > n3:
        print(f"O {n2} e o maior numero")
    else:
        print(f"O {n3} e o maior numero")
    #Menor numero
    if n1 < n2 and n1 < n3:
        print(f"O {n1} e o menor numero")
    elif n2 < n1 and n2 < n3:
        print(f"O {n2} e o menor numero")
    else:
        print(f"O {n3} e o maior numero")