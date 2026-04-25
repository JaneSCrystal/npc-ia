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

    if request.method == "GET":
        return "Servidor ativo."

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
    # DETECÇÃO DE AMEAÇA (ARGUS MODE)
    # -------------------------
    perigo = False

    palavras_perigo = [
        "atacar",
        "arma",
        "matar",
        "hack",
        "explodir",
        "invadir",
        "denunciar",
        "assediar"
    ]

    for p in palavras_perigo:
        if p in msg:
            perigo = True
            break

    # -------------------------
    # escolha de identidade
    # -------------------------
    if perigo:
        npc_nome = "Argus"
        resposta = "Alerta. Sua ação foi registrada. Mantenha distância imediatamente."
    else:
        npc_nome = "Orion Guard"

        resposta = modo["padrao"]

        if "oi" in msg:
            resposta = modo["oi"]

        elif "ola" in msg or "olá" in msg:
            resposta = modo["ola"]

        elif "ajuda" in msg:
            resposta = modo["ajuda"]

        elif "quem" in msg:
            resposta = (
                "Sou Orion Guard. "
                "Inspirado na constelação Orion, cujas estrelas brilham intensamente no céu noturno, "
                "eu permaneço atento, observando e protegendo em silêncio. "
                "Assim como a luz de Orion orienta na escuridão, minha função é garantir a segurança da Crystal."
            )

    # -------------------------
    # resposta final
    # -------------------------
    return f"{npc_nome}: {nome}, {resposta}"


# -------------------------
# rodar servidor
# -------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
