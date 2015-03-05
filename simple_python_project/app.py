from flask import Flask, request, render_template, redirect, url_for, session, abort

from .model import User, Tag
from .db import db


config = {
    'SECRET_KEY': 'THIS_IS_SECRET_KEY',
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///../test.db',
}

app = Flask(__name__)
app.config.update(config)

db.init_app(app)


def get_user(user):
    return User.query.filter_by(name=user).first()


@app.route('/', methods=['GET'])
def index():
    if 'key' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.values.get('email')

    if username is None:
        abort(400)

    if get_user(username) is None:
        new_user = User(username)
        db.session.add(new_user)
        db.session.commit()
        session['key'] = new_user.key

    else:
        session['key'] = get_user(username).key

    return redirect(url_for('index'))


@app.route('/logout', methods=['GET'])
def logout():
    session.pop('key', None)
    return redirect(url_for('login'))


@app.route('/tags', methods=['GET'])
def get_tags():
    return render_template('tag.html')


@app.route('/tags', methods=['POST'])
def post_tags():
    if 'key' in session:
        tag = request.values.get('tag')

        if tag is None:
            abort(400)

        new_tag = Tag(tag)
        db.session.add(new_tag)
        db.session.commit()

        return redirect(url_for('get_tags'))
    else:
        return redirect(url_for('login'))


@app.route('/users/<name>/statistics', methods=['GET'])
def show_user_tag(name):
    return 'TAG List %s' % name


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404