#Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa. 
#O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o emprestimo será negado.

valor = float(input(' Digite o valor da casa R$ '))
salario = float(input(' Digite valor do salário do comprador R$ '))
anos = float(input(' Digite a quantidade de anos em que se pretende fazer o pagamento '))

prestacao = valor/(anos*12)
limite = salario*0.3

if prestacao > limite:
    print (f' prestação R${prestacao:.2f} > limiteR${limite:.2f}')
    print(' Sua prestação {} RECUSADA'.format('\033[01;31m'))
elif prestacao <= limite:
    print ( f'prestação R${prestacao:.2f} < = limite R${limite:.2f}')
    print(' Sua prestação {} APROVADA '.format('\033[01;32m'))
    print(f' O pagamento sera feito em {anos*12:.0f} parcelas de R${prestacao:.2f} ')