# 8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. 

n1 = float(input("Digite o preço do primeiro produto: "))
n2 = float(input("Digite o preço do segundo produto: "))
n3 = float(input("Digite o preço do terceiro produto: "))

if n1 < n2 and n1 < n3:
    print(f"você deve comprar o primeiro produto pois e o de menor custo {n1}")
elif n2 < n1 and n2 < n3:
    print(f"você deve comprar o segundo produto pois e o de menor custo {n2}")
else:
    print(f"você deve comprar o terceiro produto pois e o de menor custo {n3}")