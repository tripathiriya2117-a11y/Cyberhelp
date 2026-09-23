"""
Automated Test & Verification Script for CyberHelp Flask Application
"""
import os
import sys
import tempfile
import unittest
import json
import re

# ============================================================
# TEST ENVIRONMENT CONFIGURATION - MUST BE BEFORE APP IMPORT
# ============================================================

# Create a temporary database file for testing
TEST_DB_FD, TEST_DB_PATH = tempfile.mkstemp(suffix='_test.db')
os.close(TEST_DB_FD)  # We just need the path; SQLite will create the file

# Set test-only environment variables BEFORE importing app
os.environ["SECRET_KEY"] = "test-secret-key-only"
os.environ["ADMIN_USERNAME"] = "test_admin"
os.environ["ADMIN_PASSWORD"] = "test-password-only"
os.environ["GEMINI_API_KEY"] = ""
os.environ["FLASK_DEBUG"] = "0"
os.environ["FLASK_ENV"] = "testing"
os.environ["DATABASE_PATH"] = TEST_DB_PATH

# Now import app and db (they will use the test database)
from app import app
from db import get_db, seed_db

class CyberHelpTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Initialize test database once for all tests."""
        # Ensure database is initialized with test credentials
        with app.app_context():
            seed_db()
            # Add quiz questions for testing (since seed.sql is skipped in test mode)
            conn = get_db()
            quiz_questions = [
                (1, 'You receive an urgent SMS claiming your bank account will be deactivated within 2 hours unless you click a bit.ly link to complete KYC. What is the safest course of action?', 'Click the link immediately to prevent account suspension', 'Forward the link to family members so they can check their accounts too', 'Ignore the link, delete the SMS, and verify with your bank using their official app or branch number', 'Reply to the SMS with your bank account number and Aadhaar number', 'C'),
                (2, 'A buyer on OLX sends you a PhonePe QR code saying "Scan this and enter your UPI PIN to receive the Rs 5,000 payment". What will happen if you scan and enter your PIN?', 'You will receive Rs 5,000 in your bank account', 'Rs 5,000 will be deducted from YOUR bank account', 'The QR code will simply verify your account name without money movement', 'The transaction will be held in safe escrow until delivery', 'B'),
                (3, 'What is the primary security advantage of Two-Factor Authentication (2FA)?', 'It makes web pages load twice as fast', 'It requires an additional verification step (like an authenticator code) even if your password is stolen', 'It eliminates the need for strong passwords', 'It allows multiple people to share the same account simultaneously', 'B'),
                (4, 'A technical support caller claims your computer has a critical virus and asks you to install AnyDesk or TeamViewer QuickSupport. What should you do?', 'Install it immediately to prevent data corruption', 'Refuse and hang up, because these apps give the caller full remote control of your screen and device', 'Install the app, but only read out the 9-digit code if they show a company ID card', 'Install it and leave the computer unattended while they fix it', 'B'),
                (5, 'What is the official Indian National Emergency Helpline number for reporting cyber financial fraud immediately to freeze stolen funds?', '100', '108', '1930', '1091', 'C'),
                (6, 'Which of the following passwords has the highest security strength against automated brute-force attacks?', 'Password123!', 'Rohan@2023', 'correct-horse-battery-staple-9#Solar', '1234567890Aa', 'C'),
                (7, 'You receive a WhatsApp video call from a person in a police uniform claiming an illegal drug parcel was seized in your name and you are under "Digital Arrest". What is the reality?', 'You are legally obligated to stay on video call and transfer verification funds', 'Indian law enforcement agencies do not conduct arrests or trial procedures over WhatsApp/Skype video calls', 'You should immediately transfer your savings to the "RBI security account" they provide', 'You must keep it confidential and not inform your family', 'B'),
                (8, 'Which of the following URL structures indicates a high likelihood of a phishing website attempting to mimic State Bank of India?', 'https://www.onlinesbi.sbi/portal/login.html', 'https://retail.onlinesbi.sbi/', 'http://onlinesbi.secure-login-verification.xyz/sbi/auth', 'https://www.sbi.co.in', 'C'),
                (9, 'What is "Juice Jacking"?', 'A scam where fraudsters steal fruit juice delivery orders', 'A cyber attack where malware is loaded or data is copied from a device via a public USB charging port', 'Overcharging mobile phone batteries to cause physical damage', 'A technique to bypass SIM lock PINs using NFC', 'B'),
                (10, 'In cyber financial fraud, what is meant by the "Golden Hour"?', 'The time of day when cyber police are off duty', 'The initial 1 to 2 hours after a fraudulent transaction when calling 1930 has the highest chance of freezing funds in transit', 'The time it takes for a bank to issue a new debit card', 'The time required to reset your internet banking password', 'B'),
            ]
            for q in quiz_questions:
                conn.execute(
                    "INSERT OR IGNORE INTO quiz_questions (question_id, question_text, option_a, option_b, option_c, option_d, correct_option, admin_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                    (q[0], q[1], q[2], q[3], q[4], q[5], q[6], 1)
                )
            conn.commit()
            conn.close()

    @classmethod
    def tearDownClass(cls):
        """Clean up test database after all tests."""
        try:
            if os.path.exists(TEST_DB_PATH):
                os.remove(TEST_DB_PATH)
        except Exception:
            pass

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = True
        self.client = app.test_client()

    def get_csrf_token(self, response):
        """Extract CSRF token from response HTML."""
        match = re.search(r'name="csrf_token" value="([^"]+)"', response.get_data(as_text=True))
        if match:
            return match.group(1)
        return None

    def test_public_routes(self):
        routes = ['/', '/awareness', '/scams', '/tools', '/quiz', '/faqs', '/reporting', '/chatbot']
        for r in routes:
            resp = self.client.get(r)
            self.assertEqual(resp.status_code, 200, f"Route {r} failed with status {resp.status_code}")
            print(f"[PASS] GET {r} -> 200 OK")

    def test_url_checker_api(self):
        # Test safe url
        resp = self.client.post('/api/check-url', 
                                data=json.dumps({'url': 'https://cybercrime.gov.in'}),
                                content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertEqual(data['risk_score'], 0)
        print("[PASS] URL Checker: Safe domain detected properly.")

        # Test phishing heuristic url
        resp2 = self.client.post('/api/check-url',
                                 data=json.dumps({'url': 'http://secure-sbi-online.update-login.xyz/login.php'}),
                                 content_type='application/json')
        self.assertEqual(resp2.status_code, 200)
        data2 = resp2.get_json()
        self.assertGreaterEqual(data2['risk_score'], 50)
        self.assertIn('DANGEROUS', data2['verdict'])
        print("[PASS] URL Checker: Phishing domain flagged with high risk score.")

    def test_quiz_submission_api(self):
        submission = {
            'answers': {
                '1': 'C',
                '2': 'B',
                '3': 'B',
                '4': 'B',
                '5': 'C'
            }
        }
        resp = self.client.post('/api/quiz/submit',
                                data=json.dumps(submission),
                                content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertEqual(data['score'], 5)
        self.assertGreaterEqual(data['total'], 5)
        print(f"[PASS] Quiz Submission API: Verified score {data['score']}/{data['total']} ({data['percentage']}%)")

    def test_chatbot_api(self):
        resp = self.client.post('/api/chat',
                                data=json.dumps({'message': 'I received a message saying my electricity bill is unpaid. Is it a scam?'}),
                                content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertTrue('reply' in data)
        self.assertTrue(len(data['reply']) > 20)
        print(f"[PASS] Chatbot API: Received response ({data.get('source', '')})")

    def test_admin_auth_and_crud(self):
        # Get login page to obtain CSRF token
        login_page = self.client.get('/admin/login')
        csrf_token = self.get_csrf_token(login_page)
        self.assertIsNotNone(csrf_token, "CSRF token should be present in login form")

        # Test login with CSRF token
        resp = self.client.post('/admin/login', data={
            'username': 'test_admin',
            'password': 'test-password-only',
            'csrf_token': csrf_token
        }, follow_redirects=True)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Helpdesk Content', resp.data)
        print("[PASS] Admin Login: Successfully authenticated.")

        # Test creating awareness article (need new CSRF token from authenticated session)
        # Get admin awareness page to get fresh CSRF token
        admin_page = self.client.get('/admin/awareness')
        csrf_token = self.get_csrf_token(admin_page)
        self.assertIsNotNone(csrf_token, "CSRF token should be present in admin form")

        create_resp = self.client.post('/admin/awareness', data={
            'action': 'create',
            'title': 'Automated Test Article',
            'category': 'Test Category',
            'description': 'This is a test description generated by automated verification test.',
            'csrf_token': csrf_token
        }, follow_redirects=True)
        self.assertEqual(create_resp.status_code, 200)
        self.assertIn(b'Automated Test Article', create_resp.data)
        print("[PASS] Admin CRUD: Created awareness guide.")

        # Clean up test article
        conn = get_db()
        conn.execute("DELETE FROM awareness_content WHERE title = 'Automated Test Article'")
        conn.commit()
        conn.close()
        print("[PASS] Admin CRUD: Cleanup verified.")

    def test_csrf_protection_on_admin_login(self):
        """Test that admin login rejects requests without valid CSRF token."""
        # Attempt login without CSRF token
        resp = self.client.post('/admin/login', data={
            'username': 'test_admin',
            'password': 'test-password-only'
        }, follow_redirects=True)
        # Should be rejected with 400
        self.assertEqual(resp.status_code, 400)
        print("[PASS] CSRF Protection: Admin login rejects missing CSRF token")

    def test_csrf_protection_on_admin_crud(self):
        """Test that admin CRUD rejects requests without valid CSRF token."""
        # First login properly
        login_page = self.client.get('/admin/login')
        csrf_token = self.get_csrf_token(login_page)
        self.client.post('/admin/login', data={
            'username': 'test_admin',
            'password': 'test-password-only',
            'csrf_token': csrf_token
        }, follow_redirects=True)

        # Attempt CRUD without CSRF token
        resp = self.client.post('/admin/awareness', data={
            'action': 'create',
            'title': 'Test Article',
            'category': 'Test',
            'description': 'Test description'
        }, follow_redirects=True)
        self.assertEqual(resp.status_code, 400)
        print("[PASS] CSRF Protection: Admin CRUD rejects missing CSRF token")

if __name__ == '__main__':
    unittest.main()