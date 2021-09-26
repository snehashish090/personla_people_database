# An API for my application

from flask import *
import requests
from database import *

app = Flask(__name__)



@app.route("/api/all", methods=["GET"])
def home():
    with open("data/names.json", "r") as file:
        names = json.load(file)
    return jsonify(names)

@app.route("/api")
def val():
    with open("data/names.json", "r") as file:
        names = json.load(file)
    for i in names:
        if "first_name" in request.args:
            if request.args["first_name"] == i["first_name"]:
                return jsonify(i)
            else:
                pass
        else:
            return jsonify(names)

@app.route("/api/add")
def add_api():
    with open("data/names.json", "r") as file:
        names = json.load(file)

    names2 = []

    for i in names:
        names2.append(i["first_name"])
        
    if request.args["first_name"] not in names2:
        add_to_database(
            request.args["first_name"],
            request.args["last_name"],
            request.args["age"],
            request.args["gender"],
            request.args["email"],
            request.args["phone_no"],
            request.args["relation"],
        )
        return redirect("/api")

    else:
        return "No the the person already is there in your database"



    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")


