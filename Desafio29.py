#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h mostre uma mensagem dizendo que foi multado.
# A multa custara R$7,00 por cada km acima do limite.

velocidade = float(input("Entre com a velocidade do veiculo:  "))
if velocidade>80:
    print(" Velocidade superior ao permitido \n Você foi multado")
    multa = float((velocidade - 80)*7)
    print (f' Você pagará uma multa de R$ {multa:.2f}')
