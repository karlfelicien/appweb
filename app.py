from flask import Flask,redirect,request,render_template,url_for,session



app = Flask(__name__)
app.secret_key = "95333b1b491083c50ff0f9478e2db06ab7a5a5018627d6834e36b4e571882a91"

dico = [{"nom":"kargl","mdp":1234},{"nom":"kaco","mdp":12345},{"nom":"leon","mdp":123456}]



@app.route("/")
def home():


    return render_template("imagehtml.html")


def utilisateur(nom,mdp):

    for i in dico :
        if i["nom"] == nom and i["mdp"] == mdp:
            return i

@app.route("/login")
def login():


    return render_template("formulaire.html")

@app.route("/compteur",methods=["GET","POST"])
def compteur():

    if request.method == 'POST':

        donnees = request.form
        nom = donnees.get("nom")
        mdp = int(donnees.get("mdp"))

        utilisateurs = utilisateur(nom,mdp)

        if utilisateurs is not None:

            if "utilisateur" not in session:
                
                session["utilisateur"] = nom
                session["visiteur"] = 1
                return dict(session)
            
            
            
            else:
                
                session["visiteur"] = session["visiteur"] + 1
            
                return dict(session)

        else:
            return redirect(url_for("login"))

    else:
        if "user" in session:
            return redirect(url_for("home"))

        else:
            return redirect(url_for("login"))





if __name__ == '__main__':

    app.run(port=5000,host="192.168.1.75",debug=True)

