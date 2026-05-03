from flask import Flask, render_template, request, redirect
import json, os

app = Flask(__name__)
DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE) as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.route("/")
def home():
    data = load_data()
    return render_template("index.html", items=data)

@app.route("/add", methods=["POST"])
def add():
    data = load_data()

    item = {
        "name": request.form["name"],
        "desc": request.form["desc"],
        "loc": request.form["loc"],
        "type": request.form["type"],
        "contact": request.form["contact"],
        "collect": request.form["collect"],
        "status": "Unclaimed"
    }

    data.append(item)
    save_data(data)

    return redirect("/")

@app.route("/claim/<int:index>")
def claim(index):
    data = load_data()
    data[index]["status"] = "Claimed"
    save_data(data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)