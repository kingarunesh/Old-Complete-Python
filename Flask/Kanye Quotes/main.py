from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route("/")
def home():
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    
    return render_template("index.html", quote=quote)


if __name__ == "__main__":
    app.run(debug=True)
