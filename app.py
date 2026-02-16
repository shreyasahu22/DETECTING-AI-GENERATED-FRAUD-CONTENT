from flask import Flask, render_template
import random
import os

app = Flask(__name__)

@app.route("/")
def home():
    # fake risk value (later tum model se replace karna)
    risk = random.randint(10, 95)
    return render_template("index.html", risk=risk)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render ka port ya local 5000
    app.run(host="0.0.0.0", port=port)
