# Faça um programa que tenha uma função chamada área(), que receba as dimensões
# de um terreno retangular[largura e comprimento] e mostre a área do terreno.
def lin():
    print('=--' * 10)


def Area(lar, comp):
    lin()
    print('Mede Terreno')
    lin()
    area = lar * comp
    print()
    print(f'A area do terreno é {area} m²')


a = float(input('Largura do Terreno: '))
b = float(input('Comprimento do Terreno: '))
Area(a, b)
