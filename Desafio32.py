# Faça um programa que leia um ano qualquer e diga se ele é bissexto ou não.
ano = int(input('Entre com um ano qualquer: '))
if ano%4==0:
    if ano%100==0:
        if ano%400==0:
            print('O ano é bissexto (tem 366 dias).')
        else:
            print('O ano não é um ano bissexto (tem 365 dias)')
    else:
        print('O ano é bissexto (tem 366 dias).')
else:
    print('O ano não é um ano bissexto (tem 365 dias)')
