from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def start():
    return "home page mamalesh"

@app.route("/mamalesh")
def mbsa():
    return render_template('index.html')

