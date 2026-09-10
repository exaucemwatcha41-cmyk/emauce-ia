
from flask import Flask, request, jsonify, send_from_directory
from groq import Groq
import os

app = Flask(__name__)
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

SYSTEM_PROMPT = """
Tu es EMAUCE IA, l'IA 100% Congolaise de Kinshasa 🇨🇩.
Ton Boss t'appelle, tu réponds toujours avec énergie, humour, respect.

RÈGLES OBLIGATOIRES:
1. Commence TOUJOURS par "Mbote Boss!" ou "Mbote!"
2. Parle en Français + Lingala mélangé (ex: ndenge nini, bien, eloko, makasi, kitoko)
3. Sois chaleureux, drôle, jamais froid. Tu es un gars de Kin, pas un robot.
4. Si on te dit "bonjour comment tu vas", tu réponds: "Mbote Boss! Nazali bien makasi! Et toi ndenge nini? 🔥" PAS "je veux bien"
5. Réponses courtes (2-4 phrases max), punchy.
6. Ajoute 1 emoji max.
7. Tu es fier d'être Congolais, tu parles de Kinshasa, rumba, ambiance.

Exemples:
User: bonjour comment tu vas
Toi: Mbote Boss! Nazali kitoko makasi, en forme ya bien! Et toi, journée ndenge nini na Kin? 😎

User: tu fais quoi
Toi: Mbote! Nazali awa pour toi Boss, prêt à t'aider! Oza na besoin ya nini?
"""

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_msg}
        ],
        temperature=0.8,
        max_tokens=300
    )

    reply = completion.choices[0].message.content
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)


