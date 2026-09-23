import os
import re
import urllib.parse
import uuid
import requests
from functools import wraps
from flask import (
    Flask, render_template, request, redirect, url_for,
    flash, session, jsonify, g
)
from werkzeug.security import check_password_hash, generate_password_hash
from dotenv import load_dotenv
from db import get_db, seed_db

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'cyberhelp-community-safety-secure-secret-key-2026')
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')

# Ensure database is initialized on startup
with app.app_context():
    seed_db()

@app.before_request
def before_request():
    g.db = get_db()

@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db is not None:
        db.close()

# ----------------- Authentication Helper -----------------
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_id' not in session:
            flash('Please log in to access the Admin Panel.', 'warning')
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated_function

# ----------------- Client-Side Public Routes -----------------

@app.route('/')
def index():
    cursor = g.db.cursor()
    # Fetch counts for metrics
    articles_count = cursor.execute("SELECT COUNT(*) as count FROM awareness_content").fetchone()['count']
    scams_count = cursor.execute("SELECT COUNT(*) as count FROM scam_library").fetchone()['count']
    quiz_count = cursor.execute("SELECT COUNT(*) as count FROM quiz_questions").fetchone()['count']
    scores_count = cursor.execute("SELECT COUNT(*) as count FROM quiz_scores").fetchone()['count']
    
    # Recent items
    recent_scams = cursor.execute("SELECT * FROM scam_library ORDER BY scam_id DESC LIMIT 4").fetchall()
    recent_articles = cursor.execute("SELECT * FROM awareness_content ORDER BY content_id DESC LIMIT 4").fetchall()
    
    return render_template(
        'index.html',
        articles_count=articles_count,
        scams_count=scams_count,
        quiz_count=quiz_count,
        scores_count=scores_count,
        recent_scams=recent_scams,
        recent_articles=recent_articles
    )

@app.route('/awareness')
def awareness():
    category = request.args.get('category', '').strip()
    search_query = request.args.get('q', '').strip()
    
    query = "SELECT * FROM awareness_content WHERE 1=1"
    params = []
    
    if category and category.lower() != 'all':
        query += " AND category = ?"
        params.append(category)
        
    if search_query:
        query += " AND (title LIKE ? OR description LIKE ?)"
        params.extend([f'%{search_query}%', f'%{search_query}%'])
        
    query += " ORDER BY content_id ASC"
    
    articles = g.db.execute(query, params).fetchall()
    categories = [row['category'] for row in g.db.execute("SELECT DISTINCT category FROM awareness_content ORDER BY category ASC").fetchall()]
    
    return render_template(
        'awareness.html',
        articles=articles,
        categories=categories,
        selected_category=category,
        search_query=search_query
    )

@app.route('/scams')
def scam_library():
    category = request.args.get('category', '').strip()
    search_query = request.args.get('q', '').strip()
    
    query = "SELECT * FROM scam_library WHERE 1=1"
    params = []
    
    if category and category.lower() != 'all':
        query += " AND category = ?"
        params.append(category)
        
    if search_query:
        query += " AND (title LIKE ? OR description LIKE ?)"
        params.extend([f'%{search_query}%', f'%{search_query}%'])
        
    query += " ORDER BY scam_id ASC"
    
    scams = g.db.execute(query, params).fetchall()
    categories = [row['category'] for row in g.db.execute("SELECT DISTINCT category FROM scam_library ORDER BY category ASC").fetchall()]
    
    return render_template(
        'scam_library.html',
        scams=scams,
        categories=categories,
        selected_category=category,
        search_query=search_query
    )

@app.route('/tools')
def tools():
    return render_template('tools.html')

@app.route('/quiz')
def quiz():
    questions = g.db.execute("SELECT question_id, question_text, option_a, option_b, option_c, option_d, correct_option FROM quiz_questions ORDER BY question_id ASC").fetchall()
    return render_template('quiz.html', questions=questions)

@app.route('/faqs')
def faqs():
    search_query = request.args.get('q', '').strip()
    if search_query:
        faqs_list = g.db.execute(
            "SELECT * FROM faq WHERE question LIKE ? OR answer LIKE ? ORDER BY faq_id ASC",
            (f'%{search_query}%', f'%{search_query}%')
        ).fetchall()
    else:
        faqs_list = g.db.execute("SELECT * FROM faq ORDER BY faq_id ASC").fetchall()
        
    return render_template('faqs.html', faqs=faqs_list, search_query=search_query)

@app.route('/reporting')
def reporting():
    guidance_list = g.db.execute("SELECT * FROM reporting_guidance ORDER BY guidance_id ASC").fetchall()
    return render_template('reporting.html', guidance_list=guidance_list)

@app.route('/chatbot')
def chatbot():
    has_env_key = bool(os.environ.get('GEMINI_API_KEY', '').strip())
    return render_template('chatbot.html', has_env_key=has_env_key)

# ----------------- APIs (Tools, Quiz, Chatbot) -----------------

@app.route('/api/check-url', methods=['POST'])
def api_check_url():
    data = request.get_json(silent=True) or {}
    url = data.get('url', '').strip()
    
    if not url:
        return jsonify({'error': 'Please provide a valid URL to analyze.'}), 400
        
    # Prepend http:// if missing protocol to parse correctly
    test_url = url if re.match(r'^[a-zA-Z]+://', url) else f'http://{url}'
    
    try:
        parsed = urllib.parse.urlparse(test_url)
        hostname = parsed.hostname or ''
    except Exception:
        return jsonify({'error': 'Could not parse URL structure.'}), 400
        
    flags = []
    risk_score = 0 # 0 (Safe) to 100 (High Risk)
    
    # Check 1: IP address as hostname
    ip_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.match(ip_pattern, hostname):
        flags.append({
            'type': 'danger',
            'title': 'Direct IP Address Hostname',
            'detail': 'Legitimate organizations use registered domain names, whereas phishing servers often use raw IP addresses.'
        })
        risk_score += 40
        
    # Check 2: Embedded credentials / @ symbol
    if '@' in url:
        flags.append({
            'type': 'danger',
            'title': 'User Authentication (@) Token in URL',
            'detail': 'Attackers use "@" in URLs to obscure the true destination host.'
        })
        risk_score += 35

    # Check 3: Known URL Shorteners
    shorteners = ['bit.ly', 'tinyurl.com', 'is.gd', 't.co', 'cutt.ly', 'rb.gy', 'ow.ly', 'goo.gl', 'tiny.cc']
    if any(shortener in hostname.lower() for shortener in shorteners):
        flags.append({
            'type': 'warning',
            'title': 'URL Shortener Detected',
            'detail': f'This link is masked using a link shortener ({hostname}). It may conceal a malicious redirect.'
        })
        risk_score += 25

    # Check 4: Excessive Subdomains / Dot Count
    subdomains = hostname.split('.')
    if len(subdomains) > 4:
        flags.append({
            'type': 'warning',
            'title': 'Excessive Subdomain Stacking',
            'detail': f'Domain has {len(subdomains)} hierarchy levels, commonly used to spoof legitimate brand names.'
        })
        risk_score += 20

    # Check 5: Suspicious Brand Mimicking in Subdomains
    high_target_keywords = ['sbi', 'icici', 'hdfc', 'paytm', 'phonepe', 'gpay', 'bank', 'login', 'verify', 'update', 'kyc', 'secure', 'account', 'aadhaar']
    matched_keywords = [kw for kw in high_target_keywords if kw in hostname.lower()]
    
    # Check for excessive hyphens in hostname (e.g., secure-sbi-online)
    if hostname.count('-') >= 2:
        flags.append({
            'type': 'warning',
            'title': 'Multiple Hyphens in Hostname',
            'detail': 'Phishing domains frequently chain hyphens to impersonate official brand names.'
        })
        risk_score += 20

    # If brand keyword is in hostname but NOT the official top-level domain
    suspicious_tlds = ['.xyz', '.top', '.club', '.work', '.click', '.loan', '.tk', '.ml', '.ga', '.cf', '.gq', '.rest', '.bar', '.online']
    has_suspicious_tld = any(hostname.lower().endswith(tld) for tld in suspicious_tlds)
    
    if has_suspicious_tld:
        flags.append({
            'type': 'warning',
            'title': 'High-Risk / Disposable Top-Level Domain',
            'detail': f'The domain ends with a high-abuse TLD ({hostname.split(".")[-1]}).'
        })
        risk_score += 25

    if matched_keywords:
        if has_suspicious_tld:
            flags.append({
                'type': 'danger',
                'title': 'Brand / Security Keywords on Untrusted TLD',
                'detail': f'Found keyword(s) {matched_keywords} hosted on an untrusted TLD.'
            })
            risk_score += 35
        elif len(matched_keywords) >= 2:
            flags.append({
                'type': 'warning',
                'title': 'Multiple Sensitive Security Keywords',
                'detail': f'Domain combines multiple security keywords {matched_keywords}.'
            })
            risk_score += 25

    # Check 6: Suspicious Parameters
    suspicious_params = ['token', 'password', 'pin', 'redirect_uri', 'session', 'card', 'cvv']
    if any(param in parsed.query.lower() for param in suspicious_params):
        flags.append({
            'type': 'warning',
            'title': 'Sensitive Data Parameters in Query String',
            'detail': 'URL contains parameters attempting to pass credentials or session tokens in plain text.'
        })
        risk_score += 20

    # Determine Verdict
    risk_score = min(risk_score, 100)
    if risk_score >= 50:
        verdict = 'HIGH RISK / DANGEROUS'
        badge_class = 'danger'
        recommendation = 'DO NOT open this link or enter personal / financial details.'
    elif risk_score >= 20:
        verdict = 'SUSPICIOUS / PROCEED WITH CAUTION'
        badge_class = 'warning'
        recommendation = 'Exercise caution. Verify the sender and do not input passwords or OTPs.'
    else:
        verdict = 'NO HIGH-RISK HEURISTICS DETECTED'
        badge_class = 'success'
        recommendation = 'No prominent malicious patterns were detected by local heuristic rules. Always ensure SSL encryption is present.'

    return jsonify({
        'url': url,
        'hostname': hostname,
        'risk_score': risk_score,
        'verdict': verdict,
        'badge_class': badge_class,
        'recommendation': recommendation,
        'flags': flags
    })

@app.route('/api/quiz/submit', methods=['POST'])
def api_quiz_submit():
    data = request.get_json(silent=True) or {}
    answers = data.get('answers', {}) # Dict of {question_id: 'A'/'B'/'C'/'D'}
    
    questions = g.db.execute("SELECT question_id, question_text, option_a, option_b, option_c, option_d, correct_option FROM quiz_questions").fetchall()
    
    total = len(questions)
    score = 0
    detailed_results = []
    
    for q in questions:
        qid_str = str(q['question_id'])
        user_choice = answers.get(qid_str, '').upper()
        is_correct = (user_choice == q['correct_option'].upper())
        if is_correct:
            score += 1
            
        detailed_results.append({
            'question_id': q['question_id'],
            'question_text': q['question_text'],
            'user_choice': user_choice,
            'correct_option': q['correct_option'],
            'is_correct': is_correct,
            'options': {
                'A': q['option_a'],
                'B': q['option_b'],
                'C': q['option_c'],
                'D': q['option_d']
            }
        })
        
    # Track score in DB
    session_id = session.get('quiz_session_id')
    if not session_id:
        session_id = str(uuid.uuid4())
        session['quiz_session_id'] = session_id
        
    g.db.execute(
        "INSERT INTO quiz_scores (session_id, score, total_questions) VALUES (?, ?, ?)",
        (session_id, score, total)
    )
    g.db.commit()
    
    percentage = round((score / total) * 100 if total > 0 else 0, 1)
    
    if percentage >= 80:
        evaluation = 'Cyber Guardian! Outstanding awareness of digital threats and best practices.'
        badge = 'success'
    elif percentage >= 50:
        evaluation = 'Good Awareness! Review the topics below to plug critical safety gaps.'
        badge = 'warning'
    else:
        evaluation = 'Vulnerable to Social Engineering. Please study the CyberHelp Awareness guides carefully.'
        badge = 'danger'
        
    return jsonify({
        'score': score,
        'total': total,
        'percentage': percentage,
        'evaluation': evaluation,
        'badge': badge,
        'results': detailed_results
    })

@app.route('/api/chat', methods=['POST'])
def api_chat():
    data = request.get_json(silent=True) or {}
    message = data.get('message', '').strip()
    client_api_key = data.get('apiKey', '').strip()
    
    if not message:
        return jsonify({'error': 'Message cannot be empty.'}), 400
        
    # Use client-supplied key or .env key
    api_key = client_api_key or os.environ.get('GEMINI_API_KEY', '').strip()
    
    # If API key is available, call Gemini API
    if api_key:
        system_instruction = (
            "You are CyberHelp Assistant, a friendly, authoritative, and practical cyber safety expert. "
            "Your mission is to help everyday users (students, senior citizens, small business owners) stay safe online. "
            "Provide concise, actionable advice for cyber threats, phishing, UPI frauds, loan scams, account recovery, "
            "and official Indian reporting procedures (National Helpline 1930 and cybercrime.gov.in). "
            "Format your answers with clear bullet points and bold key action steps."
        )
        
        # Call Gemini REST API (gemini-2.0-flash or gemini-1.5-flash)
        endpoints = [
            f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}",
            f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
        ]
        
        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": f"{system_instruction}\n\nUser Question: {message}"}
                    ]
                }
            ],
            "generationConfig": {
                "temperature": 0.3,
                "maxOutputTokens": 800
            }
        }
        
        for ep in endpoints:
            try:
                resp = requests.post(ep, json=payload, timeout=12)
                if resp.status_code == 200:
                    res_json = resp.json()
                    candidates = res_json.get('candidates', [])
                    if candidates:
                        reply_text = candidates[0].get('content', {}).get('parts', [{}])[0].get('text', '')
                        if reply_text:
                            return jsonify({
                                'reply': reply_text,
                                'source': 'Gemini 2.0 Flash AI'
                            })
                elif resp.status_code == 400 or resp.status_code == 403:
                    # Invalid key or permission error
                    err_msg = resp.json().get('error', {}).get('message', 'Invalid API key')
                    return jsonify({
                        'error': f'Gemini API error: {err_msg}. Check your API key or use the built-in offline advisor.'
                    }), 400
            except Exception as e:
                pass # Try next endpoint or fallback

    # Intelligent Local Fallback Response Engine
    msg_lower = message.lower()
    fallback_reply = get_contextual_fallback_response(msg_lower)
    
    return jsonify({
        'reply': fallback_reply,
        'source': 'CyberHelp Knowledge Base (Offline Engine)'
    })

def get_contextual_fallback_response(query):
    """
    Intelligent offline rule-based response engine when no Gemini API key is configured.
    """
    if any(w in query for w in ['1930', 'helpline', 'freeze', 'call police', 'emergency', 'lost money', 'scammed']):
        return (
            "🚨 **Immediate Financial Fraud Action (Golden Hour):**\n\n"
            "1. **Call 1930 Immediately**: Dial India's National Cyber Financial Fraud helpline (1930). Report within 1–2 hours to trigger automated holds on suspect bank accounts.\n"
            "2. **Have Info Ready**: Keep your Bank Name, Account Number, UTR/Transaction Reference ID, and Suspect UPI/Account ID ready.\n"
            "3. **File on Portal**: Submit a formal complaint at [cybercrime.gov.in](https://cybercrime.gov.in).\n"
            "4. **Freeze Cards/Net Banking**: Call your bank's 24/7 card blocking number or toggle 'Card Lock' in your mobile banking app."
        )
    elif any(w in query for w in ['upi', 'qr', 'pin', 'phonepe', 'gpay', 'paytm']):
        return (
            "🛡️ **UPI Safety Rules:**\n\n"
            "- **Golden Rule**: You NEVER enter your UPI PIN or scan a QR code to *receive* money. Entering your PIN always *deducts* funds.\n"
            "- **Decline Collect Requests**: If a buyer on OLX/Marketplace sends a 'Payment Request', reject it immediately.\n"
            "- **Do Not Share OTPs**: Never read out verification OTPs over phone or chat."
        )
    elif any(w in query for w in ['loan', 'loan app', 'blackmail', 'photos', 'morphed', 'recovery']):
        return (
            "⚠️ **Dealing with Illegal Loan Apps & Harassment:**\n\n"
            "1. **Stop Paying**: Paying extortion money leads to further demands. Block recovery agent numbers immediately.\n"
            "2. **Gather Evidence**: Save screenshots of abusive WhatsApp messages, morphed photos, and payment slips.\n"
            "3. **Report to RBI Sachet**: File a complaint on [sachet.rbi.org.in](https://sachet.rbi.org.in).\n"
            "4. **Lodge Cyber FIR**: Register an FIR at [cybercrime.gov.in](https://cybercrime.gov.in) under IT Act Section 66E (privacy violation).\n"
            "5. **Notify Contacts**: Broadcast a short message to your contacts stating that your device permissions were compromised by a rogue app."
        )
    elif any(w in query for w in ['job', 'telegram', 'task', 'youtube like', 'review']):
        return (
            "🛑 **Part-Time Task / Telegram Job Scam Warning:**\n\n"
            "- **Pattern**: Scammers pay ₹150–₹500 for liking videos or rating hotels, then demand ₹10,000–₹5,00,000 to 'unlock VIP task profits'.\n"
            "- **Action**: Stop depositing money immediately. Any job that asks you to pay to work is a 100% scam.\n"
            "- **Report**: File a complaint at 1930 and [cybercrime.gov.in](https://cybercrime.gov.in)."
        )
    elif any(w in query for w in ['whatsapp', 'hack', 'instagram', 'facebook', 'cloned', 'account']):
        return (
            "🔐 **Compromised Account Recovery:**\n\n"
            "- **WhatsApp**: Re-install WhatsApp, input your phone number, and verify with SMS OTP. This logs out the hacker. Enable Two-Step Verification (PIN).\n"
            "- **Instagram/Facebook**: Visit [instagram.com/hacked](https://instagram.com/hacked) or facebook.com/hacked, revoke unauthorized login sessions, and change your password.\n"
            "- **Warn Friends**: Post a status asking friends to ignore any money requests sent from your profile."
        )
    elif any(w in query for w in ['aadhaar', 'aeps', 'biometric', 'fingerprint']):
        return (
            "🔒 **Locking Aadhaar Biometrics:**\n\n"
            "1. Visit [myaadhaar.uidai.gov.in](https://myaadhaar.uidai.gov.in) or open the **mAadhaar app**.\n"
            "2. Log in with your Aadhaar number and OTP.\n"
            "3. Select **'Lock/Unlock Biometrics'** and switch the lock ON.\n"
            "4. This blocks unauthorized fingerprint AePS withdrawals. You can unlock it temporarily for 10 minutes whenever you visit a bank or KYC center."
        )
    else:
        return (
            "🤖 **CyberHelp Safety Tips:**\n\n"
            "1. **Never Share OTPs/PINs**: No bank or official agency asks for passwords or UPI PINs.\n"
            "2. **Verify Emergency Calls**: If a caller claims to be police, customs, or power board, hang up and call the official organization directly.\n"
            "3. **Helpline 1930**: For any cyber financial fraud, report immediately to 1930 or visit [cybercrime.gov.in](https://cybercrime.gov.in).\n"
            "4. *Tip: You can add a free Gemini API key in the API Key settings modal to enable full generative AI answers!*"
        )

# ----------------- Module 2: Admin Panel & CRUD -----------------

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if 'admin_id' in session:
        return redirect(url_for('admin_dashboard'))
        
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        
        admin = g.db.execute("SELECT * FROM admin WHERE username = ?", (username,)).fetchone()
        
        if admin and check_password_hash(admin['password_hash'], password):
            session['admin_id'] = admin['admin_id']
            session['admin_username'] = admin['username']
            flash(f'Welcome back, {admin["username"]}! Logged in successfully.', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid username or password. Default is admin / admin123.', 'danger')
            
    return render_template('admin/login.html')

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_id', None)
    session.pop('admin_username', None)
    flash('You have been logged out securely.', 'info')
    return redirect(url_for('admin_login'))

@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    cursor = g.db.cursor()
    stats = {
        'awareness_count': cursor.execute("SELECT COUNT(*) FROM awareness_content").fetchone()[0],
        'scams_count': cursor.execute("SELECT COUNT(*) FROM scam_library").fetchone()[0],
        'quiz_count': cursor.execute("SELECT COUNT(*) FROM quiz_questions").fetchone()[0],
        'faq_count': cursor.execute("SELECT COUNT(*) FROM faq").fetchone()[0],
        'guidance_count': cursor.execute("SELECT COUNT(*) FROM reporting_guidance").fetchone()[0],
        'quiz_attempts': cursor.execute("SELECT COUNT(*) FROM quiz_scores").fetchone()[0]
    }
    recent_attempts = cursor.execute("SELECT * FROM quiz_scores ORDER BY score_id DESC LIMIT 5").fetchall()
    return render_template('admin/dashboard.html', stats=stats, recent_attempts=recent_attempts)

# --- Admin CRUD: Awareness Content ---
@app.route('/admin/awareness', methods=['GET', 'POST'])
@login_required
def admin_awareness():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'create':
            title = request.form.get('title', '').strip()
            category = request.form.get('category', '').strip()
            description = request.form.get('description', '').strip()
            if title and category and description:
                g.db.execute(
                    "INSERT INTO awareness_content (title, category, description, admin_id) VALUES (?, ?, ?, ?)",
                    (title, category, description, session['admin_id'])
                )
                g.db.commit()
                flash('Awareness article published successfully!', 'success')
            else:
                flash('All fields are required.', 'danger')
                
        elif action == 'edit':
            content_id = request.form.get('content_id')
            title = request.form.get('title', '').strip()
            category = request.form.get('category', '').strip()
            description = request.form.get('description', '').strip()
            if content_id and title and category and description:
                g.db.execute(
                    "UPDATE awareness_content SET title = ?, category = ?, description = ? WHERE content_id = ?",
                    (title, category, description, content_id)
                )
                g.db.commit()
                flash('Article updated successfully!', 'success')
                
        elif action == 'delete':
            content_id = request.form.get('content_id')
            if content_id:
                g.db.execute("DELETE FROM awareness_content WHERE content_id = ?", (content_id,))
                g.db.commit()
                flash('Article deleted.', 'info')
                
        return redirect(url_for('admin_awareness'))
        
    articles = g.db.execute("SELECT * FROM awareness_content ORDER BY content_id DESC").fetchall()
    return render_template('admin/awareness_crud.html', articles=articles)

# --- Admin CRUD: Scam Library ---
@app.route('/admin/scams', methods=['GET', 'POST'])
@login_required
def admin_scams():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'create':
            title = request.form.get('title', '').strip()
            category = request.form.get('category', '').strip()
            description = request.form.get('description', '').strip()
            if title and category and description:
                g.db.execute(
                    "INSERT INTO scam_library (title, category, description, admin_id) VALUES (?, ?, ?, ?)",
                    (title, category, description, session['admin_id'])
                )
                g.db.commit()
                flash('New scam pattern entry logged!', 'success')
            else:
                flash('All fields are required.', 'danger')
                
        elif action == 'edit':
            scam_id = request.form.get('scam_id')
            title = request.form.get('title', '').strip()
            category = request.form.get('category', '').strip()
            description = request.form.get('description', '').strip()
            if scam_id and title and category and description:
                g.db.execute(
                    "UPDATE scam_library SET title = ?, category = ?, description = ? WHERE scam_id = ?",
                    (title, category, description, scam_id)
                )
                g.db.commit()
                flash('Scam pattern updated.', 'success')
                
        elif action == 'delete':
            scam_id = request.form.get('scam_id')
            if scam_id:
                g.db.execute("DELETE FROM scam_library WHERE scam_id = ?", (scam_id,))
                g.db.commit()
                flash('Scam pattern deleted.', 'info')
                
        return redirect(url_for('admin_scams'))
        
    scams = g.db.execute("SELECT * FROM scam_library ORDER BY scam_id DESC").fetchall()
    return render_template('admin/scams_crud.html', scams=scams)

# --- Admin CRUD: Quiz Questions ---
@app.route('/admin/quiz', methods=['GET', 'POST'])
@login_required
def admin_quiz():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'create':
            q_text = request.form.get('question_text', '').strip()
            opt_a = request.form.get('option_a', '').strip()
            opt_b = request.form.get('option_b', '').strip()
            opt_c = request.form.get('option_c', '').strip()
            opt_d = request.form.get('option_d', '').strip()
            correct = request.form.get('correct_option', '').strip().upper()
            
            if q_text and opt_a and opt_b and opt_c and opt_d and correct in ['A', 'B', 'C', 'D']:
                g.db.execute(
                    "INSERT INTO quiz_questions (question_text, option_a, option_b, option_c, option_d, correct_option, admin_id) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (q_text, opt_a, opt_b, opt_c, opt_d, correct, session['admin_id'])
                )
                g.db.commit()
                flash('Quiz question created!', 'success')
            else:
                flash('All question fields and valid correct option (A, B, C, D) are required.', 'danger')
                
        elif action == 'edit':
            qid = request.form.get('question_id')
            q_text = request.form.get('question_text', '').strip()
            opt_a = request.form.get('option_a', '').strip()
            opt_b = request.form.get('option_b', '').strip()
            opt_c = request.form.get('option_c', '').strip()
            opt_d = request.form.get('option_d', '').strip()
            correct = request.form.get('correct_option', '').strip().upper()
            
            if qid and q_text and opt_a and opt_b and opt_c and opt_d and correct in ['A', 'B', 'C', 'D']:
                g.db.execute(
                    "UPDATE quiz_questions SET question_text = ?, option_a = ?, option_b = ?, option_c = ?, option_d = ?, correct_option = ? WHERE question_id = ?",
                    (q_text, opt_a, opt_b, opt_c, opt_d, correct, qid)
                )
                g.db.commit()
                flash('Quiz question updated.', 'success')
                
        elif action == 'delete':
            qid = request.form.get('question_id')
            if qid:
                g.db.execute("DELETE FROM quiz_questions WHERE question_id = ?", (qid,))
                g.db.commit()
                flash('Quiz question removed.', 'info')
                
        return redirect(url_for('admin_quiz'))
        
    questions = g.db.execute("SELECT * FROM quiz_questions ORDER BY question_id ASC").fetchall()
    return render_template('admin/quiz_crud.html', questions=questions)

# --- Admin CRUD: FAQs ---
@app.route('/admin/faqs', methods=['GET', 'POST'])
@login_required
def admin_faqs():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'create':
            question = request.form.get('question', '').strip()
            answer = request.form.get('answer', '').strip()
            if question and answer:
                g.db.execute(
                    "INSERT INTO faq (question, answer, admin_id) VALUES (?, ?, ?)",
                    (question, answer, session['admin_id'])
                )
                g.db.commit()
                flash('FAQ added successfully!', 'success')
                
        elif action == 'edit':
            faq_id = request.form.get('faq_id')
            question = request.form.get('question', '').strip()
            answer = request.form.get('answer', '').strip()
            if faq_id and question and answer:
                g.db.execute("UPDATE faq SET question = ?, answer = ? WHERE faq_id = ?", (question, answer, faq_id))
                g.db.commit()
                flash('FAQ updated.', 'success')
                
        elif action == 'delete':
            faq_id = request.form.get('faq_id')
            if faq_id:
                g.db.execute("DELETE FROM faq WHERE faq_id = ?", (faq_id,))
                g.db.commit()
                flash('FAQ deleted.', 'info')
                
        return redirect(url_for('admin_faqs'))
        
    faqs = g.db.execute("SELECT * FROM faq ORDER BY faq_id ASC").fetchall()
    return render_template('admin/faq_crud.html', faqs=faqs)

# --- Admin CRUD: Reporting Guidance ---
@app.route('/admin/reporting', methods=['GET', 'POST'])
@login_required
def admin_reporting():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'create':
            title = request.form.get('title', '').strip()
            steps = request.form.get('steps', '').strip()
            official_link = request.form.get('official_link', '').strip()
            if title and steps:
                g.db.execute(
                    "INSERT INTO reporting_guidance (title, steps, official_link, admin_id) VALUES (?, ?, ?, ?)",
                    (title, steps, official_link, session['admin_id'])
                )
                g.db.commit()
                flash('Reporting guide added!', 'success')
                
        elif action == 'edit':
            guidance_id = request.form.get('guidance_id')
            title = request.form.get('title', '').strip()
            steps = request.form.get('steps', '').strip()
            official_link = request.form.get('official_link', '').strip()
            if guidance_id and title and steps:
                g.db.execute(
                    "UPDATE reporting_guidance SET title = ?, steps = ?, official_link = ? WHERE guidance_id = ?",
                    (title, steps, official_link, guidance_id)
                )
                g.db.commit()
                flash('Reporting guide updated.', 'success')
                
        elif action == 'delete':
            guidance_id = request.form.get('guidance_id')
            if guidance_id:
                g.db.execute("DELETE FROM reporting_guidance WHERE guidance_id = ?", (guidance_id,))
                g.db.commit()
                flash('Reporting guide deleted.', 'info')
                
        return redirect(url_for('admin_reporting'))
        
    guides = g.db.execute("SELECT * FROM reporting_guidance ORDER BY guidance_id ASC").fetchall()
    return render_template('admin/reporting_crud.html', guides=guides)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting CyberHelp Helpdesk on http://127.0.0.1:{port}")
    app.run(host='0.0.0.0', port=port, debug=True)
