from flask import Flask, request, jsonify
from groq import Groq
import os

app = Flask(__name__)

def get_client():
    k = os.environ.get("GROQ_API_KEY")
    return Groq(api_key=k) if k else None

@app.route('/')
def home():
    return "EMAUCE IA EST EN LIGNE 🇨🇩 - Va sur /ask"

@app.route('/ask', methods=['POST'])
@app.route('/chat', methods=['POST'])
def ask():
    try:
        data = request.get_json() or {}
        msg = data.get("message","")
        client = get_client()
        if not client:
            return jsonify(reply="Cle API manquante Boss")
        res = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {"role":"system","content":"Tu es EMAUCE IA, IA congolaise cree par Exauce. Tu dis Boss, Mbote."},
                {"role":"user","content":msg}
            ]
        )
        return jsonify(reply=res.choices[0].message.content)
    except Exception as e:
        return jsonify(reply=f"Erreur: {e}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
