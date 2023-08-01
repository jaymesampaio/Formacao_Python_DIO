##############################
# PROJETO SISTEMA BANCÁRIO
##############################

menu = """
==============================   MENU  =============================
                        [d] - Depositar
                        [s] - Sacar
                        [e] - Extrato
                        [q] - Sair
===================================================================
"""

saldo = 0
LIMITE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao  = input(menu)

    if opcao == "d":
        valor = float(input("Valor do deposito: R$ "))

        if valor > 0:
            print(f"Operação realizada com sucesso! Depósito de R$ {valor:.2f}\n")
            saldo += valor
            extrato += f"Depósito R$ {valor:.2f} (+)\n"

        else:
            print("O valor informado deve ser maior do que zero. Tente novamente.")
    
    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES: 
            print(f"Erro. Limite diário de {LIMITE_SAQUES} saques atingido. Volte amanhã.")

        else:

           valor = float(input("Valor do saque: R$ "))

           if valor > LIMITE:
               print(f"Erro. O valor máximo de saque é de R$ {LIMITE}. Tente novamente.")

           elif valor > saldo:
               print("Erro. Saldo suficiente.")

           elif valor > 0:
               print(f"Saque realizado. R$ {valor:.2f}\n")
               saldo -= valor
               numero_saques += 1
               extrato += f"Saque    R$ {valor:.2f} (-)\n"

           else:
               print("Erro. O valor inválido.")

    elif opcao == "e":
        print("======================== E X T R A T O =======================")
        print(extrato)
        print(f"------------------------")
        print(f"Saldo:   R$ {saldo:.2f}")
        print("==============================================================")

    elif opcao == "q":
        break
    
    else:
        print("Operação inválida. Por favor selecione novamente a opção desejada.")