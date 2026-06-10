def EcoSort():
    print("🤖  EcoSort iniciado. Digite 'sair' para encerrar ou 'ajuda' para mais informações.")
    print("----- BEM VINDO AO EcoSort. -----")
    
   
    total_pcts = 0
    faturamento = 0.0
    leves = 0
    padroes = 0
    pesados = 0
   
    
    while total_pcts < 10:
        print(f"\n----- Pacote {total_pcts + 1} de 10 -----")
        entrada = input("Digite o peso em kg (ou 'sair':) ").strip().lower()
        
        if entrada == 'sair':
            break
    
        try:
            peso = float(entrada)
        except ValueError:
            print("Peso inválido! Digite um número.")
            continue
            

        if peso <= 2.0:
            classificacao = "Leve"
            custo = 10.00
            leves += 1
        elif peso <= 10.0:
            classificacao = "Padrão"
            custo = 20.00
            padroes += 1
        else:
            classificacao = "Pesado"
            custo = 30.00
            pesados += 1
            
        print("[1] Internacional (+20%) | [2] Nacional")
        destino = input("> ").strip()
        
        if destino == '1':
            custo = custo * 1.20
            
       
        faturamento += custo
        total_pcts += 1
        print(f"Registrado: R$ {custo:.2f}")

    
    print("\n ======== RELATÓRIO FINAL ========")
    print(f"Total de pacotes: {total_pcts}")
    print(f"Carga total: {}")
    print(f" Leves: {leves} | Padrões: {padroes} | Pesados: {pesados}")
    print(f" Faturamento: R$ {faturamento:.2f}")
    print(f"Ticket médio por pacote: {}")
    print("==================================")


EcoSort()