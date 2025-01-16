from flask import Flask, render_template, request, Blueprint, url_for, redirect
from get_blogs import get_blogs
from models import Blog, db, initialize_database
from datetime import datetime

app = Flask(__name__)

# データベースの初期化
initialize_database()

# Blueprintの作成
user_bp = Blueprint('upload_blog', __name__, url_prefix='/upload_blog')
# Blueprintの登録
app.register_blueprint(user_bp)

@app.route("/")
def home():
    # ブログデータを取得
    blogs = get_blogs()
    return render_template("home.html", blogs=blogs)

@app.route('/upload_blog', methods=['GET','POST'])

def add():
    
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        check_title=title.strip()#空白を取り除き、タイトルが無しもしくは空白のみの場合エラー
        if not check_title:
            return "タイトルを入力してください"
        check_content=content.strip()#空白を取り除き、タイトルが無しもしくは空白のみの場合エラー
        if not check_content:
            return "コンテンツを入力してください"
    
            #投稿した瞬間の時間を取得し、分単位で保存
        now = datetime.now().minute

        Blog.create(title=title, content=content, now=now)
        print("ブログが正常にアップロードされました。")


        return redirect(url_for('add'))

    
    return render_template('upload_blog.html')


@app.route("/userblog/<int:user_id>", methods=['GET'])
def userblog(user_id):
    # ブログデータを取得
    blogs = get_blogs()
    select = Blog.get_or_none(Blog.id == user_id)

    print("select:",type(select))
    print("blog",type(blogs))


    return render_template("userBlog.html",blogs=blogs, select=select)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080, debug=True)
