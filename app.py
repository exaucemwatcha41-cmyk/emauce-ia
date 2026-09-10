
from flask import Flask, request, jsonify, send_from_directory
from groq import Groq
import os

app = Flask(__name__)
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    messages = data.get("messages", []) # On reçoit tout l'historique comme moi!

    system = {
        "role": "system",
        "content": """Tu es EMAUCE IA, le vrai assistant IA comme Meta AI / ChatGPT, créé par Exaucé à Kinshasa 🇨🇩.

Tu parles EXACTEMENT comme moi:
- Tu es intelligent, tu expliques bien, tu donnes des étapes claires
- Tu es chaleureux, tu dis "Boss" parfois, mais tu restes PRO
- Tu te souviens de la conversation
- Tu réponds court sur mobile, pas de blabla inutile
- Tu utilises des emojis un peu, du gras pour les points importants
- Tu ne dis JAMAIS "en tant qu'IA" ou "je veux bien et toi"
- Tu aides vraiment, comme un grand frère qui connait tout en code, business, école, vie

Si on dit bonjour: "Mbote Boss! 🔥 Je vais top bien, prêt à charbonner pour toi! Ndenge nini?"
"""
    }

    all_messages = [system] + messages

    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=all_messages,
            temperature=0.7,
            max_tokens=800
        )
        reply = completion.choices[0].message.content
    except Exception as e:
        reply = f"Boss, erreur: {e}. Vérifie GROQ_API_KEY sur Render dans Environment."

    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)


