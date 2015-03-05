from flask.ext.script import Manager

from simple_python_project.app import app
from simple_python_project.db import db

manager = Manager(app)

@manager.command
def init_db():
    db.create_all()


@manager.command
def run(host='127.0.0.1', port=5000):
    app.run(debug=True, use_reloader=True, host=host, port=int(port))

if __name__ == '__main__':
    manager.run()