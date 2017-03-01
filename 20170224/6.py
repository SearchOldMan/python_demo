from flask import request,render_template,Flask

app = Flask(__name__)

@app.route('/login',methods=['POST','GET'])
def login():
	error = None
	if request.method == 'POST':
		if valid_login(request.form['username'],request.form['password']):
			return login_the_user_in(request.form['username'])
		else:
			error = 'Invalid username/password'

	return render_template('login.html',error=error)

def login_the_user_in(username):
	print 'hello %s'%username

app.run()