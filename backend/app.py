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

@app.route("/graph", methods=['POST'])
def func2():
    return {"message":[
	{"a":{"x":10,"y":20}},
	{'b':{"x":10,"y":20}},
	{'c':{"x":10,"y":20}},
	{'d':{"x":10,"y":20}},
	{'e':{"x":10,"y":20}},
	{'f':{"x":10,"y":20}},
	{'g':{"x":10,"y":20}}]}

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)
