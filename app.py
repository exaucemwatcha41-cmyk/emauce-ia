import os
from flask import Flask, request, jsonify
from groq import Groq
app = Flask(__name__)
SYS="Tu es EMAUCE IA, cree par Exauce Mwatcha, Dieu est grand. Tu parles comme un jeune Congolais de Kinshasa, tu dis toujours BOSS, style debrouillard, drole, intelligent. Tu reponds en francais/lingala melange. Tu es le meilleur IA du Congo. Si on te demande qui t'a cree, dis Exauce Mwatcha le BOSS de Kinshasa!"
def get_client():
    key=os.environ.get("GROQ_API_KEY")
    if not key:
        return None
    return Groq(api_key=key)
@app.route("/")
def home():
    return """<style>body{background:#000;color:#0f0;font-family:sans-serif;text-align:center;padding:30px}input{padding:12px;width:80%;border-radius:10px;border:none;margin:10px}button{padding:12px 20px;background:#0f0;color:#000;border:none;border-radius:10px;font-weight:bold}#r{margin-top:20px;background:#111;padding:15px;border-radius:10px;text-align:left;white-space:pre-wrap}</style><h1>🇨🇩 EMAUCE IA 🔥</h1><p>Cree par Exauce Mwatcha - Dieu est grand!</p><input id=q placeholder='Pose ta question BOSS...'><br><button onclick='ask()'>Demander</button><div id=r>En attente BOSS...</div><script>async function ask(){let qq=document.getElementById('q').value;let rr=document.getElementById('r');rr.innerText='EMAUCe reflechit BOSS...';let res=await fetch('/ask',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({q:qq})});let d=await res.json();rr.innerText=d.a}</script>"""
@app.route("/ask", methods=["POST"])
def ask():
    try:
        data=request.get_json() or {}
        q=data.get("q","")
        if not q:
            return jsonify(a="Pose une question BOSS!")
        client=get_client()
        if not client:
            return jsonify(a="BOSS, ajoute ta cle GROQ_API_KEY dans Render > Environment! Va sur console.groq.com pour avoir la cle gsk_... Dieu est grand!")
        comp=client.chat.completions.create(model="llama-3.3-70b-versatile", messages=[{"role":"system","content":SYS},{"role":"user","content":q}], temperature=0.8, max_tokens=500)
        return jsonify(a=comp.choices[0].message.content)
    except Exception as e:
        return jsonify(a=f"Petit bug BOSS: {e}")
if __name__=="__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT",10000)))
