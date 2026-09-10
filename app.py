from flask import Flask, request, jsonify
from groq import Groq
import os
app = Flask(__name__)
def get_client():
    k=os.environ.get("GROQ_API_KEY")
    if not k: return None
    return Groq(api_key=k)
@app.route('/')
def home():
    return """<html><head><meta name='viewport' content='width=device-width,initial-scale=1'><style>body{margin:0;background:#000;color:#fff;font-family:Arial;display:flex;flex-direction:column;height:100vh}.header{background:#ff6b00;padding:15px;text-align:center;font-weight:bold}#chat{flex:1;overflow:auto;padding:10px;display:flex;flex-direction:column;gap:10px}.msg{padding:12px;border-radius:18px;max-width:80%}.user{background:#ff6b00;align-self:flex-end}.bot{background:#222;align-self:flex-start}</style></head><body><div class='header'>EMAUCE IA 🇨🇩</div><div id='chat'><div class='msg bot
