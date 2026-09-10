from flask import Flask, request, jsonify
from groq import Groq
import os

app = Flask(__name__)

def get_client():
    k = os.environ.get("GROQ_API_KEY")
    return Groq(api_key=k) if k else None

@app.route('/')
def home():
    return open('index.html', encoding='utf-8').read()

@app.route('/ask')
def ask_get():
    msg = request.args.get("q","")
    if not msg:
        return "Pose une question Boss!"
    client = get_client()
    if not client:
        return "Cle API manquante Boss, configure GROQ_API_KEY sur Render"
    try:
        res = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {"role":"system","content":"Tu es EMAUCE IA, la premiere IA 100% Congolaise, cree par Exauce. Tu parles comme un Kinois, tu dis Mbote Boss, tu es fier, drole et intelligent. Reponds toujours en Lingala melange Francais."},
                {"role":"user","content":msg}
            ]
        )
        return res.choices[0].message.content
    except Exception as e:
        return f"Erreur: {e}"

@app.route('/ask', methods=['POST'])
@app.route('/chat', methods=['POST'])
def ask_post():
    data = request.get_json() or {}
    msg = data.get("message","")
    client = get_client()
    if not client:
        return jsonify(reply="Cle API manquante")
    res = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role":"system","content":"Tu es EMAUCE IA, la premiere IA 100% Congolaise."},
            {"role":"user","content":msg}
        ]
    )
    return jsonify(reply=res.choices[0].message.content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
