#026: Faça um programa que leia uma frase pelo teclado
# mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez
# e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase :\n')).strip()
frase = frase.upper()
print('Aparece a letra A {} vezes'.format(frase.count('A')))
print('A letra A aparece por primeiro na posição {}'.format(frase.find('A')+1))
print('A letra A aparece por ultimo na posição {}'.format(frase.rfind('A')+1))