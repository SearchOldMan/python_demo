from flask import Flask,escape,redirect,url_for,session,request

app = Flask(__name__)

@app.route('/')
def index():
	if 'username' in session:
		return 'logged in as %s' % escape(session['username'])
	return 'You are not logged in'

@app.route('/login',methods=['POST','GET'])
def login():
	if request.method == 'POST':
		session['username'] = request.form['username']
	return '''
		<form method='post'>
			<p><input type="text" name="username"/></p>
			<p><input type="submit" value="login"/></p>
		</form>
	'''
@app.route('/logout')
def logout():
	session.pop('username',None)
	return redirect(url_for('index'))

app.secret_key = '2\xcc_o\x9f9\x1c\xae\\x87\xe1\xec\xc9g)I\\x15\xe9$<WS\xf5\xed*'

app.run()