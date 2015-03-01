from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    #if login => return hello world
    #else => login page redirect
    return

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #db에 값 넣어서 ㅋㅋㅋㅋㅋㅋㅋㅋ
        return
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()