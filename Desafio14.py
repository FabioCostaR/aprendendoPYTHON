#Escreva um programa que converta um a temperatura digitada em ºC e converta para ºF
c = float(input(' Qual temperatura em Celsiu você deseja converter para Fahrenheit? '))
f = ((c*9)+160)/5
print('\033[1;32m {}°F'.format(f))