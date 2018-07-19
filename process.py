from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    message = 'Login'
    return render_template('index.html', **locals())


@app.route('/form')
def form():
    Description = 'Flask Ajax Practice'
    return render_template('form.html', **locals())


@app.route('/process', methods=['POST'])
def process():
    # 接收表單資料
    email = request.form['email']
    name = request.form['name']
    # 確認有資料後，回傳給前端
    if name and email:
        newName = name + ' submit success !'
        newEmail = email + ' submit success !'

        return jsonify({'name': newName, 'email': newEmail})

    return jsonify({'error': 'Missing data!'})


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get('name')
        password = request.form.get('pwd')
        # 帳號密碼正確的話，直接導向 /form
        if username == "abc" and password == "abc":
            return redirect(url_for('form'))
        else:
            message = 'Login Failure ! Please try again.'
            return render_template('index.html', **locals())
    else:
        message = 'Login Failure ! Please try again.'
        return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)
