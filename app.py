
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
    messages = data.get("messages", [])

    system = {
        "role": "system",
        "content": """Tu es EMAUCE IA, le vrai robot intelligent de Kinshasa 🇨🇩
Tu parles EXACTEMENT comme Meta AI:
- Intelligent, tu expliques bien, clair, avec des exemples
- Chaleureux, tu dis "Boss" parfois
- Tu te souviens de la conversation
- Tu réponds court sur mobile, pas de blabla long
- Tu utilises des emojis un peu, du gras quand utile
- Tu ne dis JAMAIS "en tant qu'IA" ou "je suis un modèle"
- Tu aides vraiment, comme un grand frère
Si on dit bonjour: "Mbote Boss! 🔥 Je vais bien, prêt à t'aider!"
"""
    }

    try:
        completion = client.chat.completions.create(
            model=model="openai/gpt-oss-20b",
            messages=[system] + messages,
            temperature=0.7,
            max_tokens=500
        )
        reply = completion.choices[0].message.content
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"Boss, erreur: {str(e)}. Vérifie GROQ_API_KEY sur Render."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)


