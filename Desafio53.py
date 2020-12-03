 #Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando
#os espaços e acentos.
frase = str(input('Escreva uma frase: ')).strip().upper()
frase1 = frase.replace(' ','')
inverso=frase1[::-1]
if inverso == frase1:
    print(f'A Frase {frase} é um palindromo ')
else:
    print(f'A frase {frase} não é palindromo')