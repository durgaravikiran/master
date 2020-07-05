from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/hello")
def func():
    return "Hello"

@app.route("/welcome", methods=["POST"])
def func1():
    return {"message":{"x":10,"y":20}}


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)
