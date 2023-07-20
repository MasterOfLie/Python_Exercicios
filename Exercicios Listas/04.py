#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes. 

vetor = []
for i in range(10):
    palavra = input("Digite um caracter: ").upper()
    vetor.append(palavra[0])
print(vetor)
consoantes = 0
for i in vetor:
    if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        consoantes += 1
print("As consoantes foram: ", consoantes)

