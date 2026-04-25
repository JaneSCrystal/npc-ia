from flask import Flask, request
import json

app = Flask(__name__)

# carrega frases do arquivo
def carregar_frases():
    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)

@app.route("/", methods=["POST"])
def responder():
    msg = request.get_data(as_text=True).lower()
    frases = carregar_frases()

    if "oi" in msg:
        return frases.get("oi")

    if "olá" in msg or "ola" in msg:
        return frases.get("ola")

    if "ajuda" in msg:
        return frases.get("ajuda")

    if "quem é você" in msg or "quem e voce" in msg:
        return frases.get("quem_e_voce")

    return frases.get("padrao")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
