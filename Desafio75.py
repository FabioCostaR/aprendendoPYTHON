#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
#No final mostre:
#Quantas vezes apareceu o numero 9
# Em que posição foi digitado o primeiro valor 3
#Quais foram os números pares.
v1= int(input('Entre com um valor entre 0 ~ 9:'))
v2= int(input('Entre com um valor entre 0 ~ 9:'))
v3= int(input('Entre com um valor entre 0 ~ 9:'))
v4= int(input('Entre com um valor entre 0 ~ 9:'))
valor=(v1,v2,v3,v4)
c=t=0
print(f'Você digitou {valor}')
for c in range(0,4):
    if valor[c]==9:
        t+=1
print(f'O número 9 apareceu {t} vezes')
if 3 in valor:
    print(f'O numero 3 apareceu na {valor.index(3)} posição ')
else:
    print('O numero 3 não apareceu.')

print('Os valores pares foram: ',end='')
for n in valor:
    if n%2==0:
        print(n ,end='  ')
    else:
        print('NENHUM')
        break

