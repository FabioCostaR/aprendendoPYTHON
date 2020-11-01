#A Confederação Nacional de Nataçao precisa de um programa que leia o ano de nascimento de um atleta
#e mostre a sua categoria, de acordo com a idade:
#até 9 anos: Mirim
#até 14 anos: Infantil
#até 19 anos: Junior
#até 20 anos: Senior
#Acima: Master

from datetime import date
atual = date.today().year
ano = int(input(' Em qual ano você nasceu ? '))
idade = atual - ano

if idade<9:
    print(f'Sua idade é {idade}, portanto sua categoria é \033[01;32m MIRIM.')
elif idade>=9 and idade<14 :
    print(f'Sua idade é {idade}, portanto sua categoria é \033[01;32m INFANTIL')
elif idade>=14 and idade<19:
    print(f'Sua idade é {idade}, portanto sua categoria é \033[01;32m JUNIOR')
elif idade>=19 and idade<20:
    print(f'Sua idade é {idade}, portanto sua categoria é \033[01;32m SENIOR')
elif idade>=20:
    print(f'Sua idade é {idade}, portanto sua categoria é \033[01;32m MASTER')