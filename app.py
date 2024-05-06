from flask import *

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login',methods=['GET','POST'])

def login():
    uname=request.form['uname']
    passwrd=request.form['pass']

    if uname=="ayush" and passwrd=="google":
        return "welcome to marklance"


if __name__=='__main__':
    app.run(debug=True)
