#Faça um programa que jogue par ou impar . O jogo só será interrompido quando o
#jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
c=s=0

print('-='*20,'\n'
       '      VAMOS JOGAR PAR OU IMPAR \n'
        '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
while True:
    user = int(input('Diga um valor: '))
    pc = randint(1,2)
    user1 = str(input('Par ou impar [P/I]? ')).strip().upper()
    s=user+pc
    if s%2==0 and user1=='I':
        print(f'Você jogou {user} e o computador jogou {pc} \n'
              f'Total : {user+pc} \n'
              f'Deu PAR')
        print('VOCÊ PERDEU !!!')
        break
    elif s%2!=0 and user1=='P':
        print(f'Você jogou {user} e o computador jogou {pc} \n'
              f'Total : {user + pc} \n'
              f'Deu IMPAR')
        print('VOCÊ PERDEU !!!')
        break
    elif s%2==0 and user1=='P':
        print(f'Você jogou {user} e o computador jogou {pc} \n'
              f'Total : {user + pc} \n'
              f'Deu PAR')
        print('VOCÊ GANHOU !!!')
        c+=1
    elif s%2!=0 and user1=='I':
        print(f'Você jogou {user} e o computador jogou {pc} \n'
              f'Total : {user + pc} \n'
              f'Deu IMPAR')
        print('VOCÊ GANHOU !!!')
        c += 1
print(f'Você ganhou {c} vezes')
