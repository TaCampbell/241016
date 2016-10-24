from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"
	
@app.route("/name")
def nameonly():
	return "My name is Earl!"
	
@app.route("/name/<name>")
def name(name):
	return "My name is " + name
	
@app.route("/firstname", methods = ['GET'])
def gettest():
	var = request.args.get("firstname")
	return var
	
@app.route("/firstnamepost", methods = ['POST'])
def gettest2():
	var = request.form["firstname"]
	return var
	
@app.route('/hello/')
@app.route('/hello/<name>')
def hello1(name=None):
	return render_template('hello.html', name=name)
	
if __name__=="__main__":
	app.run()