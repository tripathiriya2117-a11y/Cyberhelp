# CyberHelp - Community Cyber Safety Helpdesk

A web-based Community Cyber Safety Helpdesk built with **Python (Flask)** and **SQLite** designed to build digital safety awareness and assist non-technical users (students, senior citizens, small business owners). 

This version replaces PHP & MySQL/XAMPP with a standalone, zero-setup Python environment.

---

## 🌟 Key Features & Modules

1. **Awareness Hub**: Categorized guides on Phishing, OTP Frauds, QR Code traps, SIM Swap attacks, Identity Theft, and emerging AI deepfake voice scams.
2. **Scam Information Library**: Searchable database of real-world scam patterns (Part-time Telegram tasks, Fake loan apps, Electricity bill threats, Courier drug parcel scams, and more).
3. **Safety Validation Tools**:
   - **Password Strength & Entropy Analyzer**: Client-side Shannon entropy calculation ($E = L \times \log_2 R$), brute-force crack time estimator, dictionary pattern detection, and character diversity checklist.
   - **URL Safety & Phishing Scanner**: Dual client/server heuristic link scanner checking for direct IP hosts, suspicious TLDs (`.xyz`, `.top`), shortened URLs (`bit.ly`, etc.), embedded `@` credentials, and spoofed subdomains.
4. **Interactive Safety Quiz**: Database-driven multiple-choice quiz with immediate score calculations, performance evaluation, and question-by-question breakdown.
5. **Cybercrime Reporting Guide**: Official Indian reporting procedures highlighting the **National Cyber Financial Fraud Helpline 1930 ("Golden Hour")**, **cybercrime.gov.in**, **RBI Sachet**, and **DoT Chakshu**.
6. **Gemini AI Safety Assistant**: Conversational assistant powered by Google Gemini API with fallback to built-in offline safety rules.
7. **Secure Admin Panel**: Session-authenticated management interface with password hashing, CSRF protection, rate-limited login, and complete CRUD operations for all database entities.

---

## 📁 Directory Structure

```
cyberhelp/
├── app.py                     # Main Flask application with routes & APIs
├── db.py                      # SQLite connection helper & auto-seeder
├── schema.sql                 # Pure SQLite database schema
├── seed.sql                   # 5-10 rich sample seed entries per module
├── seed.py                    # Standalone seed executor
├── requirements.txt           # Python package dependencies
├── .env                       # Environment variables (NOT committed to git)
├── .env.example               # Example environment variables
├── README.md                  # Project documentation & run guide
├── static/
│   ├── css/
│   │   └── style.css          # Custom styling & responsive design
│   └── js/
│       ├── main.js            # General UI interactions & quiz engine
│       ├── password_tool.js   # Client-side entropy & password analyzer
│       ├── url_checker.js     # URL safety & heuristic scanner
│       └── chatbot.js         # Gemini API & offline chatbot UI
└── templates/
    ├── base.html              # Layout template with navbar, footer & 1930 banner
    ├── index.html             # Homepage with metrics & emergency banner
    ├── awareness.html         # Awareness Hub with filters & live search
    ├── scam_library.html      # Searchable Scam Library
    ├── tools.html             # Safety Tools (Password & URL scanners)
    ├── quiz.html              # Interactive Safety Quiz
    ├── faqs.html              # Searchable FAQ accordion
    ├── reporting.html         # Cybercrime Reporting Guidance
    ├── chatbot.html           # Dedicated AI Chatbot page
    └── admin/
        ├── login.html         # Admin login
        ├── dashboard.html     # Admin dashboard & quiz attempts tracker
        ├── awareness_crud.html# CRUD for awareness articles
        ├── scams_crud.html    # CRUD for scam patterns
        ├── quiz_crud.html     # CRUD for quiz questions
        ├── faq_crud.html      # CRUD for FAQs
        └── reporting_crud.html# CRUD for reporting guidance
```

---

## 🚀 Getting Started

### 1. Requirements
- Python 3.8+ installed on your machine.
- No XAMPP, Apache, or MySQL required!

### 2. Install Dependencies
In your terminal / command prompt:
```bash
cd cyberhelp
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Copy `.env.example` to `.env` and set the required values:
```bash
cp .env.example .env
```

**Required variables:**
- `SECRET_KEY` - A secure random string (generate with: `python -c "import secrets; print(secrets.token_hex(32))"`)
- `ADMIN_PASSWORD` - Secure password for the admin account
- `ADMIN_USERNAME` - Admin username (default: admin)

**Optional variables:**
- `GEMINI_API_KEY` - Google Gemini API key for AI chatbot (get from https://aistudio.google.com/app/apikey)
- `PORT` - Server port (default: 5000)
- `FLASK_DEBUG` - Set to "1" to enable debug mode (default: 0)
- `FLASK_ENV` - Set to "production" for production deployment

### 4. Initialize & Seed Database (Optional - Happens automatically on startup)
```bash
python seed.py
```
This creates `cyberhelp.db` and populates 8–10 realistic sample entries for every module and creates the admin account using your configured credentials.

### 5. Run the Application
```bash
python app.py
```
Open your browser and navigate to:
```
http://127.0.0.1:5000
```

---

## 🔐 Admin Access

- **URL**: `http://127.0.0.1:5000/admin/login`
- **Username**: Value of `ADMIN_USERNAME` environment variable (default: `admin`)
- **Password**: Value of `ADMIN_PASSWORD` environment variable (**must be set in .env**)

> **Security Note**: The admin password is no longer hardcoded. You must configure `ADMIN_PASSWORD` in your `.env` file before first run. The application will fail to start if required security configuration is missing.

---

## 🤖 Gemini API Key Configuration (Optional)

To enable live Google Gemini AI responses in the Chatbot:
1. Get a free API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Open `.env` and set:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```
3. *Note: If no key is set, CyberHelp automatically falls back to its built-in expert cyber safety knowledge base.*

---

## 🔒 Security Features

- **No hardcoded secrets** - All secrets loaded from environment variables
- **CSRF Protection** - All state-changing forms protected with Flask-WTF CSRF tokens
- **Rate Limited Login** - Admin login limited to 5 attempts per minute per IP
- **Secure Session Cookies** - HttpOnly, SameSite=Lax, Secure (in production)
- **Security Headers** - X-Content-Type-Options, X-Frame-Options, Referrer-Policy, Content-Security-Policy
- **SQL Injection Prevention** - All queries use parameterized statements
- **XSS Prevention** - Jinja2 autoescaping enabled, no `|safe` filters on user content
- **Debug Mode Disabled by Default** - Controlled via `FLASK_DEBUG` environment variable

---

## ⚠️ Important Disclaimers

**URL Safety Scanner**: The URL analyzer uses heuristic-based checks and does **not** guarantee that a URL is safe or malicious. It is an educational aid, not a substitute for professional security tools or threat intelligence feeds.

**No Absolute Security Guarantees**: This application is an educational platform for cybersecurity awareness. While security best practices have been implemented, no software can provide absolute security. Users should follow official reporting procedures (Helpline 1930, cybercrime.gov.in) for actual incidents.
