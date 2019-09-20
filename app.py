from flask import Flask, request, Response, render_template, redirect, flash, url_for, session
# import hashlib
from passlib.hash import sha256_crypt
import psycopg2


connection=psycopg2.connect(
    host="0.0.0.0",
    database="tech_db_name",
    user="postgres",
    password="shadyshady"
)
# cursor=connection.cursor()

# file=open("data.sql","r")
# cursor.execute(file.read())


# connection.commit()
# print("OK")

app=Flask('app')
app.secret_key="userlogin"


@app.route("/", methods=["GET", "POST"])
def main_index():
    
    if request.method == "GET":
        return redirect("/movies")


@app.route("/movies", methods=["GET", "POST"])
def movie_index():
    context = {
            "data": "movie",
            
        }
    if request.method == "GET":
        return render_template("index.html",**context)

@app.route("/random", methods=["GET", "POST"])
def random_index():
    a="random"
    if request.method == "GET":
        return render_template("index.html")

@app.route("/last24h", methods=["GET", "POST"])
def last24_index():
    
    if request.method == "GET":
        return render_template("24h.html")



@app.route("/signup", methods=["GET", "POST"])
def mai_index():
    if request.method == "GET":
        return render_template("sign.html")
    else:
        name=request.form["full_name"]
        email=request.form["email"]
        password=sha256_crypt.encrypt(request.form["password"])

        cursor=connection.cursor()
        cursor.execute(f"INSERT INTO users_sign (full_name, email, password) VALUES ('{name}','{email}','{password}');")
        connection.commit()

        return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def log_index():
    if request.method == "GET":
        return render_template("login.html")
    else:  
        
        email=request.form["email"]
        password=request.form["password"]
        cursor=connection.cursor()
        cursor.execute(f"SELECT * FROM users_sign WHERE email='{email}'")
        data = cursor.fetchone()
        connection.commit()
        if data:
               if sha256_crypt.verify(password,data[3]):
                       flash("basariyla giris yaptiniz","success")

                       session["logged_in"]=True
                       session["username"]=data[1]
                       return redirect(url_for("main_index"))
               else:
                       flash("Invalid password","danger")
                       return redirect(url_for("log_index"))
        else:
                flash("Invalid email","danger")
                return redirect(url_for("log_index"))


@app.route("/logout")
def logout_html():
    session.clear()
    return render_template("index.html")

    




app.run(debug=True, host='0.0.0.0', port=5000)

# print(sha256_crypt.verify("12345", "$5$rounds=535000$9BkFr2l9nkkctFaT$VToahfdE1EZQg4Czg.i0S.OQ6U8pVVoc7Lin8FxNmb2"))