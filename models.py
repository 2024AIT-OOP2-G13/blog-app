from peewee import SqliteDatabase, Model, CharField, DateTimeField
from datetime import datetime

# データベースの接続
db = SqliteDatabase('blogs.db')

# ブログモデルの定義
class Blog(Model):
    title = CharField()
    content = CharField()
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db 