from flask import Flask, render_template, request, jsonify
from database import db
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/submit')
def submit_page():
    return render_template('submit.html')

@app.route('/submit', methods=['POST'])
def submit_proposal():
    data = {
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
    
    # Add proposal to persistent database
    proposal = db.add_proposal(data)
    
    return render_template('proposal.html', proposal=proposal)

@app.route('/proposals')
def list_proposals():
    proposals = db.get_all_proposals()
    return render_template('proposals.html', proposals=proposals)

@app.route('/health')
def health_check():
    stats = db.get_statistics()
    return jsonify({
        "status": "healthy", 
        "message": "Proposer.btc is running!",
        "database_stats": stats
    })

@app.route('/api/proposals')
def api_proposals():
    """API endpoint to get all proposals as JSON."""
    proposals = db.get_all_proposals()
    return jsonify(proposals)

@app.route('/api/proposals/<int:proposal_id>')
def api_proposal(proposal_id):
    """API endpoint to get a specific proposal by ID."""
    proposal = db.get_proposal_by_id(proposal_id)
    if proposal:
        return jsonify(proposal)
    return jsonify({"error": "Proposal not found"}), 404

@app.route('/api/search')
def api_search():
    """API endpoint to search proposals."""
    query = request.args.get('q', '')
    if query:
        results = db.search_proposals(query)
        return jsonify(results)
    return jsonify([])

@app.route('/api/stats')
def api_stats():
    """API endpoint to get database statistics."""
    stats = db.get_statistics()
    return jsonify(stats)

if __name__ == '__main__':
    # Railway will set PORT environment variable, default to 8080
    port = int(os.environ.get('PORT', 8080))
    print(f"Starting Proposer.btc on port {port}")
    print(f"Database file: {db.db_file}")
    app.run(host='0.0.0.0', port=port)
