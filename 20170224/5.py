from flask import Flask,render_template
app = Flask(__name__)

@app.route('/user/')
@app.route('/user/<username>')
def login(username=None):
	return render_template('hello.html',username=username)

app.run()