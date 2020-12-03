#Faça um programa que mostre a tabuada de vários numeros, um de cada vez,
# para cada valor digitado pelo usuario.
# O programa só será interrompido quando o numeros solicitado for negativo.

while True:
    n = int (input('Quer ver a tabuada de qual valor? '))
    c=1
    print('-=' * 20)
    if n<0:
        break
    for c in range (c,11):
        print(f'{n} x {c} = {n*c}')
    print('-=' * 20)
print('Programa TABUADA \n'
       '***ENCERRADO*** \n'
      '!!! Volte Sempre !!!')

