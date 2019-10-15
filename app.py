from flask import Flask
from flask import render_template as rt
from flask import request
import json
app = Flask(__name__)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return rt('hello.html')


if __name__ == "__main__":
    app.run()