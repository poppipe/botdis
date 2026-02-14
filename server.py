from flask import Flask
from threading import Thread
app = Flask('')
@app.route('/')
def home():
    return "Sever is running!"
def run():
    app.run(host='0.0.0.0',post=8080)
def sever_on():
    t=Thread(target=run)
    t.start