#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: 
n1 = int(input("Digite o primeiro numero Inteiro: "))
n2 = int(input("Digite o segundo numero Inteiro: "))
n3 = float(input("Digite o terceiro numero Real: "))

#o produto do dobro do primeiro com metade do segundo . 
aux = n1 * 2 *(n2/2)
print("Questao A: ",aux)

#a soma do triplo do primeiro com o terceiro. 
aux = n1 *3 +n3
print("Questao B:",aux)

#o terceiro elevado ao cubo. 
aux = n3**3
print("Questao C:",aux)