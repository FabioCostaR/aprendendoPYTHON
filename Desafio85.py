#Crie um programa onde o usuário possa digitar 7 valores numericos e
#cadastre-os em uma unica lista que mantenha separados valores pares e impares.
#No final, mostre os valores pares e impares em ordem crescente.
lista=[]
par=list()
impar=list()
for c in range (0,7):
    num=int(input('Entre com um valor?: '))
    lista.append(num)
for c in range(0,7):
    if lista[c]%2==0:
        par.append(lista[c])
    else:
        impar.append(lista[c])
par.sort()
impar.sort()
print(lista)
print(par)
print(impar)