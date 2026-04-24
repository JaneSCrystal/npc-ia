from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def responder():
    if request.method == "POST":
        msg = request.get_data(as_text=True).lower()

        if "oi" in msg or "olá" in msg:
            return "Boa noite. Posso ajudar?"

        if "ajuda" in msg:
            return "Informe sua solicitação."

        if "quem é você" in msg:
            return "Sou responsável pela segurança deste local."

        return "Estou acompanhando o ambiente."

    return "Servidor ativo."

port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)
