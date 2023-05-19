#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). 
tamanho = float(input("Tamanho do Arquivo em MB: "))
velocidade = float(input("Velocidade de Download em Mbps: "))
velocidade_download = velocidade / 8
tempo_download = (tamanho / velocidade_download) / 60
print(f"Com uma internet de {velocidade} Mbps voce vai baixar o arquivo de {tamanho}MB em {tempo_download}")
