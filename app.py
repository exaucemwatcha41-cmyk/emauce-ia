from flask import Flask, request, jsonify
from groq import Groq
import os

app = Flask(__name__)

def get_client():
    key = os.environ.get("GROQ_API_KEY")
    if not key: return None
    return Groq(api_key=key)

@app.route('/')
def home():
    html = """
    <html><head><meta name='viewport' content='width=device-width,initial-scale=1'>
    <style>
    body{margin:0;background:#000;color:#fff;font-family:Arial;display:flex;flex-direction:column;height:100vh}
   .header{background:#ff6b00;padding:15px;text-align:center;font-weight:bold;font-size:18px}
    #chat{flex:1;overflow-y:auto;padding:10px;display:flex;flex-direction:column;gap:10px}
   .msg{padding:12px 15px;border-radius:18px;max-width:80%}
   .user{background:#ff6b00;align-self:flex-end}
   .bot{background:#222;align-self:flex-start;border:1px solid #333}
   .bar{display:flex;padding:10px;background:#111;gap:10px}
    input{flex:1;padding:12px;border-radius:25px;border:1px solid #333;background:#222;color:#fff}
    button{background:#ff6b00;border:none;color:#fff;padding:12px 20px;border-radius:25px;font-weight:bold}
    </style></head>
    <body>
    <div class='header'>EMAUCE IA 🇨🇩 - Par Exauce</div>
    <div id='chat'><div class='msg bot'>Mbote Boss! Je suis EMAUCE IA, ton IA congolaise! Pose-moi une question 🔥</div></div>
    <div class='bar'><input id='inp' placeholder='Ecris ici Boss...'><button onclick='send()'>Envoyer</button></div>
    <script>
    async function send(){
     let i=document.getElementById('inp'); let m=i.value; if(!m) return;
     let c=document.getElementById('chat'); c.innerHTML+="<div class='msg user'>"+m+"</div>"; i.value='';
     c.scrollTop=c.scrollHeight;
     let r=await fetch('/ask',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:m})});
     let d=await r.json(); c.innerHTML+="<div class='msg bot'>"+d.reply+"</div>"; c.scrollTop=c.scrollHeight;
    }
    document.getElementById('inp').addEventListener('keypress',function(e){if(e.key==='Enter') send();});
    </script>
    </body></html>
    """
    return html

@app.route('/ask', methods=["POST"])
@app.route('/chat', methods=["POST"])
def ask():
    try:
        d = request.get_json() or {}
        m = d.get("message","") or d.get("msg","")
        if not m:
            return jsonify({"reply":"Pose ta question Boss!"})
        c = get_client()
        if not c:
            return jsonify({"reply":"Clé API manquante Boss! Va sur Render > Environment > ajoute GROQ_API_KEY"})
        chat = c.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role":"system","content":"Tu es EMAUCE IA, une IA congolaise créée par Exauce. Tu parles lingala et français. Tu es fun, jeune, tu dis Boss, Mbote. Tu es très intelligent."},
                {"role":"user","content":m}
            ]
        )
        return jsonify({"reply": chat.choices[0].message.content})
    except Exception as e:
        return jsonify({"reply": f"Erreur: {str(e)}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
