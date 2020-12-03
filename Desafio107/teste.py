#Crie um módulo chamado moeda.py que tenha as funçoes incorporadas
#aumentar(),diminuir(),dobro() e metade().
#Faça também um programa que importe esse modulo e use alguas dessas funções.
import moeda

p=float(input('Digite o preço: '))
print(f'A metade de {(p)} \n')
      f'O dobro de {(p)} e {moeda.dobro(p)} \n'
      f'Aumentando 10%, temos {moeda.aumentar(p,10)} \n'
      f'Reduzindo 13%, temos {moeda.diminuir(p,13)}')