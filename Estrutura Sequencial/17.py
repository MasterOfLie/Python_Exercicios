#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. 
import math as mt

metros = float(input("Metros Quadrados: "))

litros = mt.ceil(metros / 6)
litros_folga = mt.ceil(litros * 1.1)

# 18 LITROS

quantidade_l18 = mt.ceil(litros / 18)
preco_l18 = quantidade_l18 * 80
print(f"Para pintar {metros} metros, é necessário {quantidade_l18} litros de tinta de 18L, total de R${preco_l18}")

# 3,6 LITROS

quantidade_l36 = mt.ceil(litros / 3.6)
preco_l36 = quantidade_l36 * 25

print(f"Para pintar {metros} metros, é necessário {quantidade_l36} litros de tinta de 3,6L, total de R${preco_l36}")

# MIX
mix_18 = mt.floor(litros_folga / 18)  # Por questão de lógica, aqui faz mais sentido arredondar para baixo
mix_resto18 = litros_folga % 18
mix_36 = mt.ceil(mix_resto18 / 3.6)
preco_mix = (mix_18 * 80) + (mix_36 * 25)

print(f"Para pintar {metros} metros, é necessário {mix_18} litros de tinta de 18L e {mix_36} litros de tinta de 3,6L, total de R${preco_mix}")