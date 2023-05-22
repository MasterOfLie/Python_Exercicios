# 22 - Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão). 

n = int(input('Digite um número inteiro: '))

resto = n % 2
if resto == 0:
    print('O número é par')
else:
    print('O número é impar')