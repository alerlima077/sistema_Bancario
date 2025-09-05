menu = """
====== NOSSO BANCO S.A ======

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("✅ Depósito realizado com sucesso.")
        else:
            print("⚠️ Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= LIMITE_SAQUES

        if excedeu_saldo:
            print("⚠️ Operação falhou! Saldo insuficiente.")

        elif excedeu_limite:
            print(f"⚠️ Operação falhou! O limite por saque é de R$ {limite:.2f}.")

        elif excedeu_saques:
            print(f"⚠️ Operação falhou! Número máximo de saques excedido ({LIMITE_SAQUES}).")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1
            print("✅ Saque realizado com sucesso.")
        
        else:
            print("⚠️ Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato, end="")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================")

    elif opcao == "0":
        print("👋 Obrigado por usar o NOSSO BANCO S.A. Até logo!")
        break

    else:
        print("⚠️ Operação inválida, por favor selecione novamente a operação desejada.")
