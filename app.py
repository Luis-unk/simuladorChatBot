from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# "Inteligência Simulada" com respostas por palavra-chave
respostas = {
    "saldo": "Seu saldo atual é de R$ 1.254,76.",
    "extrato": "Você teve 5 movimentações recentes. Deseja que eu envie os detalhes por e-mail?",
    "limite": "O seu limite de cartão de crédito é R$ 3.000,00. Limite disponível: R$ 2.150,00.",
    "bloquear cartão": "Para bloquear seu cartão, acesse o app ou ligue para 0800-123-4567.",
    "fatura": "Sua fatura atual vence em 10/05 e o valor é de R$ 623,40.",
    "ajuda": "Claro! Posso te ajudar com saldo, extrato, fatura, bloqueio de cartão e mais.",
    "contato": "Você pode falar com um atendente ligando para 0800-000-0000, 24h por dia.",
    "horário": "Nosso horário de atendimento é das 08h às 18h, de segunda a sexta.",
    "sair": "Volte sempre!"
}

def encontrar_resposta(mensagem):
    mensagem = mensagem.lower()
    for chave in respostas:
        if chave in mensagem:
            return respostas[chave]
    return "Desculpe, não entendi sua pergunta. Poderia reformular?"

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
    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run(debug=True)
