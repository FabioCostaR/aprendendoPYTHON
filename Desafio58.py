#Melhore o jogo Desafio028 onde o computador vai pensar em um numero entre 0 e 10
#So que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.
from random import randint
escolhaPC = randint(1,10)
jogada = 1
user = int(input('Escolha um numero entre 1 ate 10 '))
if user>=1 and user<=10:
    while escolhaPC != user:
        user = int(input('ERROU !!! Escolha um numero entre 1 ate 10 :'))
        jogada+=1
        if user <=1 or user>=10:
            print('FIM DE JOGO \n'
                  'VOCÊ PERDEU !!!')
            quit()
else:
    print('Escolha inválida')
    quit()
print(f'Você acertou em {jogada}jogadas !!!')
print('FIM')