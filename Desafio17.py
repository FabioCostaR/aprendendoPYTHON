#faca um programa que leia o valor dos catetos de um triangulo retangulo e calcule o valor da hipotenusa

import math
op = float(input('Entre com o valor do cateto oposto a hipotenusa : '))
ad = float(input("Entre com o valor do cateto adjacente a hipotenusa : "))
hip = math.sqrt(math.pow(op,2)+math.pow(ad,2))
print(hip)