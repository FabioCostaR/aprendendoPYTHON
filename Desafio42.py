#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
#se elas podem ou não formar um triângulo. Se formar classificar em:
#Equilátero
#Escaleno
#Isosceles.

lado1 = float(input('Insira a medida do segmento 1 :'))
lado2 = float(input('Insira a medida do segmento 2 :'))
lado3 = float(input('Insira a medida do segmento 3 :'))
if lado1< lado2+lado3 and lado2<lado1+lado3 and lado3<lado1+lado2:
    print('Esses segmentos formam um triangulo.')
    if lado1==lado2 and lado1==lado3:
        print('Formam um triangulo EQUILÁTERO')
    elif lado1==lado2 and lado1!=lado3:
        print('Formam um triangulo ISÓSCELES.')
    elif lado2==lado3 and lado1!=lado2:
        print('Formam um triangulo ISÓSCELES.')
    else:
        print('Formam um triangulo ESCALENO')
else:
    print('Esses segmentos não formam um triangulo')