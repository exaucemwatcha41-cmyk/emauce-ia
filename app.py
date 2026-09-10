from flask import Flask, request, jsonify
import os
from groq import Groq

app = Flask(__name__)

SYS = "Tu es EMAUCE IA, cree par Exauce Mwatcha, une IA congolaise fiere, intelligente, qui aide tout le monde. Tu reponds en lingala, francais, anglais selon la question. Tu es le meilleur."

def get_client():
    key = os.environ.get("GROQ_API_KEY")
    if not key:
        return None
    return Groq(api_key=key)

@app.route('/')
def home():
    return """<style>body{background:#000;color:#fff;font-family:sans-serif;text-align:center;padding:20px}</style><h1>🇨🇩 EMAUCE IA LIVE</h1><p>La premiere IA 100% Congolaise par Exauce</p><div id="chat" style="max-width:600px;margin:auto;text-align:left;background:#111;padding:15px;border-radius:10px;height:300px;overflow-y:auto"></div><div style="max-width:600px;margin:15px auto;display:flex"><input id="q" placeholder="Pose ta question..." style="flex:1;padding:12px;border-radius:8px;border:none"><button onclick="send()" style="padding:12px 20px;margin-left:10px;background:#00f;color:#fff;border:none;border-radius:8px">Envoyer</button></div><script>async function send(){let i=document.getElementById('q');let q=i.value;if(!q)return;let c=document.getElementById('chat');c.innerHTML+='<div><b>Toi:</b> '+q+'</div>';i.value='';let r=await fetch('/ask',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:q})});let d=await r.json();c.innerHTML+='<div style=\"margin:10px 0;color:#0f0\"><b>EMAUCE:</b> '+d
