#Escreva um programa que pergunte o salario de um funcionário e calcule o valor do aumento.
#Se salario superior a R$1250,00 calcule valor de 10%
# se salario menor que 1250,00 aumento de 15%
sal = float(input('Entre com o valor do salário :'))
if sal>1250:
    sal=(sal*0.1)+sal
else:
    sal=(sal*0.15)+sal
print("O novo salario será de {}".format(sal))