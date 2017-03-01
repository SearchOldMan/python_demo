from flask import Flask

app = Flask(__name__)

@app.route('/user/<username>')
def show_username(username):
	return 'User %s'%username

app.run()
