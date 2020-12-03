#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os
# 10 primeiros termos dessa progressão.
a1 = int(input(' Qual é o primeiro termo dessa progressão ? '))
r = int(input(' Qual é a razão dessa progressão? '))
for n in range(0,10):
    an= a1 + n*r
    print(an)