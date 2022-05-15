from flask import Flask,render_template,redirect,request,session
from flask_session import Session

app=Flask(__name__)

app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)

@app.route("/product")
def product():
    return render_template("product.html",url=request.args.get("url"),price=request.args.get("price"),pname=request.args.get("pname"), pdescribe=request.args.get("pdescribe"),stock=request.args.get("stock"))

@app.route("/delivery",methods=["GET","POST"])
def cart():
    if request.method=="POST":
        return redirect("/congrats")
    return render_template("delivery.html",prname=request.args.get("prname"))

@app.route("/congrats",methods=["GET","POST"])
def congrats():
    if request.method=="POST":
        return render_template("congrats.html")
    return redirect("/delivery")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        session["name"]=request.form.get("name")
        return redirect("/")
    return render_template("register.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        session["name"]=request.form.get("name")
        return redirect("/")
    return render_template("login.html")



@app.route("/logout")
def logout():
    session["name"]=None
    return redirect("/")


if __name__=="__main__":
    app.run(debug=False)