#Faça um programa que receba o valor de um angulo e calcule o seno, cosseno e tangente desse.
import math
ang = float(input("entre com o valor do angulo em graus"))
rad=math.radians(ang)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print(f'O seno vale {sen} o cosseno vale {cos} e a tangente vale {tan}')