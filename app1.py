from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World! This is my first flask app'

@app.route('/login')
def login():
    return 'No passwords, all welecome'

@app.route('/predict')
def predict():
    return 'No Snow Tomorrow!'

if __name__ == '__main__':
    app.run(port= 4000)