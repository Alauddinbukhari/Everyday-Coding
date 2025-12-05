from flask import Flask, render_template
import requests

app = Flask(__name__)

url = "https://api.npoint.io/c790b4d5cab58020d391"
    
try:
        response = requests.get(url)
        response.raise_for_status()
        posts = response.json()
        print(posts)
except requests.exceptions.RequestException as e:
        print("Error fetching blog data:", e)
        posts = []  # fallback

@app.route('/')
def home():
  

    return render_template("index.html", posts=posts)


@app.route("/post/<int:post_id>")
def view_post(post_id):
      
      return render_template("post.html", post=posts[post_id-1])



if __name__ == "__main__":
    app.run(debug=True)

