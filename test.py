from datetime import datetime

def opcoes():
    print("(1) - Consultar saldo")
    print("(2) - Verificar Extrato")
    print("(3) - Como bloquear algum cartão?")
    print("(4) - Sair")

tipo = True
data_atual = datetime.now()

while(tipo):
    try:
        opcoes()
        opcao = int(input("Digite aqui: "))
    
        if(opcao == 1):
            print(f"""
Consulta de Saldo - {data_atual.strftime("%d/%m/%Y")}

Agência: 0001
Conta: 123456-7

Saldo disponível: R$ 3.250,75
Limite do cheque especial: R$ 1.000,00

Saldo total disponível: R$ 4.250,75
""")
        elif(opcao == 2):
            print("""
Extrato da Conta - 03/05/2025

Saldo atual: R$ 3.250,75

Movimentações recentes:
------------------------------------------
Data       | Descrição                | Valor
------------------------------------------
03/05/2025 | Supermercado Bom Preço  | -R$ 125,40
02/05/2025 | Depósito                | +R$ 500,00
30/04/2025 | Conta de luz            | -R$ 89,30
------------------------------------------
""")
        elif(opcao == 3):
            print("""
Bloqueio de Cartão - Passo a Passo

Se você perdeu seu cartão ou suspeita de fraude, siga um dos passos abaixo para bloqueá-lo:

1 Pelo aplicativo:
   - Acesse o app do banco.
   - Vá em: Cartões > Gerenciar > Bloquear Cartão.
   - Confirme a solicitação com sua senha ou biometria.

2 Pela Central de Atendimento (24h):
   - Ligue para: 0800 123 4567
   - Escolha a opção "Bloquear cartão".
   - Tenha em mãos seu CPF para identificação.

3 Pelo site oficial:
   - Acesse sua conta pelo site do banco.
   - Vá até a área de Cartões > Bloqueio.
   - Siga as instruções na tela.

Dica de segurança:
Se houver suspeita de uso indevido, registre um boletim de ocorrência e comunique o banco imediatamente.

Seu cartão será cancelado e um novo será emitido.
"""

)
        elif(opcao == 4):
            print("Volte Sempre!")
            tipo = False
        else:
            print("Opção invalida, Tente novamente")  
            
    except ValueError:
        print("Você precisa digitar um número Inteiro!")
  
