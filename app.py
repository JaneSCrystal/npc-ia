from flask import Flask, request
import json

app = Flask(__name__)

def carregar():
    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)

def detectar_estado(msg):
    msg = msg.lower()

    if any(x in msg for x in ["ataque", "sair", "invadir", "perigo", "ameaça", "ameaça"]):
        return "protecao"

    if any(x in msg for x in ["segurança", "seguranca", "estranho", "quem é você"]):
        return "atencao"

    return "normal"


@app.route("/", methods=["GET", "POST"])
def responder():

    if request.method == "GET":
        return "Servidor ativo."

    msg = request.get_data(as_text=True)
    cfg = carregar()

    estado = detectar_estado(msg)
    modo = cfg["modos"]["seguranca"]

    # base padrão (Crystal sempre protegida)
    resposta = modo["padrao"]

    if "oi" in msg.lower():
        resposta = modo["oi"]

    if "olá" in msg.lower() or "ola" in msg.lower():
        resposta = modo["ola"]

    if "ajuda" in msg.lower():
        resposta = modo["ajuda"]

    if "quem" in msg.lower():
        resposta = modo["quem_e_voce"]

    # 🔥 sobrescreve conforme estado
    if estado == "atencao":
        resposta = "Estou observando. Identifique-se corretamente."

    if estado == "protecao":
        resposta = "Atenção. Você está violando o perímetro da Crystal."

    return resposta


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
