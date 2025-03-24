menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 1000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\n========= O Valor foi depositado em sua coanta! =========\n")

        else:
            print("\n Operação falhou! O valor informado é inválido. \n")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\n Operação falhou! Você não tem saldo suficiente. \n")

        elif excedeu_limite:
            print("\n Operação falhou! O valor do saque excede o limite. \n")

        elif excedeu_saques:
            print("\n Operação falhou! Número máximo de saques excedido. \n")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\n========= O valor foi sacado de sua conta! =========\n")

        else:
            print("\n Operação falhou! O valor informado é inválido. \n")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "4":
        print("=========================================\n ORBIGADO PELA PREFERENCIA, VOLTE SEMPRE! \n=========================================")
        break

    else:
        print("\n Operação inválida, por favor selecione novamente a operação desejada. \n")
    