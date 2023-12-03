# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Jenkins! Flask App Deployed on EC2."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
