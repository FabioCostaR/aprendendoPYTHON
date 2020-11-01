#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#e mostre quantos dólares ela pode comprar
#Considere US$ 1,00 = R$ 3,27

n = float(input("Qual a quantidade de dinheiro que você tem na carteira? R$ "))
d = n/5.59
print(f' R$ {n} corresponde a U$ {d} ')
