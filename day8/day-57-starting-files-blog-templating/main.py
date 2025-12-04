from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    url = "https://www.npoint.io/docs/c790b4d5cab58020d391"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        posts = response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching blog data:", e)
        posts = []  # fallback

    return render_template("index.html", posts=posts)


if __name__ == "__main__":
    app.run(debug=True)

