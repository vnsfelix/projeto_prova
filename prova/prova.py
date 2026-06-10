def EcoSort():
 while True:
    print("-" * 50)
    print("🤖 EcoSort iniciado. Digite 'sair' para encerrar ou 'ajuda' para mais informações.")
    print("-" * 50)
    print("\nBem-vindo ao EcoSort!")
    
    entrada_peso = input("Qual seria o peso do pacote? (em kg): ").lower().strip()
    if entrada_peso == 'sair':
        print("Programa encerrado. Até logo!")
        break
        
    if entrada_peso == 'ajuda':
        print("\n AJUDA: Digite o peso do pacote usando números (ex: 2.5 ou 12).")
        print("Pesos até 2kg são Leves, até 10kg são Padrão e acima disso são Pesados.")
        continue

    try:
        peso = float(entrada_peso)
    except ValueError:
        print(" Peso inválido! Por favor, digite um número válido.")
        EcoSort()
        return

    if peso <= 2.0:
        classificacao = "Leve"
        custo_base = 10.00
    elif peso <= 10.0:
        classificacao = "Padrão"
        custo_base = 20.00
    else:
        classificacao = "Pesado"
        custo_base = 30.00

    print("\n--- Opções de Destino ---")
    print("[1] Destino Internacional")
    print("[2] Destino Nacional")
    print("[3] Voltar / Cancelar")
    
    escolha = input("> ").strip()
    
    if escolha == '1':
        custo_final = custo_base * 1.20
        print(f" Classificação: {classificacao} | Taxa Internacional: +20%")
        print(f" Custo Final: R$ {custo_final:.2f}")
    elif escolha == '2':
        print(f" Classificação: {classificacao}")
        print(f" Custo Final: R$ {custo_base:.2f}")
    elif escolha == '3':
        print("Voltando ao início...")
        EcoSort()
    else:
        print("Opção inválida! Reiniciando processo...")
        EcoSort()

EcoSort()
