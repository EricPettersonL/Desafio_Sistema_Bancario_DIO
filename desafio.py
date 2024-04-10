# Regras do desafio
#Sistema simples de saque, deposito e extração de dinheiro
# Deposito 
    # só valores positivos
    # todos devem ser armazenados para vizualizar no extrato
    
# Saque
    # No maximo 3 saques de 500 por dia
    # Se não houver saldo, mostrar uma mensagem informando
    # todos devem ser armazenados para vizualizar no extrato
    
# Extrato
    # deve mostrar todos os movimentos
    # e no final mostrar o saldo atual
    
menu = "\nSelecione uma das opções: \n 1 - Depositar \n 2 - Sacar \n 3 - Extrato \n 4 - Sair \n"

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Quanto deseja depositar? "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("O valor precisa ser positivo!")
    elif opcao == "2":
        valor = float(input("Quanto deseja sacar? "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print("Saldo insuficiente!")
        elif excedeu_limite:
            print(f"Limite de saldo de R$ {limite:.2f} excedido!")
        elif excedeu_saques:
            print("Limite de saques diarios excedido!")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("O valor precisa ser positivo!")
    elif opcao == "3":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===============================")
    elif opcao == "4":
        break
    else:
        print("Operação inválida, tente novamente!")
        