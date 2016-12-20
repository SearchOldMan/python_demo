from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/index/')
def index():
    return 'indexPage'
if __name__ == '__main__':
    app.run(debug=True)