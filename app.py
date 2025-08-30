from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime
import os

app = Flask(__name__)

# In-memory storage (replace with database in production)
proposals = []

@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/submit')
def submit_page():
    return render_template('submit.html')

@app.route('/submit', methods=['POST'])
def submit_proposal():
    data = {
        'timestamp': datetime.now().isoformat(),
        'title': request.form.get('title'),
        'subtitle': request.form.get('subtitle'),
        'description': request.form.get('description'),
        'problem': request.form.get('problem'),
        'github': request.form.get('github'),
        'youtube': request.form.get('youtube'),
        'email': request.form.get('email'),
        'website': request.form.get('website'),
        'eta': request.form.get('eta'),
        'investment': request.form.get('investment')
    }
    proposals.append(data)
    return render_template('proposal.html', proposal=data)

@app.route('/proposals')
def list_proposals():
    return render_template('proposals.html', proposals=proposals)

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy", "message": "Proposer.btc is running!"})

# Railway expects the app to be available as a variable
# This is the standard pattern for Railway deployments
if __name__ == '__main__':
    # Use Railway's PORT environment variable, fallback to 9999 for local development
    port = int(os.environ.get('PORT', 9999))
    # Use 0.0.0.0 to bind to all interfaces (required for Railway)
    print(f"Starting Proposer.btc on port {port}")
    app.run(debug=False, host='0.0.0.0', port=port)
