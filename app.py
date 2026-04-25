from flask import Flask, request
import json

app = Flask(__name__)

# -------------------------
# carregar config JSON
# -------------------------
def carregar():
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print("Erro ao carregar config:", e)
        return None


# -------------------------
# endpoint principal
# -------------------------
@app.route("/", methods=["GET", "POST"])
def responder():

    # teste no navegador
    if request.method == "GET":
        return "Servidor ativo."

    # mensagem recebida do Second Life
    raw = request.get_data(as_text=True)

    cfg = carregar()
    if not cfg:
        return "Erro de configuração."

    modo = cfg["modos"]["seguranca"]

    # -------------------------
    # reconhecimento de nome
    # -------------------------
    nome = "Visitante"
    msg = raw.lower()

    if ":" in raw:
        partes = raw.split(":", 1)
        nome = partes[0].strip()
        msg = partes[1].strip().lower()

    # -------------------------
    # lógica de resposta
    # -------------------------
    resposta = modo["padrao"]

    if "oi" in msg:
        resposta = modo["oi"]

    elif "ola" in msg or "olá" in msg:
        resposta = modo["ola"]

    elif "ajuda" in msg:
        resposta = modo["ajuda"]

    elif "quem" in msg:
        resposta = modo["quem_e_voce"]

    # -------------------------
    # resposta final (nome na frente)
    # -------------------------
    return f"{nome}, {resposta}"


# -------------------------
# rodar servidor
# -------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
