from flask import Flask, request, render_template, redirect, url_for, session, abort

from .model import User, Tag
from .db import db
from .util import login_required


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
@login_required
def index():
    return render_template('index.html')


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
        session['username'] = new_user.name
        session['key'] = new_user.key

    else:
        session['username'] = username
        session['key'] = get_user(username).key

    return redirect(url_for('index'))


@app.route('/logout', methods=['GET'])
def logout():
    session.pop('username', None)
    session.pop('key', None)

    return redirect(url_for('login'))


@app.route('/tags', methods=['GET'])
@login_required
def get_tags():
    return render_template('tag.html')


@app.route('/tags', methods=['POST'])
@login_required
def post_tags():
    tag = request.values.get('tag')
    username = session['username']

    if tag is None:
        abort(400)

    new_tag = Tag(tag, username)
    db.session.add(new_tag)
    db.session.commit()

    return redirect(url_for('get_tags'))


@app.route('/users/<name>/statistics', methods=['GET'])
def show_user_tag(name=None):
    tags = Tag.query.filter_by(username=name).all()
    # count = db.query(User.group, db.label('members', db.func.count(User.id)), db.label('total_balance', db.func.sum(User.balance))).group_by(User.group).all()

    return render_template('statistics.html', tags=tags)



@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404