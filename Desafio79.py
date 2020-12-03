#Crie um programa em que o usuario possa digitar vários valores númericos e
#Cadastre-os em uma lista. Caso o numero já exista, ele não será adicionado.
#No final, serão exibidos todos os valores unicos digitados, em ordem crescente.
valores=list()
while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
       print('Valor adicionado com sucesso.')
       valores.append(num)
    else:
        print('Valor já encontrado na lista.')
    opcao = str(input('Deseja continuar? [S/N]? ')).strip().upper()[0]
    if opcao=='N':
        break
print(valores)