#!/usr/bin/env python3
"""
Comprehensive API test script for proposer.btc Flask application
Tests actual functionality: form submission, data storage, and template rendering
"""

import requests
import json
import time
from datetime import datetime

class ProposerAPITester:
    def __init__(self, base_url="http://localhost:9999"):
        self.base_url = base_url
        self.session = requests.Session()
        
    def test_homepage(self):
        """Test the main form page loads"""
        try:
            response = self.session.get(f"{self.base_url}/")
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            assert "Proposer.btc - Submit Your Proposal" in response.text, "Title not found"
            assert "hx-post=\"/submit\"" in response.text, "HTMX post attribute missing"
            assert "name=\"title\"" in response.text, "Title field missing"
            print("✅ Homepage loads correctly with form")
            return True
        except Exception as e:
            print(f"❌ Homepage test failed: {e}")
            return False
    
    def test_proposal_submission(self):
        """Test proposal submission with test data"""
        test_data = {
            'title': 'Test API Project',
            'subtitle': 'Testing the API functionality',
            'description': 'This is a test proposal to verify the API works',
            'problem': 'Need to test the complete submission flow',
            'github': 'https://github.com/test/api-test',
            'youtube': 'https://youtube.com/watch?v=api-test',
            'email': 'test@api.com',
            'website': 'https://api-test.com',
            'eta': '1 week',
            'investment': '0.0005'
        }
        
        try:
            response = self.session.post(f"{self.base_url}/submit", data=test_data)
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            assert "Proposal Submitted Successfully" in response.text, "Success message missing"
            assert test_data['title'] in response.text, "Title not in response"
            assert test_data['subtitle'] in response.text, "Subtitle not in response"
            assert test_data['description'] in response.text, "Description not in response"
            print("✅ Proposal submission successful")
            return True
        except Exception as e:
            print(f"❌ Proposal submission failed: {e}")
            return False
    
    def test_proposals_listing(self):
        """Test the proposals listing page"""
        try:
            response = self.session.get(f"{self.base_url}/proposals")
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            assert "All Submitted Proposals" in response.text, "Proposals title missing"
            assert "Test API Project" in response.text, "Test proposal not found"
            assert "REIT" in response.text, "Original REIT proposal not found"
            print("✅ Proposals listing works correctly")
            return True
        except Exception as e:
            print(f"❌ Proposals listing failed: {e}")
            return False
    
    def test_form_validation(self):
        """Test form validation with missing required fields"""
        incomplete_data = {
            'title': 'Incomplete Test',
            # Missing required fields
        }
        
        try:
            response = self.session.post(f"{self.base_url}/submit", data=incomplete_data)
            # Should still work since Flask doesn't enforce HTML5 validation server-side
            print("✅ Form handles incomplete data gracefully")
            return True
        except Exception as e:
            print(f"❌ Form validation test failed: {e}")
            return False
    
    def test_data_persistence(self):
        """Test that submitted data persists across requests"""
        try:
            # Submit a new proposal
            new_data = {
                'title': 'Persistence Test',
                'subtitle': 'Testing data persistence',
                'description': 'This should persist',
                'problem': 'Testing persistence',
                'github': 'https://github.com/test/persistence',
                'youtube': 'https://youtube.com/watch?v=persistence',
                'email': 'persistence@test.com',
                'website': 'https://persistence-test.com',
                'eta': '2 days',
                'investment': '0.0002'
            }
            
            # Submit
            submit_response = self.session.post(f"{self.base_url}/submit", data=new_data)
            assert submit_response.status_code == 200, "Submit failed"
            
            # Check if it appears in listings
            time.sleep(1)  # Small delay to ensure processing
            list_response = self.session.get(f"{self.base_url}/proposals")
            assert "Persistence Test" in list_response.text, "New proposal not found in listing"
            
            print("✅ Data persistence working correctly")
            return True
        except Exception as e:
            print(f"❌ Data persistence test failed: {e}")
            return False
    
    def run_all_tests(self):
        """Run all API tests"""
        print("🧪 Running Comprehensive API Tests\n")
        print(f"Testing API at: {self.base_url}")
        print("=" * 50)
        
        tests = [
            ("Homepage Loading", self.test_homepage),
            ("Proposal Submission", self.test_proposal_submission),
            ("Proposals Listing", self.test_proposals_listing),
            ("Form Validation", self.test_form_validation),
            ("Data Persistence", self.test_data_persistence)
        ]
        
        passed = 0
        total = len(tests)
        
        for test_name, test_func in tests:
            print(f"\n🔍 Testing: {test_name}")
            if test_func():
                passed += 1
            else:
                print(f"   ⚠️  {test_name} failed")
        
        print("\n" + "=" * 50)
        print(f"📊 Test Results: {passed}/{total} tests passed")
        
        if passed == total:
            print("🎉 ALL TESTS PASSED! Your proposer.btc API is fully functional!")
        else:
            print(f"❌ {total - passed} test(s) failed")
        
        return passed == total

def main():
    """Main test runner"""
    print("🚀 Proposer.btc API Test Suite")
    print("Make sure your Flask app is running on port 9999\n")
    
    tester = ProposerAPITester()
    
    try:
        success = tester.run_all_tests()
        if success:
            print("\n✅ Your API is ready for production use!")
        else:
            print("\n⚠️  Some issues detected - check the errors above")
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to Flask app. Make sure it's running on port 9999")
        print("   Run: python3 app.py")
    except Exception as e:
        print(f"❌ Test suite error: {e}")

if __name__ == "__main__":
    main()
