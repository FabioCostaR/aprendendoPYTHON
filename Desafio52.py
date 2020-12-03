#Faça um programa que leia um número inteiro e diga se ele é primo ou não.
nume = int(input('Entre com um numero inteiro qualquer: '))
soma=0
for x in range(2,nume):
    if nume%x==0:
        print(f'\033[01;32m {x}', end="")
        soma=soma+1
    else:
        print(f'\033[34m {x}\033[m', end="")
if soma==0:
    print(f'\n {nume} tem {soma} divisores, portanto \033[01;35m É PRIMO')
else:
    print(f'\n {nume} tem {soma} divisores, portanto \033[01;32m NÃO É PRIMO')





