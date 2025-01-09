from models import User, db

def register_user():
    username = input("ユーザーネームを入力してください: ")
    password = input("パスワードを入力してください: ")

    try:
        user = User(username=username)
        user.set_password(password)
        user.save()
        print("ユーザーが正常に登録されました。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    db.connect()
    db.create_tables([User])
    register_user()
    db.close() 