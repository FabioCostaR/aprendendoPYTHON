#Crie  um programa onde o usuario digite uma expressão que use parenteses.
#Seu aplicativo deverá analisar a se a expressão passada está com os parenteses abertos e
#Fechados na ordem correta.
exp=str(input('Digite a expressão: '))
pilha=list()
for simb in exp:
    if simb=='(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha)==0:
            pilha.append(')')
            break
        else:
            pilha.pop()
if len(pilha)==0:
    print('Expressão Válida')
else:
    print('Expressão Inválida')

