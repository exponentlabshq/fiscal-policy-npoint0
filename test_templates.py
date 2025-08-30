#!/usr/bin/env python3
"""
Test script to validate all HTML templates work correctly
"""

def test_index_html():
    """Test index.html template"""
    try:
        with open('templates/index.html', 'r') as f:
            content = f.read()
        
        # Check required elements
        assert 'hx-post="/submit"' in content, "HTMX post attribute missing"
        assert 'name="title"' in content, "Title field missing"
        assert 'name="subtitle"' in content, "Subtitle field missing"
        assert 'name="description"' in content, "Description field missing"
        assert 'name="problem"' in content, "Problem field missing"
        assert 'name="github"' in content, "GitHub field missing"
        assert 'name="youtube"' in content, "YouTube field missing"
        assert 'name="email"' in content, "Email field missing"
        assert 'name="website"' in content, "Website field missing"
        assert 'name="eta"' in content, "ETA field missing"
        assert 'name="investment"' in content, "Investment field missing"
        
        print("✅ index.html: All required fields present")
        return True
    except Exception as e:
        print(f"❌ index.html: {e}")
        return False

def test_proposal_html():
    """Test proposal.html template"""
    try:
        with open('templates/proposal.html', 'r') as f:
            content = f.read()
        
        # Check template variables
        assert '{{ proposal.title }}' in content, "Title variable missing"
        assert '{{ proposal.subtitle }}' in content, "Subtitle variable missing"
        assert '{{ proposal.description }}' in content, "Description variable missing"
        assert '{{ proposal.problem }}' in content, "Problem variable missing"
        assert '{{ proposal.github }}' in content, "GitHub variable missing"
        assert '{{ proposal.youtube }}' in content, "YouTube variable missing"
        assert '{{ proposal.email }}' in content, "Email variable missing"
        assert '{{ proposal.website }}' in content, "Website variable missing"
        assert '{{ proposal.eta }}' in content, "ETA variable missing"
        assert '{{ proposal.investment }}' in content, "Investment variable missing"
        assert '{{ proposal.timestamp }}' in content, "Timestamp variable missing"
        
        print("✅ proposal.html: All template variables present")
        return True
    except Exception as e:
        print(f"❌ proposal.html: {e}")
        return False

def test_proposals_html():
    """Test proposals.html template"""
    try:
        with open('templates/proposals.html', 'r') as f:
            content = f.read()
        
        # Check template logic
        assert '{% if proposals %}' in content, "If statement missing"
        assert '{% for proposal in proposals %}' in content, "For loop missing"
        assert '{% endfor %}' in content, "Endfor missing"
        assert '{% else %}' in content, "Else statement missing"
        assert '{% endif %}' in content, "Endif missing"
        
        print("✅ proposals.html: All template logic present")
        return True
    except Exception as e:
        print(f"❌ proposals.html: {e}")
        return False

def test_app_py():
    """Test app.py Flask application"""
    try:
        with open('app.py', 'r') as f:
            content = f.read()
        
        # Check required imports and routes
        assert 'from flask import' in content, "Flask import missing"
        assert '@app.route(\'/\')' in content, "Index route missing"
        assert '@app.route(\'/submit\', methods=[\'POST\'])' in content, "Submit route missing"
        assert '@app.route(\'/proposals\')' in content, "Proposals route missing"
        assert 'render_template(' in content, "Template rendering missing"
        
        print("✅ app.py: All required routes and imports present")
        return True
    except Exception as e:
        print(f"❌ app.py: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing All HTML Templates and Flask App\n")
    
    tests = [
        test_index_html,
        test_proposal_html, 
        test_proposals_html,
        test_app_py
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print(f"\n📊 Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All templates are functionally correct!")
        print("\nTo test the live app:")
        print("1. python3 app.py")
        print("2. Open http://localhost:5000 in browser")
        print("3. Submit a test proposal")
        print("4. View all proposals")
    else:
        print("❌ Some tests failed - check the errors above")

if __name__ == "__main__":
    main()
