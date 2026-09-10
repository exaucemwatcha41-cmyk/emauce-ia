from flask import Flask, request, jsonify
from groq import Groq
import os

app = Flask(__name__)
BASE = os.path.dirname(os.path.abspath(__file__))

def get_client():
    k = os.environ.get("GROQ_API_KEY")
    return Groq(api_key=k) if k else None

@app.route('/')
def home():
    p = os.path.join(BASE, "index.html")
    if not os.path.exists(p):
        return "index.html introuvable", 404
    return open(p, encoding='utf-8').read()

@app.route('/ask')
def ask_get():
    msg = request.args.get("q","")
    if not msg:
        return "Pose une question Boss!"
    client = get_client()
    if not client:
        return "Cle GROQ_API_KEY manquante"
    try:
       
