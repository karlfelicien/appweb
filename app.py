from flask import Flask,redirect,request,render_template,url_for,session



app = Flask(__name__)


@app.route("/")
def home():


    return render_template("index.html")



@app.route("/login")
def login():


    return render_template("formulaire.html")


        



if __name__ == '__main__':

    app.run(debug=True)

