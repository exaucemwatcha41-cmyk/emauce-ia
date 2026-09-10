from flask import Flask, request, jsonify
from groq import Groq
import os

app = Flask(__name__)

def get_client():
    key = os.environ.get("GROQ_API_KEY")
    if not key:
        return None
    return Groq(api_key=key)

@app.route('/')
def home():
    html = """
    <html><head><meta name='viewport' content='width=device-width,initial-scale=1'>
    <style>
    body{margin:0;background:#000;color:#fff;font-family:Arial;display:flex;flex-direction:column;height:100vh}
    .header{background:#ff6b00;padding:15px;text-align:center;font-weight:bold;font-size:18px}
    #chat{flex:1;overflow-y:auto;padding:10px;display:flex;flex-direction:column;gap:10px}
    .msg{padding:12px 15px;border-radius:18px;max-width:80%;word-wrap:break-word}
    .user{background:#ff6b00;align-self:flex-end}
    .bot{background:#222;align-self:flex-start;border:1px solid #333}
    .bar{display:flex;padding:10px;background:#111;gap:10px}
    input{flex:1;padding:12px;border-radius:25px;border:1px solid #333;background:#222;color:#fff;outline:none}
    button{background:#ff6b00;border:none;color:#fff;padding:12px 20px;border-radius:25px;font-weight:bold}
    </style></head>
    <body>
    <div class='header'>EMAUCE IA 🇨🇩 -
