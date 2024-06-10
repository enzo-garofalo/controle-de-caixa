import os 
import tabulate
from datetime import date, datetime

data = datetime.now().strftime("%d-%m-%y")
fluxo = {}


def abrir_caixa():
  os.system('cls')
  print('Caixa Aberto')
  inicio = float(input('Digite o inicio: '))

  fluxo[data] = [inicio , 0.0 ]
  return

def retirar():
    os.system('cls')
    print('Retirada')
    retirada = float(input('Digite o valor retirado: '))

    fluxo[data][1] = retirada

def menu():
    while True:
        os.system('cls')
        print('='*22, 'Menu', '='*22)
        print('-'*16, '| 1- Abrir Caixa  |', '-'*13)
        print('-'*16, '| 2- Retirar      |', '-'*13)
        print('-'*16, '| 3- Fechar Caixa |', '-'*13)
        print('='*50)
        escolha = int(input("O que deseja fazer? "))
        if escolha == 1:
            abrir_caixa()
        elif escolha == 2:
            retirar()
        elif escolha == 3:
            print('caixa fechado')
            print(fluxo)

            print('='*20,'Até Logo','='*20)
            exit()
        else:
            print("Digite uma opção válida!")
            continue


menu()