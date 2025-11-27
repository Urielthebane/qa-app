from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()  # ← reads your .env file
client = Groq()  # ← automatically uses GROQ_API_KEY from .env

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.json.get("question")
    if not question:
        return jsonify({"error": "No question"}), 400

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",   # fast & free
        messages=[{"role": "user", "content": question}],
        temperature=0.7,
        max_tokens=600
    )
    answer = response.choices[0].message.content
    return jsonify({"answer": answer})

if __name__ == "__main__":
    port = int(os.environ.get("port", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)