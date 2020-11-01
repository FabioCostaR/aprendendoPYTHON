#Escreva um programa que leia um numero inteiro qualquer e para para o usuario escolher a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

nume = int( input( "Entre com um numero inteiro : "))
opcoes = int(input('Escolha uma das opções: \n'
      'Digite \033[01;31m [1] \033[m para base binário \n'
      'Digite \033[01;32m [2] \033[m para base octal \n'
      'Digite \033[01;34m [3] \033[m para base hexadecimal \n'
      'Sua opção é : '))

if opcoes==1:

    print (f' {nume} = {bin(nume)[2:]} na base binária')
elif opcoes==2:

    print(f'{nume} = {oct(nume)[2:]} na base octal')
elif opcoes==3:

    print(f'{nume} = {hex(nume)[2:]} na base hexadecimal')
else:
    print ('\033[01;37m OPÇÃO INVÁLIDA')
print('\033[01;34m * * * FIM * * *')