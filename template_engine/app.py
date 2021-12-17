from flask import Flask, render_template

app = Flask(__name__, template_folder="views")

@app.route("/templates")
def templates():
    user = {
        "name" : "Renato Oliveira",
        "idade" : 47,
        "email" : "renato@renato.com" 
    }
    return render_template("index.html", user=user)

if __name__ == "__main__":
    app.run(debug=True)