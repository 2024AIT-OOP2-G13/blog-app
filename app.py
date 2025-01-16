from flask import Flask, render_template, request, Blueprint, url_for, redirect, flash,session
from get_blogs import get_blogs
from models import Blog, db, initialize_database, User
from datetime import datetime
import os
from functools import wraps


app = Flask(__name__)

initialize_database()

app.secret_key = 'secret_key'

user_bp = Blueprint('upload_blog', __name__, url_prefix='/upload_blog')
app.register_blueprint(user_bp)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            user = User.get(User.username == username)
            if user.check_password(password):
                session['username'] = username 
                print("ログインに成功しました。")
            else:
                flash('パスワードが間違っています。')
                return redirect(url_for('login'))

        except User.DoesNotExist:
            flash('ユーザーが存在しません')
            return redirect(url_for('login'))

        return redirect(url_for('home'))

    return render_template("userLogin.html")

@app.route("/register_user",methods=['GET','POST'])
def register_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            user = User(username=username)
            user.set_password(password)
            user.save()
        except Exception as e:
            
            flash('ユーザーはすでに存在します。')
            return redirect(url_for('register_user'))


        return render_template("userLogin.html")
    
    
    return render_template("register_user.html")

@app.route("/home")
@login_required
def home():
    blogs = get_blogs()
    return render_template("home.html", blogs=blogs)

@app.route('/upload_blog', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        blogs = get_blogs()
        check_title=title.strip()#空白を取り除き、タイトルが無しもしくは空白のみの場合エラー
        if not check_title:
            return "タイトルを入力してください"
        check_content = content.strip()
        if not check_content:
            return "コンテンツを入力してください"

        # 現在のユーザーを取得
        current_user = User.get(User.username == session['username'])

        # ブログを作成
        Blog.create(title=title, content=content, user=current_user)
        print("ブログが正常にアップロードされました。")

        return redirect(url_for('home'))

    return render_template('upload_blog.html')


@app.route("/userblog/<int:user_id>", methods=['GET'])
def userblog(user_id):
    # ブログデータを取得
    blogs = get_blogs()
    select = Blog.get_or_none(Blog.id == user_id)

    print("select:",type(select))
    print("blog",type(blogs))


    return render_template("userBlog.html",blogs=blogs, select=select)

@app.route('/logout')
def logout():
    session.pop('username', None)  # セッションからユーザー名を削除
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080, debug=True)
