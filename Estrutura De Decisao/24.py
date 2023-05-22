# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

#     par ou ímpar;
#     positivo ou negativo;
#     inteiro ou decimal. 

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

op = input('Digite a operação: S - soma | M - multiplicação | D - divisão | U - subtração: ').upper()
if op == 'S':
    print('{} + {} = {}'.format(n1, n2, n1 + n2))
    resto = (n1 + n2) % 2
    print('O número é par' if resto == 0  else 'O número é impar')
    print('O número é negativo' if n1 < 0 and n2 < 0 else 'O número é positivo')
elif op == 'M':
    print('{} * {} = {}'.format(n1, n2, n1 * n2))    
    resto = (n1 + n2) % 2
    print('O número é par' if resto == 0  else 'O número é impar')
    print('O número é negativo' if n1 < 0 and n2 < 0 else 'O número é positivo')
elif op == 'D':
    print('{} / {} = {}'.format(n1, n2, n1 / n2))
    resto = (n1 + n2) % 2
    print('O número é par' if resto == 0  else 'O número é impar')
    print('O número é negativo' if n1 < 0 and n2 < 0 else 'O número é positivo')
elif op == 'U':
    print('{} - {} = {}'.format(n1, n2, n1 - n2))
    resto = (n1 + n2) % 2
    print('O número é par' if resto == 0  else 'O número é impar')
    print('O número é negativo' if n1 < 0 and n2 < 0 else 'O número é positivo')
