from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Railway! Proposer.btc is working!'

@app.route('/health')
def health():
    return 'OK'
