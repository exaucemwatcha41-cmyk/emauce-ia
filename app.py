
from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq
import os

app = Flask(__name__)
CORS(app)
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route("/")
def home():
    return """<!DOCTYPE html><html><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'><title>EMAUCE IA</title><style>body{background:#000;color:#fff;font-family:Arial;text-align:center;padding:20px}.box{border:2px solid gold;border-radius:20px;padding:20px;max-width:400px;margin:20px auto}input{width:90%;padding:15px;border-radius:30px;border:none;outline:none}button{background:#00c853;color:#fff;padding:12px 25px;border:none;border-radius:30px;margin-top:15px;font-weight:bold;cursor:pointer}.msg{background:#111;padding:15px;border-radius:15px;margin-top:20px;text-align:left}</style></head><body><h1>🇨🇩 EMAUCE IA</h1><p>La premiere IA 100% Congolaise</p><div class='box'><input id='q' placeholder='Pose ta question...'><button onclick='ask()'>Demander</button><div id='rep' class='msg'>🤖 Mbote Boss! Je suis EMAUCE IA 🇨🇩 L'IA 100% Congolaise creee a Kinshasa par Exauce!</div><button onclick="window.open('https://wa.me/?text=Decouvre EMAUCE IA https://e-ia-1.onrender.com')">📱 Partager sur WhatsApp</button></div><script>async function ask(){let q=document.getElementById('q').value;let rep=document.getElementById('rep');if(!q)return;rep.innerText='⏳...';let r=await fetch('/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:q})});let d=await r.json();rep.innerText=d.reply;}</script></body></html>"""

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data=request.json
        msg=data.get("message","")
        comp=client.chat.completions.create(model="openai/gpt-oss-20b",messages=[{"role":"system","content":"Tu es EMAUCE IA, IA Congolaise cree par Exauce a Kinshasa. Tu dis Boss."},{"role":"user","content":msg}],temperature=0.7,max_tokens=800)
        return jsonify({"reply":comp.choices[0].message.content})
    except Exception as e:
        return jsonify({"reply":f"Erreur: {str(e)}"})

if __name__=="__main__":
    app.run(host="0.0.0.0",port=10000)

