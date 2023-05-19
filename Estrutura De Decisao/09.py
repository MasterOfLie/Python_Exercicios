# 9 - Faça um Programa que leia três números e mostre-os em ordem decrescente. 

n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
n3 = float(input("Digite o terceiro numero: "))
meio = 0
menor = 0
maior = 0
if n1 == n2 and n1 == n3:
    print(f"Os numeros sao iguais")
else:
    #N1 
    if n1 > n2 and n1 > n3:
        maior = n1
    elif n1 < n2 and n1 < n3:
        menor = n1
    else:
        meio = n1
    #N2
    if n2 > n1 and n2 > n3:
        maior = n2
    elif n2 < n1 and n2 < n3:
        menor = n2
    else:
        meio = n2
    #N3
    if n3 > n1 and n3 > n2 :
        maior = n3
    elif n3 < n1 and n3 < n2:
        menor = n3
    else:
        meio = n3
print(f" O Maior numero e {maior}\n O Numero do meio e {meio}\n O Menor numero e {menor}")