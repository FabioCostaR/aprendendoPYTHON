#Desenvolva uma lógica que leia o peso e altura de uma pessoa
#calcule seu IMC e mostre seu status de acordo com a tabela abaixo.
#Abaixo de 18.5 abaixo do peso
#Entre 18.5 e 25 peso ideal
#25 ate 30 sobrepeso
#30 ate 40 obesidade
#acima de 40 obesidade mórbida

peso = float(input('Qual é seu peso em kg? '))
altura = float(input('Qual é sua altura em metros? '))
IMC = peso/(altura**2)

print(IMC)

if IMC<18.5 and IMC>0:
    print('Você está abaixo do peso')
elif IMC>=18.5 and IMC<25:
    print('Você está no peso ideal')
elif IMC>=25 and IMC<30:
    print('Você está com sobrepeso')
elif IMC>=30 and IMC<40:
    print('Você está obeso')
else:
    print('Você está com obesidade morbida')