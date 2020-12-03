#Refaça o Desafio 009, mostrando a tabuada de um numero que o usuário escolher.
#Usando o laço for.
nume = int(input('Insira o numero do qual você deseja obter a tabuada: '))
for c in range (0,11):
    resul = nume * c
    print(f'\033[01;34m {nume} x {c} = {resul}')