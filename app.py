from flask import Flask, request, jsonify, render_template, send_file
from flask_cors import CORS
from io import BytesIO 

app = Flask(__name__)
CORS(app)

# "Inteligência Simulada" com respostas por palavra-chave
respostas = {
    "saldo": "Seu saldo atual é de R$ 1.254,76.",
    "bloquear cartão": 
    """
        Bloqueio de Cartão - Instruções

        Se você perdeu seu cartão ou suspeita de fraude, siga um dos passos abaixo para bloqueá-lo:

        1. Pelo aplicativo:
        - Acesse o app do banco.
        - Vá em: Cartões > Gerenciar > Bloquear Cartão.
        - Confirme a solicitação com sua senha ou biometria.

        2. Pela Central de Atendimento (24h):
        - Ligue para: 0800 123 4567
        - Escolha a opção "Bloquear cartão".
        - Tenha em mãos seu CPF para identificação.

        3. Pelo site oficial:
        - Acesse sua conta pelo site do banco.
        - Vá até a área de Cartões > Bloqueio.
        - Siga as instruções na tela.

        Dica de segurança:
        Se houver suspeita de uso indevido, registre um boletim de ocorrência e comunique o banco imediatamente.

    Seu cartão será cancelado e um novo será emitido.
""",
    "fatura": "Sua fatura atual vence em 10/05 e o valor é de R$ 623,40.",
    "ajuda": "Claro! Posso te ajudar com saldo, extrato, fatura, limite, contato, horário e mais.",
    "contato": "Você pode falar com um atendente ligando para 0800-000-0000, 24h por dia.",
    "horário": "Nosso horário de atendimento é das 08h às 18h, de segunda a sexta.",
    "limite": "O seu limite total é de: R$ 3.000 || Disponível: R$ 2,460",
    "sair": "Volte sempre!"
}

def encontrar_resposta(mensagem):
    mensagem = mensagem.lower()
    for chave in respostas:
        if chave in mensagem:
            return respostas[chave]
    return "Desculpe, não entendi sua pergunta. Poderia reformular?"

# Função para gerar o arquivo de extrato
def gerar_extrato_arquivo():
    extrato = """
    Extrato da Conta - 03/05/2025

    Saldo atual: R$ 3.250,75

    Movimentações recentes:
    - 03/05/2025: Supermercado Bom Preço      | -R$ 125,40
    - 02/05/2025: Depósito                    | +R$ 500,00
    - 30/04/2025: Conta de luz                | -R$ 89,30
    """
    # Usando BytesIO para criar um arquivo binário em memória
    output = BytesIO()
    output.write(extrato.encode('utf-8'))  # Codificando o texto para bytes
    output.seek(0)  # Retorna ao início do arquivo para leitura
    return output

# Rota principal que carrega o HTML
@app.route("/")
def home():
    return render_template("index.html")

# Rota de resposta do bot
@app.route("/responder", methods=["POST"])
def responder():
    data = request.json
    pergunta = data.get("mensagem", "")
    resposta = encontrar_resposta(pergunta)
    
    # Se a pergunta for sobre extrato, gerar o arquivo e retornar o link para o download
    if "extrato" in pergunta.lower():
        return jsonify({
            "resposta": "Clique no link abaixo para baixar seu extrato:",
            "download_link": "/download_extrato"
        })
    
    return jsonify({"resposta": resposta})

# Rota para o download do extrato
@app.route("/download_extrato")
def download_extrato():
    # Gerar o arquivo de extrato
    extrato_arquivo = gerar_extrato_arquivo()

    # Retornar o arquivo como resposta
    return send_file(
        extrato_arquivo, 
        as_attachment=True, 
        download_name="extrato_bancario.txt", 
        mimetype="text/plain"
    )

if __name__ == "__main__":
    app.run(debug=True)