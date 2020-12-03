#Aprimore o desafio anterior, mostrando no final:
#A soma de todos os valores pares digitados.
#A soma dos valores da terceira coluna
#O maior valor da segunda linha
soma=coluna=maior=0
M=[[0,0,0],[0,0,0],[0,0,0]]
for i in range (0,3):
    for j in range(0,3):
        M[i][j]=int(input(f'Entre com o valor da posição [{i+1},{j+1}] :'))
        if M[i][j]%2==0:
            soma=soma+M[i][j]
print('=**'*10)
for i in range(0,3):
    for j in range(0,3):
        print(f'[{M[i][j]:^6}]', end='')
    print()
print('=**'*10)
print(f'A soma dos valores pares é {soma}')
for i in range(0,3):
    coluna+=M[i][2]
print(f'A soma dos elementos da terceira coluna é {coluna}')
for j in range(0,3):
    if j==0:
        maior=M[1][j]
    else:
        if maior<M[1][j]:
            maior=M[1][j]
print(f' o maior numero da segunda linha é {maior}')