#Faça um algoritmo que leia o salário de uma funcionário e mostre seu novo salário, com 15% de aumento
n = float(input(' Qual é o valor do salario do funcionário? R$ '))
n1 = float(input(' Qual é a porcentagem de aumento que esse funcionário receberá?'))
aum = (n*n1)/100
print(f'O funcionário recebe atualmente R${n:.2f} \n'
      f' Ele receberá um aumento de {n1}% \n'
      f' Com isso ele passará a receber R${n+aum:.2f} \n' )