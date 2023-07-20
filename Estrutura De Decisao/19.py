# 19 - Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo. 
n = int(input('Digite um número inteiro menor que 1000: '))
print('Quantidade de centenas: ', n // 100)
print('Quantidade de dezenas: ', (n % 100) // 10)
print('Quantidade de unidades: ', n % 10)