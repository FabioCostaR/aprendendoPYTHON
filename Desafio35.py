#Desenvolva um programa que leia o comprimento de três retas e dia ao usuario se
#elas podem ou não formar triangulo.

r1 = float(input('digite o tamanho da reta 1 :'))
r2 = float(input('digite o tamanho da reta 2 :'))
r3 = float(input('digite o tamanho da reta 3 :'))
print('-='*20)
if (r1<r2+r3) and (r2<r1+r3) and (r3<r1+r2):
    print('Essas retas formam um triangulo')
else:
    print('Essas retas não conseguem formar um triangulo')
print('-='*20)