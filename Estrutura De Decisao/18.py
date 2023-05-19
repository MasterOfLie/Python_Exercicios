# 18 - Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida. 
#from datetime import date # Importa a biblioteca datetime

dia = int(input("Informe o dia: "))
mes = int(input("Informe o mes: "))
ano = int(input("Informe o ano: "))

if dia <= 31 and dia >= 1 and mes <= 12 and mes >= 1 and ano <= 2021:
    print("Data válida")
    print(f"{dia}/{mes}/{ano}")
else:
    print("Data inválida")