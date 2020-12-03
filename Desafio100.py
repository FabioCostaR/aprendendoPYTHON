#Faça um programa que tenha uma lista chamada numeros e duas funçoes chamadas sorteia()
#e somaPar().A primeira função vai sortear 5 números e coloca-los dentro de uma lista
# e a segunda vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
numeros=[]
from random import randint
def sorteia(lista):
    print('Sorteando 5 valores da lista. \n')
    for c in range(0,5):
        n=randint(1,10)
        numeros.append(n)
        print(f'{n}', end=' ',flush=True)
    print('PRONTO!!!')
def somaPar(numeros):
    soma=0
    for valor in numeros:
        if valor % 2 == 0 :
            soma += valor
    print(f'A soma dos números pares é {soma}.')


sorteia(numeros)
somaPar(numeros)