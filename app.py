from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head><title>Pierrot IA - EMAUCE</title></head>
    <body style="font-family: sans-serif; text-align: center; padding: 50px; background: #f5f5f5;">
        <h1>🤖 Pierrot IA</h1>
        <h2>Assistant EMAUCE</h2>
        <p>Ton IA est en ligne Boss!</p>
        <input id="msg" placeholder="Parle à Pierrot..." style="padding:10px; width:300px;">
        <button onclick="alert('Pierrot arrive! Code à connecter à OpenAI')" style="padding:10px;">Envoyer</button>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

