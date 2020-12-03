#Crie um programa onde 4 jogadores joguem um dado e tenham resultados
#aleatórios. Guarde esses resultados em um dicionário. No final coloque esse
#dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
p1 = randint(1,6)
p2 = randint(1,6)
p3 = randint(1,6)
p4 = randint(1,6)
resultado={'p1':p1, 'p2':p2, 'p3':p3, 'p4':p4}
for k, v in resultado.items():
    print(f'Jogador {k} lançou o dado.',end='')
    for c in range(0,2):
        sleep(2)
        print('.', end='')
    print(f' \n O jogador {k} tirou {v}')
clas=[]
clas = sorted(resultado.items(), key=itemgetter(1), reverse=True)
print('')
sleep(2)
print('='*10,'CLASSIFICAÇÃO', '='*10)
for i, v in enumerate(clas):
    print(f' {i+1}° Lugar: Jogador {v[0]} com {v[1]} pontos')