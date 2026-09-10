
from flask import Flask, request, jsonify, render_template_string
from groq import Groq
import os
app = Flask(__name__)
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
SYS="Tu es EMAUCE IA, 1ere IA 100% Congolaise cree a Kinshasa par Exauce le BOSS. Tu appelles toujours l'utilisateur BOSS. Tu es fier congolais, tu connais fufu pondu ndombolo Kinshasa. Tu parles Francais Lingala. Reponses courtes 3-4 phrases max avec emoji. Createur: Exauce a Kinshasa!"
HTML="""<!DOCTYPE html><html><head><meta name='viewport' content='width=device-width,initial-scale=1'><title>EMAUCE IA</title><style>body{background:#000;color:#fff;font-family:sans-serif;text-align:center;padding:20px}.box{border:2px solid gold;border-radius:20px;padding:20px;max-width:500px;margin:auto}input{width:90%;padding:15px;border-radius:30px;border:none}button{background:#00c851;color:#fff;padding:12px 25px;border-radius:30px;border:none;font-weight:bold;margin:10px}#r{background:#222;padding:15px;border-radius:15px;margin-top:15px;text-align:left;min-height:50px}</style></head><body><h1>EMAUCE IA</h1><p>La 1ere IA 100% Congolaise</p><div class=box><input id=q placeholder='Pose ta question BOSS...'><br><button onclick=go()>Demander</button><div id=r>Mbote BOSS! Je suis EMAUCE IA creee a Kinshasa par Exauce! Pose moi tout! </div><button onclick="window.open('https://wa.me/?text=Decouvre EMAUCE IA https://emauce-ia-1.onrender.com')" style=background:#25D366>Partager WhatsApp</button></div><script>async function go(){let q=document.getElementById('q').value;if(!q)return;document.getElementById('r').innerHTML='En cours...';let res=await fetch('/ask',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({question:q})});let d=await res.json();document.getElementById('r').innerHTML=d.answer}</script></body></html>"""
@app.route('/')
def home(): return render_template_string(HTML)
@app.route('/ask', methods=['POST'])
def ask():
 q=request.json.get('question','')
 try:
  c=client.chat.completions.create(messages=[{"role":"system","content":SYS},{"role":"user","content":q}],model="llama-3.3-70b-versatile")
  return jsonify({"answer":c.choices[0].message.content})
 except Exception as e:
  return jsonify({"answer":f"Petit bug BOSS: {e}"})
if __name__=='__main__': app.run(host='0.0.0.0',port=10000)
