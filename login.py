from models import User, db

def login():
    username = input("ユーザーネームを入力してください: ")
    password = input("パスワードを入力してください: ")

    try:
        user = User.get(User.username == username)
        if user.check_password(password):
            print("ログインに成功しました。")
        else:
            print("パスワードが間違っています。")
    except User.DoesNotExist:
        print("ユーザーが存在しません。")

if __name__ == "__main__":
    db.connect()
    login()
    db.close() 