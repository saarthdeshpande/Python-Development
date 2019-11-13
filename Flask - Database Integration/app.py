from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

@app.route("/adduser",methods = ["POST"])
def add_user():
    data = request.get_json()
    id_ = data["userid"]
    pw_ = data["password"]
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    sq = f"SELECT * FROM users where userid = '{id_}'"
    check = cursor.execute(sq)
    check = list(check)
    if len(check) > 0:
        connection.commit()
        connection.close()
        return jsonify({"Message": "Username Already Exists."})
    else:
        iq = "INSERT INTO users VALUES(?,?)"
        cursor.execute(iq,(id_,pw_))
        connection.commit()
        connection.close()
        return jsonify({"Message":"Successfully Added."})

@app.route("/display")
def disp():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    sq = "SELECT * FROM users"
    g = cursor.execute(sq)
    g = list(g)
    users = []
    for i in g:
        users.append({"userid":i[0],"password":i[1]})
    # execute returns a generator, which is like a pointer and points at database
    connection.close()
    return jsonify({"All Users: ":users})

@app.route("/login",methods = ["POST"])
def login():
    attempt = request.get_json()
    id_ = attempt["userid"]
    pw_ = attempt["password"]
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    sq = f"SELECT * FROM users where userid = '{id_}'"
    g = cursor.execute(sq)
    g = list(g)
    if len(g) > 0:
        if g[0][1] == pw_:
            connection.close()
            return jsonify({"Message":"Login Successful!"})
        else:
            connection.close()
            return jsonify({"Message":"Wrong Password. Try Again."})
    else:
        connection.close()
        return jsonify({"Error":"Username does not exist."})

app.run(port = 5051)