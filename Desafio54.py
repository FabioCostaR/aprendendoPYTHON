#Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade, e quantas ja são maiores.
from datetime import date
menor=0
maior=0

for c in range(0,7):
    ano = int(input(f'Qual é o ano de nascimento da {c+1}° pessoa? '))
    if ano > date.today().year or date.today().year -ano>130:
        print('Verifique o ano digitado.')
        quit()
    else:
        if date.today().year - ano < 18:
            menor+=1
        else:
            maior+=1
print(f'Temos, com base nos anos que foram digitados: {menor} pessoas Menores e \n '
      f'{maior} pessoas que já atingiram a maioridade.')
