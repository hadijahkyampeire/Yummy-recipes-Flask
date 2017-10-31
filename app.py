from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')
@app.route("/showsignup")
def showsignup():
    return render_template('signup.html')
@app.route("/showlogin")
def showlogin():
	return render_template('login.html')
@app.route('/viewrecipes')
def viewrecipes():
	return render_template('addrecipe.html')

if __name__=="__main__":
    app.run(debug=True)
    