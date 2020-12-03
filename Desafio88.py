#Faça um programa que ajude um jogador da mega sena a criar palpites
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 numeros
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
num = int(input('Quanto palpites você deseja? '))
palpite=[]
lista=[]

total=0
#while total<= num:
while total<num:
    cont = 0
    while True:
        n = randint(1,60)
        if n not in palpite:
            palpite.append(n)
            cont+=1
        if cont>=6:
            break
    palpite.sort()
    lista.append(palpite[:])
    palpite.clear()
    total+=1
print('-=*'*10)
print('** PALPITES JOGOS MEGA SENA **')
print('-=*'*10)
print(f'      Seus {num} palpites são:')
print('_'*30)
for i, l in enumerate(lista):
    print(f'Jogo {i+1}: {l}')
    sleep(1)







    #sorteie 6 numeros/ cada palpite é uma lista de 6 numeros
#Mostre os palpites/ lista das listas palpites.
