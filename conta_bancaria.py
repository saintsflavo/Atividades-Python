saldo = []
valor_extrato = []

def depositar_dinheiro():
    deposito = float(input("Insira o valor para depositar: "))
    
    if deposito > 0:
        saldo.append(deposito)
        print("\nDepósito realizado com sucesso!")
        print(f"Saldo atual: R$ {sum(saldo):.2f}")
    else:
        print("Valor inválido.")

def sacar_dinheiro():
    saque = float(input("Insira o valor para sacar: "))

    if saque > 0:
        if saque <= sum(saldo):
            saldo.append(-saque)
            print("\n Saque realizado com sucesso!")
            print(f"Saldo atual: R$ {sum(saldo):.2f}")
        else:
            print("Saldo insuficiente")
    else:
        print("Valor inválido")



def mostrar_extrato():
    print("\n ======= EXTRATO =======")
    
    if len(saldo) == 0:
        print("Não foram realizadas transações")
    else:
        for valor in saldo:
            if valor > 0:
                print(f"Depósito: R$ {valor:.2f}")
            else:
                print(f"Saque: R$ {abs(valor):.2f}")
    
    print(f"Saldo atual: {sum(saldo):.2f}")


opcao = None
while opcao != 0:
    print("")
    print("====== MENU INSANO ======")
    print("")
    print("1 - Depositar dinheiro")
    print("2 - Sacar dinheiro")
    print("3 - Mostrar extrato")
    print("0 - Sair")
    print("")

    
    entrada = (input("Digite a opção desejada: ")).strip()

     
    if entrada == "":
        print("")
        print("Escolha a opção desejada: ")
        continue
    
    if entrada.isdigit():
        opcao = int(entrada)
    else:
        print("-----Opção inválida-----")
        continue

    if opcao == 1:
        depositar_dinheiro()
    elif opcao == 2:
     sacar_dinheiro()
    elif opcao == 3:
        mostrar_extrato()
    elif opcao == 0:
     print("")
     print("Até a próxima!")
    else:
     print("-----Opção inválida-----")
