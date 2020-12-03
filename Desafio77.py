#Crie um programa que tenha uma tupla com várias palavras (sem acento).
#Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.
palavras = ('encontro','indice', 'determinada', 'lista', 'passado', 'desejado','argumento')
for p in palavras:
    print(f' \n Na palavra "\033[01;32m {p.upper()}\033[m" temos: ', end='  ')
    for letra in p:
        if letra.lower()in 'aeiou':
            print(letra,end='  ')
