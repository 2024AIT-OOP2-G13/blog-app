from models import Blog, db

def upload_blog():
    title = input("タイトルを入力してください: ")
    blog_content = input("ブログの内容を入力してください: ")

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