#Faça um programa que leia um numero qualquer e mostre seu fatorial.(a com while e b com o for)
from time import sleep
escolha=0
nume = int(input('Entre com o numero: '))
fat = 1
while escolha!=2:
    escolha = int(input('Escolha sua opção : \n'
                    '[1] Calculo do Fatorial pelo laço while. \n'
                    '[2] Calculo do Fatorial pelo laço for. \n'
                    '[3] SAIR \n'
                    
                    'Sua escolha é : '))
    if escolha<1 or escolha>2:
        print('Escolha Inválida')
    elif escolha==1:
        c = nume
        while c!=1:
            fat = fat*c
            sleep(1)
            print(f'{c}', end=' ')
            print(' x 'if c>1 else '=', end='')
            sleep(0.5)
            c-=1
        print(f'= {fat}')
        quit()

    elif escolha==2:
        for c in range (nume,1,-1):
            fat = fat*c
        print(f'{nume}! = {fat}')
        quit()
    else:
        print('FIM')
        quit()