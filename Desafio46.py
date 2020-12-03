#Faça um programa que mostre na tela uma CONTAGEM REGRESSIVA para estouro de fogos de artificio.
#indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep

print('PREPARE-SE PARA UMA GRANDE EXPLOSÃO !!!')
for c in range(10,0,-1):
    sleep(1)
    print(c)



print('\033[1;31m BUMMM!!! \033[m')