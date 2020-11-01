#027: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input(' Entre com o nome :\n')).strip()
nome = nome.split()
print(' O primeiro nome é {}'.format(nome[0]))
print(' O ultimo nome é {}'.format(nome[-1]))