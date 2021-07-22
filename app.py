from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html")

users = {
    "tugba": "12345",
    "linda": "6789",
    "thomas": "nl234"
}

@app.route("/login", methods=["POST", "GET"])
def login():
    user = request.form["username"]
    password = request.form["password"]
    if user in users:
        if users[user] == password:
            return render_template("home.html", name = user)
        else:
            return render_template("login.html", info="invalid password")
    else:
        return render_template ("login.html", info="invalid user")

if __name__ == "__main__":
    app.run(debug = True)




