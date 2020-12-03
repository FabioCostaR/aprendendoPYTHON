#Crie um programa que leia dois valores e mostre um menu na tela:
#1 somar 2 multiplicar 3 maior 4 novos numeros 5 sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
num1 = float(input('Entre com o primeiro valor: '))
num2 = float(input('Entre com o segundo valor: '))
escolha=0
while escolha !=5:
    escolha = int(input('ESCOLHA UMA DAS OPÇÕES: \n'
                        '   [1] SOMAR OS NÚMEROS \n'
                        '   [2] MULTIPLICAR OS NÚMEROS \n'
                        '   [3] CLASSIFICAR \n'
                        '   [4] INSERIR NOVOS NUMEROS \n'
                        '   [5] SAIR \n' \
                        'SUA ESCOLHA É : '))
    if escolha<1 or escolha>5:
        print('Opção INVÁLIDA .\n')
    elif escolha==1:
        soma = num1 + num2
        print(f'\033[01;33m {num1} + {num2} = {soma} \033[m')
    elif escolha==2:
        multi = num1 * num2
        print(f'\033[01;33m {num1} x {num2} = {multi} \033[m')
    elif escolha==3:
        if num1>num2:
            print(f'\033[01;33m {num1} > {num2} \033[m')
        elif num1<num2:
            print(f'\033[01;33m {num1} < {num2} \033[m')
        else:
            print(f'\033[01;33m {num1} = {num2} \033[m')
    elif escolha==4:
        num1 = float(input('Entre com um novo valor para o primeiro número: '))
        num2 = float(input('Entre com um novo valor para o segundo número: '))
print('======+ OPERAÇÃO FINALIZADA +=======')