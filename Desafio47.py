# Crie um programa que mostre na tela todos os numeros pares que estão no intervalo entre 1 e 50
inicio = int(input('Qual é o inicio do intervalo? '))
fim = int(input('Qual é o ponto final do intervalo? '))
if inicio % 2 == 0  :
    for c in range (inicio, fim+1, 2) :
        print(c)
else:
    inicio=inicio+1
    for c in range(inicio, fim+1,2):
        print (c)