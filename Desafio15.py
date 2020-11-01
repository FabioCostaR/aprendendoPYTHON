# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado.
dias = int(input(' O carro foi alugado por quantos dias ? '))
dias = float(dias)
km = float(input('O carro percorreu quantos quilometros? '))
valor = (dias*60)+(km*0.15)
print('Você pagará o valor de R$ {}{:.2f}'.format('\033[1;31m',valor))