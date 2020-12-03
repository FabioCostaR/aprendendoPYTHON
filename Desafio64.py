#Crie um programa que leia varios numeros inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final mostre quantos numeros foram digitados e qual foi a soma entre eles.
nume = int ( input('Entre com o primeiro numero inteiro: '))
c=1
soma=0
while nume!=999:
    soma=soma+nume
    c+=1
    nume= int(input('Entre com um numero inteiro / Para encerrar digite 999: '))
print(f'A soma dos numeros digitados é: {soma} \n'
      f'foram digitados {c-1} numeros.')