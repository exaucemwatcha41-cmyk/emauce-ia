import os
from flask import Flask, request, jsonify
from groq import Groq

app = Flask(__name__)

SYS = "Tu es EMAUCE IA, cree par Exauce Mwatcha, une IA 100% Congolaise 🇨🇩. Tu es fiere, intelligente, tu aides tout le monde."

def get_client():
    key = os.environ.get("GROQ_API_KEY")
    if not key:
        return None
    return Groq(api_key=key)

@app.route("/")
def home():
    return """<style>body{background:#000;color:#fff;font-family:sans-serif;text-align:center;padding:20px}input{width:80%;padding:15px;border-radius:25px;border:none;margin-top:20px}button{padding:15px 25px;border-radius:25px;border:none;background:#0a84ff;color:#fff;margin-left:10px}#chat{max-width:600px;margin:auto;text-align:left;height:60vh;overflow-y:auto;border:1px solid #333;padding:15px;border-radius:15px}</style><h2>🇨🇩 EMAUCE IA 🇨🇩</h2><p>La premiere IA 100% Congolaise par Exauce</p><div id=chat></div><div><input id=q placeholder='Pose ta question...'><button onclick=ask()>Envoyer</button></div><script>async function ask(){let q=document.getElementById('q').value;if(!q)return;let c=document.getElementById('chat');c.innerHTML+=`<div style=background:#0a84ff;padding:10px;border-radius:10px;margin:8px>👤 ${q}</div>`;document.getElementById('q').value='';let r=await fetch('/ask',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:q})});let d=await r.json();c.innerHTML+=`<div style=background:#333;padding:10px;border-radius:10px;margin:8px>🤖 ${d.reply}</div>`;c.scrollTop=c.scrollHeight}</script>"""

@app.route("/ask", methods=["POST"])
@app.route("/chat", methods=["POST"])
def ask():
    try:
        data = request.get_json() or {}
        msg = data.get("message","")
        client = get_client()
        if not client:
            return jsonify({"reply": "BOSS clé GROQ non trouvée! Va sur Render > Environment > GROQ_API_KEY"})
        comp = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role":"system","content":SYS},{"role":"user","content":msg}]
        )
        return jsonify({"reply": comp.choices[0].message.content})
    except Exception as e:
        return jsonify({"reply": f"Erreur: {str(e)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
