'''
print('lero lero')
'''
#Modelo de código criado por Vínicius Chagas

# criação das variáveis iniciais
os_aberta = False
modal_escolhido = ""
os_enviada = False
remocao_realizada = False
entrega_realizada = False

# menu principal
while True:
    print("===== MENU PRINCIPAL =====")
    print("1 - Abrir Ordem de Serviço")
    print("2 - Escolher modal de atendimento")
    print("3 - Enviar OS para Prestador de Serviço")
    print("4 - Realizar Remoção da bicicleta do cliente (Ponto A)")
    print("5 - Entregar a bicicleta do cliente (Ponto B)")
    print("0 - Encerrar atendimento")

    opcao = input("Digite a opção desejada: ")

    # opção 1 - Abrir Ordem de Serviço
    if opcao == "1":
        if not os_aberta:
            print("Ordem de Serviço aberta.")
            os_aberta = True
        else:
            print("Já existe uma Ordem de Serviço aberta.")
    
    # opção 2 - Escolher modal de atendimento
    elif opcao == "2":
        if os_aberta:
            modal_escolhido = input("Digite o modal de atendimento escolhido: ")
            print(f"Modal de atendimento escolhido: {modal_escolhido}")
        else:
            print("Abra uma Ordem de Serviço primeiro.")
    
    # opção 3 - Enviar OS para Prestador de Serviço
    elif opcao == "3":
        if os_aberta and modal_escolhido != "" and not os_enviada:
            print("Ordem de Serviço enviada para Prestador de Serviço.")
            os_enviada = True
        elif not os_aberta:
            print("Abra uma Ordem de Serviço primeiro.")
        elif modal_escolhido == "":
            print("Escolha um modal de atendimento primeiro.")
        else:
            print("Ordem de Serviço já enviada.")
    
    # opção 4 - Realizar Remoção da bicicleta do cliente (Ponto A)
    elif opcao == "4":
        if os_aberta and modal_escolhido == "Guincho" and os_enviada and not remocao_realizada:
            print("Remoção da bicicleta realizada.")
            remocao_realizada = True
        elif not os_aberta:
            print("Abra uma Ordem de Serviço primeiro.")
        elif modal_escolhido != "Guincho":
            print("Modal de atendimento não é Guincho.")
        elif not os_enviada:
            print("Envie a Ordem de Serviço para o Prestador de Serviço primeiro.")
        else:
            print("Remoção da bicicleta já realizada.")
    
    # opção 5 - Entregar a bicicleta do cliente (Ponto B)
    elif opcao == "5":
        if os_aberta and modal_escolhido == "Guincho" and os_enviada and remocao_realizada and not entrega_realizada:
            print("Entrega da bicicleta realizada.")
            entrega_realizada = True
        elif not os_aberta:
            print("Abra uma Ordem de Serviço primeiro.")
        elif modal_escolhido != "Guincho":
            print("Modal de atendimento não disponível.")
