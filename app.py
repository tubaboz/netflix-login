from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html")

users = {
    "tugba.bozteke@gmail.com": "12345",
    "0618895678": "6789",
    "john@gmail.com": "nl234"
}

@app.route("/login", methods=["POST", "GET"])
def login():
    user = request.form["username"]
    password = request.form["password"]
    if user in users:
        if users[user] == password:
            return render_template("home.html", name = user)
        else:
            return render_template("login.html", feedback="Invalid password. Please try again.")
    else:
        return render_template ("login.html", feedback="Sorry, We can't find an account with this email adress. Please try again.")

if __name__ == "__main__":
    app.run(debug = True)




