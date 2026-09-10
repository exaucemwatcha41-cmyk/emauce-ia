from flask import Flask, request, jsonify
import os
from groq import Groq

app = Flask(__name__)
SYS = "Tu es EMAUCE IA, cree par Exauce Mwatcha, IA congolaise."

def get_client():
    k = os.environ.get("GROQ_API_KEY")
    if not k:
        return None
    return Groq(api_key=k)

@app.route('/')
def home():
    return "EMAUCE IA LIVE BOSS - OK"

@app.route('/ask', methods=["POST"])
@app.route('/chat', methods=["POST"])
def ask():
    try:
        d = request.get_json() or {}
        m = d.get("message","") or d.get("q","")
        if not m:
            return jsonify({"reply":"Pose question BOSS"})
        c = get_client()
        if not c:
            return jsonify({"reply":"Cle GROQ manquante"})
        r = c.chat.completions.create(model="llama3-8b-8192",messages=[{"role":"system","content":SYS},{"role":"user","content":m}])
        return jsonify({"reply":r.choices[0].message.content})
    except Exception as e:
        return jsonify({"reply":f"Erreur: {e}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
