# Solicita os dados
valor_horas = float(input('Informe o valor da hora trabalhada: '))
quantidade_horas = float(input('Informe a quantidade de horas trabalhadas no mes:'))

# Calcula o salario bruto
bruto = valor_horas * quantidade_horas

# Calcula o imposto de renda
if bruto > 2500:
    aliquotaIR = 20
elif bruto > 1500:
    aliquotaIR = 10
elif bruto > 900:
    aliquotaIR = 5
else:
    aliquotaIR = 0

valorIR = bruto * (aliquotaIR / 100.0)

# Calcula o valor para o sindicato
valorSindicato = bruto * (3 / 100.0)

# Calcula o total de descontos
totalDescontos = valorIR + valorSindicato

# Calcula o valor do FGTS
valorFGTS = bruto * (11 / 100.0)

# Calcula o salario liquido
salarioLiquido = bruto - totalDescontos

# Imprime o resultado
print ('Salario Bruto: (', valor_horas, '*', quantidade_horas, '): R$',bruto)
print ('(-) IR (', aliquotaIR, '%): R$', valorIR)
print ('(-) Sindicato ( 3 %): R$', valorSindicato)
print ('FGTS ( 11 %): R$', valorFGTS)
print ('Total de Descontos: R$', totalDescontos)
print ('Salario Liquido: R$', salarioLiquido)