from flask import Flask, request, render_template, redirect, url_for, session

from model import User

app = Flask(__name__)

app.secret_key = 'THIS_IS_SECRET_KEY'
app.config['SESSION_TYPE'] = 'filesystem'


@app.route('/', methods=['GET'])
def index():
    if 'key' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        new_user = User(request.form['email'])
        session['key'] = new_user.reset_key()
        return redirect(url_for('index'))
    else:
        return render_template('login.html')


@app.route('/logout', methods=['GET'])
def logout():
    session.pop('key', None)
    return redirect(url_for('login'))


@app.route('/tags', methods=['GET', 'POST'])
def tags():
    if 'key' in session:
        if request.method == 'POST':
            return redirect(url_for('tags'))
        else:
            return render_template('tag.html')
    else:
        return redirect(url_for('login'))


@app.route('/users/<name>/statistics', methods=['GET'])
def show_user_tag(name):
    return 'TAG List %s' % name


if __name__ == '__main__':
    app.run(debug=True)