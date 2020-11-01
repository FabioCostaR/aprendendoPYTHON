#Crie um programa que leia dois números e mostre a soma entre eles
num1 = float(input(' Entre com o primeiro valor: '))
num2 = float(input(' Entre com o segundo valor: '))
soma = num1+num2
print('{}{}{} + {}{}{} = {}{}{}'.format('\033[1;31m',num1,'\033[m','\033[1;32m',num2,'\033[m','\033[4;33m',soma,'\033[m'))