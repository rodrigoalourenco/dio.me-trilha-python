MENU = """ ***

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
 
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(MENU)

    if opcao == "d":
        print("\n=============== DEPÓSITAR ===============")
        valor = float(input("Insira o valor do deposito: =>"))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O Valor informado é inválido!!!")
    elif (opcao == "s"):
        print("\n=============== SACAR ===============")
        valor = float(input("Insira o valor do saque: =>"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques-= 1
        else:
            print("Operação falhou! O Valor informado é inválido!!!")

    elif (opcao == "e"):
        print("\n=============== EXTRATO ===============")
        print("Não foram realizadas moviventações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("\n=======================================")
    
    elif (opcao == "q"):
        print("\n=============== SAIR ===============")
        break

    else:
        print("Operação invalida, por favor selecione novamente a oparação desejada.")
