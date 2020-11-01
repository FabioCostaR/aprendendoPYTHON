#Faça um programa que leia três números e mostre qual é o maior e qual é o menor. Guanabara
a = int(input('primeiro numero: '))
b = int(input('segundo numero: '))
c = int(input('terceiro numero: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

print("O menor é {}".format(menor))

maior = a
if b>a and b>c :
    maior = b
if c>a and c>b :
    maior = c

print('O maior é {}'.format(maior))