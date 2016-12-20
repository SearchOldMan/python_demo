from flask import Flask
app = Flask(__name__)

@app.route('/aa')
def aa():
    return 'ok!'

if __name__ == '__main__':
    app.run(debug=True)