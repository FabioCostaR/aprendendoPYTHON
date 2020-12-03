#Melhore o desafio061, perguntando para o usuario se ele quer mostrar mais termos. O programa
#encerra quando ele disser que quer 0 termos.
sair=0
while sair!=2:
    a1 = int(input(' Insira o primeiro termo da Progressão Aritmética: '))
    q = int(input(' Insira a razão da PA: '))
    n = int(input(' Insira o número de termos desejados: '))
    c = 0
    while c < n:
        a = a1 + c * q
        print(f'{a} ', end='')
        print(',', end='' if c < n - 1 else '\n')
        c += 1
    sair = int(input('Você deseja: \n'
                     '[1] CONTINUAR \n'
                     '[2] SAIR \n'
                     'Você selecionou: '))
print('FIM do algoritmo')