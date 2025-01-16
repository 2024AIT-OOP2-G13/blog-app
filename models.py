from peewee import SqliteDatabase, Model, CharField, DateTimeField, ForeignKeyField
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

# データベースの接続
db = SqliteDatabase('blogs.db')

# ユーザーモデルの定義
class User(Model):
    username = CharField(unique=True)
    password_hash = CharField()

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    class Meta:
        database = db

# ブログモデルの定義
class Blog(Model):
    title = CharField()
    content = CharField()
    created_at = DateTimeField(default=datetime.now)
    user = ForeignKeyField(User, backref='blogs')

    class Meta:
        database = db 

def initialize_database():
    db.connect()
    db.create_tables([User, Blog], safe=True)
    db.close()
