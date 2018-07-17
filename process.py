from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from flask_login import UserMixin, LoginManager, login_required, current_user, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://XXXXX' #若是本地sqlite3:'sqlite:///XXX.db'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# from Entity import *

# db.create_all()
# db.session.commit()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(15), unique=True)
    Email = db.Column(db.String(50), unique=True)
    Password = db.Column(db.String(80))


@login_manager.user_loader
def load_user(user_id):  # 透過這邊的設置讓flask_login可以隨時取到目前的使用者id
    return User.query.get(int(user_id))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form')
@login_required
def form():
    return render_template('form.html', name=current_user.Username)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")

    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(
        Username=username).first()  # 查詢 database 是否有該用戶
    if user:
        if check_password_hash(user.Password, password):  # 比對輸入的密碼跟註冊時的 hash 密碼
            login_user(user, remember=True)  # 利用 login_user 登入
            if current_user.is_authenticated:
                print(current_user.is_authenticated)  # 當用戶通過驗證，返回 True
                # 若為 True，才能通過 login_required
            return redirect(url_for('form'))  # 登入成功後，導入 form 頁面

    return render_template("login.html", error="Error !")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    hashed_password = generate_password_hash(
        password, method='sha256')
    # 將輸入的資料存入資料庫
    newAccount = User(
        Username=username, Email=email, Password=hashed_password)
    db.session.add(newAccount)
    db.session.commit()

    return redirect(url_for("index"))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
