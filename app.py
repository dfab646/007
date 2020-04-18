from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///mydb.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True
db = SQLAlchemy(app)
class User(db.Model):
    firstname = db.Column(db.Integer,primary_key=True,autoincrement=True)
    lastname =  db.Column(db.String)
    email = db.Column(db.String)
    password =  db.Column(db.String)
@app.route('/',methods=['GET','POST'])
def get():
    if request.method == "GET":
        users = User.query.all()
        user = User(firstname='',lastname='',email='',password='')
        pagename = 'home'
        return render_template('home.html',pagename=pagename,users=users,user=user)
    #else:
     #   firstname = request.form['firstname']
if __name__ == '__main__':
    app.run(debug=True)