from peewee import SqliteDatabase, Model, CharField, DateTimeField
from datetime import datetime
from models import Blog, db
from flask import Blueprint, render_template, request, redirect, url_for, Flask
from datetime import datetime

app = Flask(__name__)
#仮のデータベース
blogs = []

def upload_blog():
    
    title = request.form.get("title")
    content = request.form.get("content")
    check_title=title.strip()#空白を取り除き、タイトルが無しもしくは空白のみの場合エラー
    if not check_title:
        return "タイトルを入力してください"
    check_content=content.strip()#空白を取り除き、タイトルが無しもしくは空白のみの場合エラー
    if not check_content:
        return "コンテンツを入力してください"
    
    #投稿した瞬間の時間を取得し、分単位で保存
    now = datetime.now().minute

    blog = Blog(title, content, now)
    blogs.append(blog)

    return render_template("upload_blog.html")
    
    #ここにreturn render_template("投稿を表示するためのコード")を書く