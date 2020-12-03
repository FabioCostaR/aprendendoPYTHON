# Faça um programa que tenha uma função chamada escreva(), que receba um texto
# qualquer como parametro e mostre uma mensagem com tamanho adaptável.
# Ex: escreval('Olá , mundo!)
# saida: ~~~~~~~~~~~~
#        Olá, mundo!
#	     ~~~~~~~~~~~~
def escreva(msg):
    print('~' * (len(msg)+4))
    print(f'  {msg}')
    print('~' * (len(msg)+4))


frase = str(input('Qual é a mensagem? '))
escreva(frase)
