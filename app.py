from flask import Flask, render_template
from get_blogs import get_blogs

app = Flask(__name__)

@app.route("/")
def home():
    # ブログデータを取得
    blogs = get_blogs()
    return render_template("home.html", blogs=blogs)

if __name__ == "__main__":
    app.run(port=8080, debug=True)