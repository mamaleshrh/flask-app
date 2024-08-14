from flask import Flask, render_template, request, jsonify
from rating import get_difficulty
import requests
app = Flask(__name__)

@app.route("/")
def start():
    return "home page mamalesh"


@app.route('/get-data', methods=['GET'])
def get_data():
    # Access query parameters using request.args
    key = request.args.get('key')
    return jsonify({"received_key": key})


@app.route("/mamalesh")
def mbsa():
    return render_template('index.html')

