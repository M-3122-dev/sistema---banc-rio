nome = str(input("Digite seu nome:")).title().strip()
for palavra in["da","de", "e", "dos", "a", "di", "do"]:
  nome= nome.replace(palavra.title(),palavra)


print(f"Olá {nome} essas são suas opções disponiveis\n")

print("MENU".center(50,"-"))
deposito = 0.00
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3


opcao = 0
while opcao == 0:
    print('''
    Para depósitar digite - [1]
    Para saque digite - [2]
    Para consultar o extrato atual digite - [3]
      ''')


    escolha = int(input("Qual e sua escolha?"))


    if escolha == 1:
        voltar_para_deposito = "s"
        while voltar_para_deposito == "s":
            novo_deposito = float(input("Digite o valor que você quer depósitar:"))
            if novo_deposito > 0:
              print(f"Você depositou: R${novo_deposito:.2f}, você confirma esse deposito? Digite (s para sim/ n para não):)")
              confirmacao = str(input("Digite sua escolha:")).lower()

              if confirmacao == "s":
                  deposito += novo_deposito
                  extrato += f"Deposito: +{novo_deposito:.2f}\n"
                  print(f"Seu deposito de: R${novo_deposito:.2f} foi feito")
                  print("Deseja mais alguma no nosso menu principal? Digite: 0 para sim ou 4 para não ")
                  opcao = int(input("Digite sua escolha:"))
                  if opcao == 4:
                    print(f"Muito obrigado {nome} por sua confiança")
                    exit()
                  elif opcao == 0:
                    break

              elif confirmacao == "n":
                print("Depósito cancelado, digite s para voltar para a aba de depósito:")
                voltar_para_deposito = str(input("Digite[s]:"))

            elif novo_deposito <= 0:
                print("Esse valor e inválido!")
                opcao = int(input("Digite [0] para voltar ao menu principal"))
                break


    elif escolha == 2:
      if numero_saque >= LIMITE_SAQUE:
        print("Você já realizou o limite de 3 saques diários.")
        opcao = int(input("Digite [0] para voltar ao menu:"))
      else:
        voltar_para_saque = 5
        while voltar_para_saque == 5:
          novo_saque = float(input("Digite o valor que você quer sacar?:"))

          if novo_saque > limite:
            print("Não é possível sacar um valor maior que R$500,00: digite [5] para voltar")
            voltar_para_saque = int(input("Digite:"))

          elif novo_saque > deposito:
            print(f"Não e possível sacar pois seu saldo atual é  de R${deposito:.2f}, volte até o menu e escolha a opção [1] para depósitar e ter saldo sulficiente")
            opcao = int(input("Digite [0] para voltar até o menu inicial:"))
            break

          elif novo_saque <= 0:
            print(f"Valor inválido, digite um numero maior que R$0,0")
            voltar_para_saque = int(input("Digite [5] para tentar novamente ou [0] para voltar ao menu principal"))
          else:
            print(f"Você confirma o saque de: R${novo_saque:.2f} digite s para sim/ n para não")
            confirmacao = str(input("Digite")).lower()

            if confirmacao == "s":
              deposito -= novo_saque
              numero_saque += 1
              extrato += f"Saque: -R${novo_saque:.2f}\n"
              print("Saque realizado com sucesso!")
              print("Deseja mais alguma coisa ? digite 4 para sair, digite 0 para voltar ao menu inicial ou 5 para fazer um novo saque")
              opcao = int(input("Digite"))
              if opcao == 4:
                print(f"Muito obrigado {nome} por sua confiança")
                exit()
              elif opcao == 5:
                voltar_para_saque = 5
              else:
                voltar_para_saque = 0

            else:
              print("Saque cancelar. Digite [5] para voltar ou [0] para menu")
              voltar_para_saque = int(input("Digite"))


    elif escolha == 3:
      print(" ")
      print("EXTRATO BANCÁRIO".center(50, "-"))

      if extrato == "":
        print(f"nenhuma movimentação realizada, saldo atual: R${deposito:.2f} e disponivel para saque: R${deposito:.2f}.")

      else:
        print(extrato)
        print(f"Saldo atual: R${deposito:.2f}")
        print("-" * 50)
        opcao = int(input("Digite [0] para voltar ao menu ou [4] para sair."))
        if opcao == 4:
          print(f"Muito obrigado {nome} por sua confiança!")
          break
