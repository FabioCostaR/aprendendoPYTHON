#Faça um programa que tenha uma função chamada maior(), que receba vários parâmentros
#com valores inteiros
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior
from random import randint
lista=[]
def maior(lista):
    print(f'O maior numero é {max(lista)}')

a=randint(1,10)
for c in range (0,a):
    lista.append(randint(0,10))
print(f' Foram escolhidos {len(lista)} numeros, a saber{lista}, e ', end=' ')
maior(lista)


