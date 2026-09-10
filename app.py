from flask import Flask, request, render_template_string
app = Flask(__name__)
KNOWLEDGE = {
"bonjour": "Mbote Boss ! Je suis EMAUCE IA 🇨🇩 L'IA 100% Congolaise créée à Kinshasa par Exaucé !",
"mbote": "Mbote ndeko ! Naza EMAUCE IA. Je parle Lingala, Français, Swahili !",
"kinshasa": "Kinshasa: Capitale RDC, 17M habitants, fleuve Congo, Victoire, Gombe, Bandal !",
"default": "Bonne question Boss ! EMAUCE IA apprend chaque jour. Reformule avec la culture Congolaise ! 🇨🇩"
}
HTML = """
<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<title>EMAUCE IA 🇨🇩</title>
<style>body{font-family:Arial;background:#0a0a0a;color:#fff;padding:15px;text-align:center}
.box{background:#1a1a1a;padding:20px;border-radius:20px;max-width:500px;margin:auto;border:2px solid #ffcc00}
input{width:85%;padding:14px;border-radius:30px;border:none;margin:10px}
button{padding:14px 30px;background:#25D366;color:#fff;border:none;border-radius:30px;font-weight:bold}
.answer{margin-top:20px;background:#000;padding:15px;border-radius:15px;text-align:left}
.wa{display:inline-block;background:#25D366;color:#fff;padding:12px 20px;border-radius:30px;text-decoration:none;margin-top:15px;font-weight:bold}
</style></head><body>
<h1>🇨🇩 EMAUCE IA</h1><p>La premiere IA 100% Congolaise</p>
<div class="box"><form method="POST"><input name="q" placeholder="Pose ta question..." required><br>
<button type="submit">Demander</button></form>
{% if ans %}<div class="answer">🤖 {{ ans }}</div>{% endif %}
<a class="wa" href="https://wa.me/?text=Teste EMAUCE IA: https://emauce-ia.onrender.com" target="_blank">📱 Partager sur WhatsApp</a>
</div></body></html>
"""
@app.route("/", methods=["GET","POST"])
def home():
 ans=None
 if request.method=="POST":
  q=request.form.get("q","").lower()
  ans=KNOWLEDGE["default"]
  for k,v in KNOWLEDGE.items():
   if k in q: ans=v; break
 return render_template_string(HTML, ans=ans)
if __name__=="__main__":
 app.run(host="0.0.0.0", port=10000)
