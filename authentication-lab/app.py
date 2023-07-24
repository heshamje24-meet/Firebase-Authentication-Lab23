from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyCfTAH8QoHIJ1MHaGnnWhD0rLD1FOLlW2g",
  'authDomain': "cs-is-lit.firebaseapp.com",
  "projectId": "cs-is-lit",
  "storageBucket": "cs-is-lit.appspot.com",
  "messagingSenderId": "1020758485639",
  "appId": "1:1020758485639:web:94f84ed24069bfa7b6a622",
  "measurementId": "G-N1QPDZPL7P",
  "databaseURL": ""
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    error=''
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        try:
            login_session['user']=auth.sign_in_with_email_and_password(email,password)
            return redirect(url_for('add_tweet'))
        except:
            error="authentiaction failed"
            return render_template("signin.html")
    else: 
        return render_template('signin.html')
    


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error=''
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        if len(password)>=6:
            try:
                login_session['user']=auth.create_user_with_email_and_password(email,password)
                return redirect(url_for('add_tweet'))
            except:
                error="authentiaction failed"
                return render_template("signup.html")
        else:
            return render_template("signup.html")
    else: 
        return render_template('signup.html')



@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)