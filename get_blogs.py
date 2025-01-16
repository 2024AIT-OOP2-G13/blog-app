from models import Blog, db

# データベースからブログを取得
def get_blogs():
    db.connect()
    blogs = Blog.select().order_by(Blog.created_at.desc())
    db.close()
    return blogs

if __name__ == "__main__":
    db.connect()
    get_blogs()
    db.close() 