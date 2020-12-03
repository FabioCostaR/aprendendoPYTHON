#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
#ao input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
#Ex: n=leiaInt('Digiteumn')
def leiaInt(msg):
    ok=False
    valor=0
    while True:
        num=str(input(msg))
        if num.isnumeric():
            valor=int(num)
            ok=True
        else:
            print('ERRO!!! Digite um número inteiro ')
        if ok:
            break
    return valor
#Programa principal
numero=leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {numero}')
