#Crie um programa que tenha uma função fatorial() que receba dois parametros
#o primeiro indicando o numero a calcular e o outro chamado show, que será lógico(opcional),
#indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(num,show=False):
    """
    -> Essa definição apresenta o Fatorial de um número, de forma simples ou de forma expandida
    :param num: Inteiro
    :param show: Boleano. (mostrar modo expandido)
    :return: Fatorial
    """
    prod=1
    print(f'{num} != ',end=' ')
    for c in range(num, 0, -1):
        prod = prod * c
        if show:
            if c>=2:
                print(f'{c} x ',end=' ')
            if c==1:
                print(f'{c} = ',end=' ')
    return prod


numero=int(input('numero: '))
escolha=str(input('Deseja modo expandido?[S/N] ')).strip().upper()[0]
if escolha not in 'SN':
    escolha = str(input('Deseja modo expandido?[S/N] ')).strip().upper()[0]
if escolha == 'S':
    escolha=True
else:
    escolha=False
print(f'{ fatorial(numero,escolha)}')
