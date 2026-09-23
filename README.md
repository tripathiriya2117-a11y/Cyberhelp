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
7. **Secure Admin Panel**: Session-authenticated management interface with password hashing and complete CRUD operations for all database entities.

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
├── .env                       # Environment variables
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

### 3. Initialize & Seed Database (Optional - Happens automatically on startup)
```bash
python seed.py
```
This creates `cyberhelp.db` and populates 8–10 realistic sample entries for every module and the default admin account.

### 4. Run the Application
```bash
python app.py
```
Open your browser and navigate to:
```
http://127.0.0.1:5000
```

---

## 🔑 Default Admin Credentials

- **URL**: `http://127.0.0.1:5000/admin/login`
- **Username**: `admin`
- **Password**: `admin123`

---

## 🤖 Gemini API Key Configuration (Optional)

To enable live Google Gemini AI responses in the Chatbot:
1. Get a free API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Open `.env` and set:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```
3. Or click **"API Key Settings"** directly on the Chatbot page in the web UI.
4. *Note: If no key is set, CyberHelp automatically falls back to its built-in expert cyber safety knowledge base.*
