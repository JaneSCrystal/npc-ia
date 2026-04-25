from flask import Flask, request
import json

app = Flask(__name__)

def carregar():
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


@app.route("/", methods=["GET", "POST"])
def responder():

    # 🔹 TESTE NO NAVEGADOR
    if request.method == "GET":
        return "Servidor ativo."

    # 🔹 IA (Second Life POST)
    msg = request.get_data(as_text=True).lower()

    cfg = carregar()
    if not cfg:
        return "Erro de configuração."

    modo = cfg.get("modo", "seguranca")
    frases = cfg["modos"][modo]

    if "oi" in msg:
        return frases["oi"]

    if "ola" in msg or "olá" in msg:
        return frases["ola"]

    if "ajuda" in msg:
        return frases["ajuda"]

    if "quem" in msg:
        return frases["quem_e_voce"]

    return frases["padrao"]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
