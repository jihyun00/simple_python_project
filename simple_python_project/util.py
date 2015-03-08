from functools import wraps
from flask import redirect, url_for, session


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'key' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('get_login'))
    return decorated_function