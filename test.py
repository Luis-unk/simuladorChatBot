def opcoes():
    print("(1) - Consultar saldo")
    print("(2) - Verificar Extrato")
    print("(3) - Como bloquear algum cartão?")
    print("(4) - Sair")

tipo = True

while(tipo):
    try:
        opcoes()
        opcao = int(input("Digite aqui: "))
    
        if(opcao == 1):
            print("3000,00")
        elif(opcao == 2):
            print("===EXTRATO===")
        elif(opcao == 3):
            print("Segue passo a passo:")
        elif(opcao == 4):
            print("Volte Sempre!")
            tipo = False
        else:
            print("Opção invalida, Tente novamente")  
            
    except ValueError:
        print("Você precisa digitar um número Inteiro!")
  
