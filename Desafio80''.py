#Crie um programa em que o usuario possa digitar 5 valores númericos e cadastre
#em uma lista. Já na posição correta de inserção (sem usar o sort()).
# No final mostre a lista ordenada.
lista =[]
for c in range(0,5):
    num = int(input('Insira o valor: '))
    if c==0 or num > lista[-1]:
        lista.append(num)
    else:
        pos=0
        while pos<len(lista):
            if num<=lista[pos]:
                lista.insert(pos,num)
                break
            pos+=1
            
print(lista)


