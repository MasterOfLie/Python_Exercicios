#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os. 

lista = [1, 2, 3, 4, 5]

for i in lista:
    print(i)

vetor = []
for i in range(5):
    vetor.append(int(input("Digite um numero: ")))
for i in vetor:
    print(i)
    