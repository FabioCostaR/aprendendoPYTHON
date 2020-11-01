#Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo e todas a s informações possíveis

a = input ('Digite algo :')
print ('O tipo digitado é {}{}'.format('\033[01;36m',type(a)))
print ('O tipo digitado é numérico? {}{}'.format('\033[01;37m',a.isnumeric()))
print (' O tipo digitado só tem espaço ? {}{}'.format('\033[04;35m',a.isspace()))
print (' O tipo digitado só tem letras {}'.format(a.isalpha()))