# 17 - Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto. 
from calendar import isleap # Importa a biblioteca calendar e a função isleap para verificar se o ano é bissexto ou não
ano = int(input("Informe o ano: "))
if isleap(ano):
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")
