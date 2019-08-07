from flask import Blueprint, render_template, jsonify, request
import redis
from tesdaq.command import DAQCommander
r = redis.Redis()
control = Blueprint(
        "control",
        __name__,
        static_folder="./view/dist",
        template_folder='./view'
        )

daq_cmd = DAQCommander(r)

@control.route("/")
def render():
    return render_template("index.html")

@control.route("/active-devices/")
def return_active():
    return jsonify(daq_cmd.get_active_devices())

@control.route("/device/<dev>", methods=["GET"])
def return_device(dev):
    return jsonify(daq_cmd.get_device_config(dev))

@control.route("/start-run/", methods=["POST"])
def start_run():
    print(request.form)
    for key, value in request.form[0]:
        print(key, value)
    return jsonify(0)
