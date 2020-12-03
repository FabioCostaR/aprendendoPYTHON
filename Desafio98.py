#Faça um programa que tenha uma função chamada contador(), que receba três
#parametros: inicio, fim e passo e realize a contagem.
#Seu programa tem que realizar três contagens através da funçao criada:
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem com inicio, fim e passo personalizado.
from time import sleep
def lin():
    print('=='*20)
def contador(inicio,fim,passo):
    lin()
    print('Contando de 1 até 10, de 1 em 1')
    for c in range (1,11):
        print(f'{c }',end='-')
        #sleep(1)
    print ('FIM!')
    lin()
    print('Contando de 10 até 0, de 2 em 2')
    for d in range(10,-2,-2):
        print(f'{d }', end='-')
       # sleep(1)
    print('FIM')
    lin()
    for e in range (inicio,fim+1,passo):
        print(f'{e }', end='-')
        #sleep(1)
    print('FIM')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
if passo==0:
    passo=passo+1
if inicio>fim and passo>0:
    passo=passo*-1
contador(inicio,fim,passo)