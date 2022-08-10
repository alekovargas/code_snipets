from flask import Flask
from Example_funtions import suma_simple

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello from flask'

@app.route('/service1',  methods=['POST'])
def service1():
    return str('mitexto1')


app.run()
