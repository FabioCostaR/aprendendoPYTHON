#Crie um programa que simule o funcionamento de um Caixa Eletronico.
#No inicio pergunte qual valor será sacado (INTEIRO)
#Programa vai informar quantas cédulas serão entregues de cada valor.
#Considere as cédulas de 50, 20, 10, e 1.
print('\033[01;32m = \033[m'*12)
print('\033[01;32m          BANCO SANPETER          \033[m')
print('\033[01;32m = \033[m'*12)
valor = int(input('Que valor você quer sacar? R$'))
valor50 = valor//50
resto50 = valor - (valor50*50)
valor20 = resto50//20
resto20 = resto50 - (valor20*20)
valor10 = resto20//10
resto10 = resto20 - (valor10*10)
valor1 = resto10
print(f'{valor50} notas de R$50.00') if valor50!=0 else ''
print(f'{valor20} notas de R$20.00')if valor20!=0 else''
print(f'{valor10} notas de R$10.00')if valor10!=0 else''
print(f'{valor1} notas de R$1.00') if valor1!=0 else''