from flask import Flask, request, jsonify
import os
from groq import Groq

app = Flask(__name__)
SYS = "Tu es EMAUCE IA, cree par Exauce Ndombasi Mbungu. Tu es congolais, intelligent, tu parles lingala et francais, tu aides ton boss avec fierte 🇨🇩"

def get_client():
    k = os.environ.get("GROQ_API_KEY")
    if not k:
        return None
    return Groq(api_key=k)

@app.route('/')
def home():
    html = """
<!DOCTYPE html>
<html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width'>
<title>EMAUCE IA 🇨🇩</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#0a0a0a;color:white;font-family:Arial;height:100vh;display:flex;flex-direction:column}
.header{background:linear-gradient(90deg,#ff6b00,#ff9500);padding:15px;text-align:center;font-weight:bold;font-size:20px}
#chat{flex:1;overflow-y:auto;padding:15px;display:flex;flex-direction:column;gap:10px}
.msg{padding:12px 15px;border-radius:18px;max-width:80%;word-wrap:break-word}
.user{background:#ff6b00;align-self:flex-end;color:white}
.bot{background:#222;align-self:flex-start;border:1px solid #333}
.bar{display:flex;padding:10px;background:#111;gap:10px}
input{flex:1;padding:12px;border-radius:25px;border:none;background:#222;color:white;outline:none}
button{background:#ff6b00;border:none;color:white;padding:12px 20px;border-radius:25px;font-weight:bold}
</style></head>
<body>
<div class='header'>EMAUCE IA 🇨🇩 - Par Exauce</div>
<div id='chat'><div class='msg bot'>Mbote Boss! Je suis EMAUCE IA, ton IA congolaise! Pose-moi une question 🔥</div></div>
<div class='bar'><input id='inp' placeholder='Ecris ici Boss...'><button onclick='send()'>Envoyer</button></div>
<script>
async function send(){
 let i=document.getElementById('inp'); let m=i.value.trim(); if(!m)return;
 let c=document.getElementById('chat'); c.innerHTML+="<div class='msg user'>"+m+"</div>"; i.value='';
 c.scrollTop=c.scrollHeight;
 let r=await fetch('/ask',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:m})});
 let d=await r.json(); c.innerHTML+="<div class='msg bot'>"+d.reply+"</div>"; c.scrollTop=c.scrollHeight;
}
document.getElementById('inp').addEventListener('keypress',e=>{if(e.key==='Enter')send()});
</script>
</body></html>
"""
    return html

@app.route('/ask', methods=["POST"])
@app.route('/chat', methods=["POST"])
def ask():
    try:
        d = request.get_json() or {}
        m = d.get("message","") or d.get("msg","") or d.get("q","")
        if not m:
            return jsonify({"reply":"Pose ta question Boss!"})
        c = get_client()
        if not c:
            return jsonify({"reply":"Cle GROQ_API_KEY manquante sur Render Boss!"})
        r = c.chat.completions.create(model="llama-3.1-8b-instant",messages=[{"role":"system","content":SYS},{"role":"user","content":m}],temperature=0.7,max_tokens=800)
        return jsonify({"reply":r.choices[0].message.content})
    except Exception as e:
        return jsonify({"reply":f"Erreur: {str(e)}"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
