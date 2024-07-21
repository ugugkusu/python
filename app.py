from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def hello_world():
    if request.method == "GET":
       return render_template("login.html")
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if not username or not password:
            error = "Kullanıcı adı yada şifre boş olamaz.."
            return render_template("login.html", error=error)
        if username == "mendebur" and password == "taklaci_guvercin_34":
            return send_from_directory("uploads/", "world2.zip")
        else:
            error = "Kullanıcı adı yada şifre yanlış.."
            return render_template("login.html", error=error)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
