from flask import Flask,request,url_for,redirect,flash,render_template

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login',methods=['POST','GET'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'secret':
			error = 'Invalid credentials'
		else:
			flash('You were successful login')
			return redirect(url_for('index.html'))

	return render_template('login1.html',error=error)

app.run()