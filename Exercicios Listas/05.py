# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores. 
import os
vetor = []
par = []
impares = []

for i in range(20):
    numero = int(input("Digite um numero: "))
    vetor.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impares.append(numero)
os.system("cls") ##### LIMPAR TERMINAL ANTES DE IMPRIMIR OS VALORES
print("O vetor é: ",vetor)
print("O vetor PAR é: ",par)
print("O vetor IMPARES é: ",impares)
