from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Railway! Proposer.btc is working!"

@app.route('/health')
def health():
    return "OK"

if __name__ == '__main__':
    # Railway will set PORT environment variable
    port = int(os.environ.get('PORT', 8080))
    print(f"Starting app on port {port}")
    print(f"PORT env var: {os.environ.get('PORT', 'not set')}")
    app.run(host='0.0.0.0', port=port)
