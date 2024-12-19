from models import Blog, db

# データベースから古い順にブログを取得
def get_blogs():
    query = Blog.select().order_by(Blog.created_at.asc())
    for blog in query:
        print(f"Title: {blog.title}, Content: {blog.content}, Created At: {blog.created_at}")

if __name__ == "__main__":
    db.connect()
    get_blogs()
    db.close() 