from flask import Flask,request,make_response
app = Flask(__name__)

@app.route('/')
def index():
	resp = make_response(render_template('login.html'))
	resp.set_cookie('username','the username')
	return resp

app.run()