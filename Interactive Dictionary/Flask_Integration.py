from flask import Flask,jsonify,request
import json

data=json.load(open("data.json"))

app=Flask(__name__)

@app.route("/getValue",methods = ['POST'])
def getDictionaryItem():
    user_input = request.get_json()
    for name in data:
        if name.lower() == user_input["word given"].lower():
            return jsonify({'meaning':data[name]})

    return jsonify({'message':'Word Not Found!'})

app.run(port=5005)
