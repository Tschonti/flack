import os
import datetime
from flask import Flask, render_template, request, json, jsonify
from flask_socketio import SocketIO, emit
import sys

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

channels = {}

@app.route("/")
def index():
    return render_template("index.html", channels=channels)

@socketio.on("new channel")
def newchannel(data):
    if data["channame"] in channels:
        emit("invalidc", {"channame": data["channame"]}, broadcast=True)
    else:
        channels[data["channame"]] = []
        emit("nchannel", {"channame": data["channame"]}, broadcast=True)

@socketio.on("new message")
def newmessage(data):
    if data["channame"] not in channels:
        emit("invalidm", {"channame": data["channame"]}, broadcast=True)
    else:
        if len(channels[data["channame"]]) == 100:
            channels[data["channame"]].remove(channels[data["channame"]][0])
        timestamp = datetime.datetime.utcnow().strftime("%d/%m/%Y, %H:%M:%S")
        newmes = [data["user"], data["message"], timestamp]
        channels[data["channame"]].append(newmes)
        #print(data["message"], file=sys.stderr)
        emit("nmessage", {"user": data["user"], 'message': data["message"], "timestamp": timestamp, "channame": data["channame"]}, broadcast=True)

@app.route("/chanselect", methods=["POST"])
def chanselect():
    name = request.form.get("name")
    if name in channels:
        return json.dumps({'status':'OK', 'mes': channels[name], 'channame': name})
    else:
        return json.dumps({'status':'OK', 'mes':0})
