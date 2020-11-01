#Faça um programa que leia o ano de nascimento e de acordo com sua idade, diga:
# Se ele ainda vai se alistar no serviço militar
# Se é a hora de se alistar
# Se já passou do tempo do alistamento
# O programa deve mostrar o tempo que falta ou que passou do prazo do alistamento.
from datetime import date
atual = date.today().year
ano = int(input('Qual é o ano do seu nascimento ? \n'))
if (atual-ano)>=0 and (atual-ano)<18:
    print ('Você ainda vai se alistar, faltam {} anos'.format(18-(atual-ano)))
elif (atual-ano)>=0 and (atual-ano)>18:
    print('Seu tempo de se alista já passou a {} anos'.format((atual-ano)-18))
elif(atual-ano)>=0 and (atual-ano)==18:
    print(' É hora de se alistar.')
else:
    print(' Você ainda nem nasceu!!! ')