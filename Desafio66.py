#Crie um programa que leia vários números inteiros pelo teclado.
#O programa so para quando o usuario digitar 999, que é condição de parada.
# No final, mostre quantos numeros foram digitados e qual foi a soma entre eles.
#Desconsiderando o flag.
cont = soma =0
while True:
    n = int (input('Digite um valor (use 999 para parar): '))
    if n == 999:
        break
    soma+=n
    cont+=1

print(f'A soma dos valores digitados é {soma} \n'
      f'Foram digitados {cont} numeros.')
