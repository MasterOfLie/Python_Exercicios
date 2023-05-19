#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: 
hora = float(input("Horas trabalhada: "))
salario = float(input("Salario por hora: "))

#salário bruto. 
salario_bruto = salario*hora
print("Salario Bruto: ",salario_bruto)

#IR
ir = salario_bruto *0.11
print("Voce pagou: ", ir ," De IR")

#INSS
inss = salario_bruto *0.08
print("Voce pagou: ", inss ," De INSS")
#quanto pagou ao sindicato. 
sindicato = salario_bruto * 0.05
print("Voce pagou: ", sindicato ," De Sindicato")

#o salário líquido. 
salario_liquido = salario_bruto - ir - inss - sindicato
print("Salario bruto: ", salario_bruto, "Salario liquido: ",salario_liquido)