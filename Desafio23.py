#023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
numero = int(input(' Inserte um numero entre 0 e 9999 : '))
u = (numero//1)%10
d = (numero//10)%10
c = (numero//100)%10
m = (numero//1000)%10
print(f'Esse numero possui: \n'
      f'{u} unidades \n'
      f'{d} dezenas \n'
      f'{c} centenas \n'
      f'{d} unidades de milhar \n')
