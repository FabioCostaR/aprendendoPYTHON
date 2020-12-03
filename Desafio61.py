#Refaça o desafio051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos,
#da progressão usando a estrutura while.
a1 = int(input(' Insira o primeiro termo da Progressão Aritmética: '))
q = int(input(' Insira a razão da PA: '))
n = int(input(' Insira o número de termos desejados: '))
c=0
while c<n:
    a = a1+c*q
    print(f'{a} ', end='')
    print(',', end='' if c<n-1 else '\n')
    c+=1
print('FIM')