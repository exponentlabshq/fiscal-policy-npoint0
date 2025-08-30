from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime

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

if __name__ == '__main__':
    app.run(debug=True, port=9999)
