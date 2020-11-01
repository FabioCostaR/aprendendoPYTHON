#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

n1 = float(input("Entre com a medida em metros: "))
cm=n1*100
mm=n1*1000
print(f'{n1} metros corresponde a {cm} centimetros e a {mm} milimetros')