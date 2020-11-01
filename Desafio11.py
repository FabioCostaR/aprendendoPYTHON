#Faça um programa que leia a largura e altura de uma parede em metros,
#calcule a sua área e a quantidade de tintas necessárias para pintá-la,
#sabendo que cada litro de tinta, pinta uma área de 2m²

l = float(input(" Qual é a largura da parede ? "))
comprimento = float(input(" Qual é o comprimento da parede ? "))
A = l * comprimento
l1 = A/2
print(f" Você gastará {l1} litros de tinta para pintar essa parede. ")