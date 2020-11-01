# Faça um programa que pergunte a distancia de uma viagem em KM
## Calcule o preço da passagem, cobrando R$0,50 por Km em viagens até 200km e
# R$ 0,45 para viagens mais longas
km = float(input('Qual a distancia da viagem ? '))
if km<=200 :
    valor = float(km * 0.5)
    print(f'O valor da sua viagem é de R${valor:.2f}')
else :
    custo = float(km*0.45)
    print(f'O valor da sua viagem é de R${custo:.2f}')