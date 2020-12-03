#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade
# da digitação de um número de tipo inválido. Aproveite e crie também uma função
# leiaFloat() com a mesma funcionalidade

def leiaInt(msg):
    while True:
        try:
           n= int(input(msg))
        except(ValueError,TypeError):
            print('\033[31m ERRO !!!  \n Por Favor, digite um número inteiro válido\033[m')
        except(KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário')
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            real=float(input(msg))
        except(ValueError,TypeError) :

            print(f'\033[31m ERRO !!!  \n Por Favor, digite um número real válido\033[m  ')
            print('\033[31m ERRO !!!  \n Por Favor, digite um número real válido\033[m')
            return 0
        else:
            return real


#Programa prinpal
inteiro=leiaInt('Digite um n° Inteiro: ')
real=leiaFloat('Digite um n° Real: ')


print(f'O valor inteiro digitado foi {inteiro} e o valor real digitado foi {real}')
