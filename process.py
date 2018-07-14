from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
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


if __name__ == '__main__':
    app.run(debug=True)
