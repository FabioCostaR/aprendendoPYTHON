#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores
#lidos pelo teclado.
#No final, mostre a matriz tela, com formulação correta.
matriz=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(0,3):
    for j in range(0,3):
        matriz[i][j]=int(input(f'Para a posição [{i+1},{j+1}] entre com o valor :'))
for i in range(0,3):
    for j in range(0,3):
        print(f' [{matriz[i][j]:^7}]', end='')
    print()
