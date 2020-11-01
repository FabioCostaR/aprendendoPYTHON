#Crie um programa que faça o computador jogar JoKenPô com você
import emoji
import random
from time import sleep
print ('='*20)
op = int(input(emoji.emojize('CHOISE YOUR DESTINY :\n'
               '====================\n'
               '\033[01;31m [ 0 ] \033[m PEDRA :raised_fist:\n'
               '\033[01;33m [ 1 ] \033[m PAPEL :raised_hand:\n'
               '\033[01;36m [ 2 ] \033[m TESOURA :victory_hand:\n'
                             'Qual é sua jogada ? ')))
op2 = random.randint(0,2)
if op==0:
    OPA = str(emoji.emojize('PEDRA :raised_fist:'))
    if op2==0:
        OPB = str(emoji.emojize(':raised_fist: PEDRA'))
        resultado = str('\033[01;34m EMPATE')
    elif op2==1:
        OPB = str (emoji.emojize(':raised_hand: PAPEL'))
        resultado = str('\033[01;34m COMPUTADOR VENCEU')
    elif op2==2:
        OPB = str (emoji.emojize(':victory_hand: TESOURA'))
        resultado = str('\033[01;34m VOCÊ VENCEU')
if op==1:
    OPA = str (emoji.emojize(' PAPEL :raised_hand:'))
    if op2==1:
        OPB = str (emoji.emojize(':raised_hand: PAPEL'))
        resultado = str('\033[01;34m EMPATE')
    elif op2==2:
        OPB = str (emoji.emojize(':victory_hand: TESOURA'))
        resultado = str('\033[01;34m COMPUTADOR VENCEU')
    elif op2==0:
        OPB = str(emoji.emojize(':raised_fist: PEDRA'))
        resultado = str('\033[01;34m VOCÊ VENCEU')
if op==2:
    OPA = str (emoji.emojize('TESOURA :victory_hand:'))
    if op2==2:
        OPB = str (emoji.emojize(':victory_hand: TESOURA'))
        resultado = str('\033[01;34m EMPATE')
    elif op2==0:
        OPB = str(emoji.emojize(':raised_fist: PEDRA'))
        resultado = str('\033[01;34m COMPUTADOR VENCEU')
    elif op2==1:
        OPB = str (emoji.emojize(':raised_hand: PAPEL'))
        resultado = str('\033[01;34m VOCÊ VENCEU')
else:
    print(emoji.emojize('DEEEEERR :middle_finger:'))
    quit()
#lançamento
sleep(1)
print ('JO')
sleep(2)
print('KEN')
sleep(1)
print('PÔ')
sleep(0.5)
#resultado
print('\033[1;32m =- \033[m'* 12)
print (f'\033[31m VOCÊ {OPA} \033[m x \033[34m{OPB} COMPUTADOR \033[m \n'
       f'         \033[01;35;40m{resultado} \033[m')
print('\033[1;32m =- \033[m'* 12)


