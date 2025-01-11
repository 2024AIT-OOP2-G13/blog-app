from models import Blog, db
from flask import Flask, render_template, request, redirect, url_for

def upload_blog():
    title = request("タイトルを入力してください: ")
    blog_content = request("ブログの内容を入力してください: ")

    # ブログをデータベースに保存
    try:
        blog = Blog.create(title=title, content=blog_content)
        print("ブログが正常にアップロードされました。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    db.connect()
    db.create_tables([Blog])
    upload_blog()
    db.close()