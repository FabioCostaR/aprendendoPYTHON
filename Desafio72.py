#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
#por extenso, de zero até vinte.
#Seu programa deverá ler um numero pelo teclado ( 0 ~20) e mostra-lo por extenso.
extenso=('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quize','dezesseis','dezesete','dezoito','dezenove','vinte')
valor = int(input('Digite um numero entre 0 ~ 20:'))
while valor<0 or valor>20:
    print('Tente novamente.')
    valor = int(input('Digite um numero entre 0 ~ 20:'))
print(f'Você digitou o numero {extenso[valor]}')