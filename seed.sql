-- Seed Data for CyberHelp SQLite Database
-- Contains 8-10 rich, realistic sample entries for each module

-- 1. Default Admin (Password: admin123)
-- Hash generated using pbkdf2:sha256:600000
INSERT INTO admin (admin_id, username, password_hash) 
VALUES (1, 'admin', 'scrypt:32768:8:1$k1jN8bV9xL0qP2wZ$39b1a50c8227b686256f1f31f9b33a59828e8334dd1b8a5356e9c991a0fa25e626e256b826eb3907c088be3381a1faae1d87e0766e4a2dcb72ee91b9b18ba047')
ON CONFLICT(username) DO NOTHING;

-- 2. Awareness Articles (10 Entries)
INSERT INTO awareness_content (content_id, title, category, description, admin_id) VALUES
(1, 'Understanding Phishing, Spear Phishing & Smishing', 'Phishing', 'Phishing is a deceptive technique where attackers disguise themselves as reputable organizations (banks, tax departments, tech support) via email, SMS (smishing), or phone calls (vishing) to steal sensitive credentials such as passwords, OTPs, and credit card numbers. 
Always inspect sender email addresses for subtle misspellings (e.g., support@paypa1.com instead of paypal.com). Never click links in unsolicited emails asking for account verification or password resets.', 1),

(2, 'The Danger of OTP & PIN Sharing Scams', 'OTP Fraud', 'One-Time Passwords (OTPs) and UPI PINs are confidential keys to your financial accounts. Banks, payment gateways, and government agencies will NEVER ask you for your OTP, MPIN, or UPI PIN. 
Scammers often pose as bank executives claiming your KYC is expiring, your account is suspended, or a reward is waiting. Remember: You only enter your UPI PIN to SEND money, never to RECEIVE money.', 1),

(3, 'QR Code Scams: You Never Scan to Receive Money', 'QR Scams', 'A rampant online marketplace fraud involves scammers posing as interested buyers on OLX, Facebook Marketplace, or Quikr. The scammer sends a QR code claiming: "Scan this code on PhonePe/GPay to receive the payment into your account."
CRITICAL RULE: Scanning a QR code and entering your UPI PIN authorizes a DEBIT transaction. Receiving money via UPI requires zero action, zero QR scans, and zero PIN entry on your phone.', 1),

(4, 'SIM Swap Fraud & Signal Hijacking', 'Identity Theft', 'In a SIM swap attack, fraudsters use forged identification documents or social engineering with telecom providers to port your mobile number to a SIM card in their possession. Once activated, the attacker intercepts all your SMS OTPs, password reset links, and bank alerts.
Warning signs include sudden, unexplained loss of cellular signal and "No Service" status. If your phone loses connectivity unexpectedly, contact your telecom carrier immediately from an alternate phone.', 1),

(5, 'Securing Identity & Locking Aadhaar Biometrics', 'Identity Theft', 'Aadhaar-enabled Payment Systems (AePS) allow financial transactions using fingerprint biometrics. Cybercriminals have exploited leaked land registry documents containing fingerprint images to withdraw funds without OTP.
Protect yourself by using the official mAadhaar app or UIDAI resident portal (myaadhaar.uidai.gov.in) to lock your biometrics. You can unlock them temporarily in seconds whenever you need KYC authentication.', 1),

(6, 'Social Media Impersonation & Account Hijacking', 'Social Media', 'Attackers clone public profiles (name, profile picture, bio) on Instagram, Facebook, or WhatsApp and message friends/family claiming an urgent medical emergency or travel crisis requiring immediate funds via UPI.
Always protect your accounts with Two-Factor Authentication (2FA) using an Authenticator app (such as Google Authenticator) rather than SMS. Set your friends lists and personal details to private.', 1),

(7, 'Risks of Public Wi-Fi & "Evil Twin" Hotspots', 'Device Security', 'Free public Wi-Fi networks in airports, cafes, and hotels are often unencrypted, allowing attackers on the same network to snoop on unencrypted traffic. Criminals can also set up rogue hotspots (e.g., "Airport_Free_WiFi_Official") to intercept login sessions and credentials.
Avoid accessing bank accounts or sensitive work portals on public Wi-Fi. Always use a reputable Virtual Private Network (VPN) and ensure the browser URL displays "https://" with a valid padlock icon.', 1),

(8, 'AI Voice Cloning & Deepfake Emergency Scams', 'Emerging Threats', 'Using just 3 to 10 seconds of audio scraped from social media videos, generative AI tools can clone a loved one''s exact voice, cadence, and tone. Scammers call parents or grandparents pretending to be their child in police custody, injured in an accident, or kidnapped, begging for immediate ransom.
Always establish a secret "Family Safe Word" to verify distress calls, and independently hang up and dial your family member''s real phone number directly before transferring any money.', 1),

(9, 'Fake Antivirus & Browser Notification Malware', 'Device Security', 'Malicious websites trigger alarming full-screen popups claiming "Your PC is infected with 5 viruses! Call Microsoft Support immediately." Calling the number connects you to a boiler-room call center that tricks you into granting remote access and charging exorbitant fees.
Close the browser tab using Task Manager (Ctrl + Shift + Esc). Never call toll-free numbers from unexpected web popups, and never grant remote access software permissions to unknown callers.', 1),

(10, 'Digital Arrest & Law Enforcement Video Call Extortion', 'Emerging Threats', 'Scammers pose as CBI, Mumbai Police, ED, or Customs officers on Skype/WhatsApp video calls wearing fake uniforms and backgrounds. They claim a parcel with narcotics or forged passports in your name was seized, or your Aadhaar was linked to money laundering.
They place victims under a fake "Digital Arrest", forbidding them from disconnecting while coercing them to transfer funds into "RBI verification escrow accounts". Fact: Indian law enforcement NEVER conducts judicial hearings, arrests, or financial verification over Skype or video calls.', 1);

-- 3. Scam Library (10 Entries)
INSERT INTO scam_library (scam_id, title, category, description, admin_id) VALUES
(1, 'Part-Time Telegram & YouTube Like Task Scam', 'Job Offers', 'Modus Operandi: Victims receive WhatsApp messages offering Rs 150-500 per task for liking YouTube videos, writing Google Reviews, or rating hotels. After earning Rs 1,000 in early payouts to build trust, the victim is invited to a Telegram VIP group and lured into investing Rs 50,000 to Rs 10 Lakhs in fake crypto/merchant prepaid task portals.
Red Flags: Easy work with sky-high payouts, payment via Telegram channels, requirement to deposit money to "unlock" your earnings.
Prevention: Legitimate companies never charge money or require prepaid tasks for employment.', 1),

(2, 'Instant Fake Loan Apps & Extortion Racket', 'Loan Apps', 'Modus Operandi: Fraudulent loan apps advertised on social media promise instant disbursals of Rs 5,000-50,000 with zero documentation. Upon installation, the app harvests the user''s entire contact list, gallery photos, and device permissions.
The victim receives a small fraction of the loan after heavy deduction, and within days, loan recovery agents morph victim photos into obscene images and threaten to circulate them to all family and professional contacts.
Prevention: Only borrow from RBI-registered NBFCs and banks. Never grant Contact/Gallery permissions to loan utility apps.', 1),

(3, 'Electricity Bill Disconnection SMS Threat', 'Utility Threats', 'Modus Operandi: Bulk SMS sent in regional languages stating: "Dear Consumer, your electricity power will be disconnected tonight at 9:30 PM because your previous month bill was not updated. Immediately call Electricity Officer at 98xxxxxx."
When the anxious victim calls, they are instructed to download a remote support app (AnyDesk/QuickSupport) or pay a nominal Rs 10 recharge on a spoofed portal, which steals bank credentials and wipes the account.
Prevention: State power distribution boards never send SMS from 10-digit personal mobile numbers and do not direct payments to individual numbers.', 1),

(4, 'Courier Parcel Drug & Customs Impersonation', 'Courier / Police Impersonation', 'Modus Operandi: Victim receives an automated call claiming to be from FedEx, DHL, or Blue Dart: "A parcel containing 5 fake passports, 150g MDMA drugs, and banned credit cards sent from Mumbai to Taiwan in your name has been intercepted."
The call is transferred to a fake "Cyber Crime Narcotics Officer" who shows fake police IDs, issues fake arrest warrants, and demands the victim liquidate fixed deposits and transfer money to "clear their name with the Reserve Bank of India".
Prevention: Legitimate customs and police agencies register formal FIRs and summon individuals in person; they never demand fund transfers to personal bank accounts.', 1),

(5, 'WhatsApp KBC Lottery & Lucky Winner Scam', 'Lottery', 'Modus Operandi: Victims receive an audio clip and forged certificate with Amitabh Bachchan and Prime Minister photos claiming they won Rs 25 Lakhs in the "KBC WhatsApp All India Sim Card Lucky Draw".
To claim the prize, the victim is asked to pay "tax clearance fees", "file processing charges", and "GST duty" into various individual mule accounts.
Prevention: WhatsApp does not run lotteries. Neither KBC nor telecom operators conduct lucky draws based on random SIM card numbers.', 1),

(6, 'Remote Access Desktop Sharing Fraud (AnyDesk / TeamViewer)', 'Tech Support', 'Modus Operandi: Scammers pose as customer care representatives from banks, e-commerce portals (Amazon, Flipkart), or wallet providers (Paytm, PhonePe) helping you process a refund or KYC update.
They direct you to install AnyDesk, TeamViewer, or RustDesk from Google Play Store and ask for the 9-digit session code. Once shared, they view your screen in real time, watch you enter passwords/OTPs, or take control to transfer funds.
Prevention: Never share remote screen access codes with anyone. Remote access apps give 100% control of your device.', 1),

(7, 'Fake Customer Care Search Engine Poisoning', 'Search Engine Spoofing', 'Modus Operandi: Cybercriminals create fake websites and edit Google Business listings for airlines, banks, courier hubs, wine shops, and delivery services with their personal fraud mobile numbers.
When customers search Google for "XYZ Bank Customer Care Number" and call the top listing, the fraudster pretends to be an official agent and sends malicious APK files or UPI payment request links to "resolve the issue".
Prevention: Always look up customer service contact details inside the verified official mobile banking app or on the official domain URL printed on the back of your debit card.', 1),

(8, 'Matrimonial & International Romance Gift Scam', 'Romance & Matrimonial', 'Modus Operandi: Scammer creates an attractive profile on matrimony apps or Instagram posing as an NRI doctor, engineer, or pilot based in the UK/USA. After weeks of building emotional intimacy and promising marriage, they announce they have sent expensive gifts (jewelry, iPhone, designer watches, foreign currency).
A few days later, a fake "Customs Official at Delhi Airport" calls the victim demanding customs clearance fee, anti-money laundering penalty, and courier charges running into lakhs.
Prevention: Never transfer money to someone you have never met in person, regardless of promises made.', 1),

(9, 'Fake Work-From-Home Amazon Order Review Tasks', 'Job Offers', 'Modus Operandi: Fraudsters pose as e-commerce recruitment agencies on WhatsApp/LinkedIn offering daily wages for "optimizing merchant product rankings" or "boosting crypto trade volume".
Users are asked to complete consecutive sets of 30 orders. In the middle of the set, a "combo order with negative balance" triggers, forcing the victim to deposit progressively larger sums (Rs 10,000, Rs 50,000, Rs 2,00,000) to withdraw their principal.
Prevention: No legitimate e-commerce platform requires users to top up personal funds to perform product testing or order reviews.', 1),

(10, 'High-Return Forex & Crypto Trading Pig Butchering', 'Investment Fraud', 'Modus Operandi: Scammers connect via dating apps or WhatsApp "wrong numbers" and slowly brag about their wealth generated through specialized algorithmic crypto or forex trading.
They introduce the victim to a fraudulent trading platform (manipulated web portal showing massive fabricated profits). When the victim attempts to withdraw their money, the platform demands a 20% capital gains tax deposit, freezing all assets when payment is refused.
Prevention: Only trade on SEBI or FIU-registered domestic exchanges. Unrealistic returns (e.g. 5% daily guarantee) are 100% fraudulent.', 1);

-- 4. Quiz Questions (10 Questions with 4 options & correct answer)
INSERT INTO quiz_questions (question_id, question_text, option_a, option_b, option_c, option_d, correct_option, admin_id) VALUES
(1, 'You receive an urgent SMS claiming your bank account will be deactivated within 2 hours unless you click a bit.ly link to complete KYC. What is the safest course of action?',
'Click the link immediately to prevent account suspension',
'Forward the link to family members so they can check their accounts too',
'Ignore the link, delete the SMS, and verify with your bank using their official app or branch number',
'Reply to the SMS with your bank account number and Aadhaar number',
'C', 1),

(2, 'A buyer on OLX sends you a PhonePe QR code saying "Scan this and enter your UPI PIN to receive the Rs 5,000 payment". What will happen if you scan and enter your PIN?',
'You will receive Rs 5,000 in your bank account',
'Rs 5,000 will be deducted from YOUR bank account',
'The QR code will simply verify your account name without money movement',
'The transaction will be held in safe escrow until delivery',
'B', 1),

(3, 'What is the primary security advantage of Two-Factor Authentication (2FA)?',
'It makes web pages load twice as fast',
'It requires an additional verification step (like an authenticator code) even if your password is stolen',
'It eliminates the need for strong passwords',
'It allows multiple people to share the same account simultaneously',
'B', 1),

(4, 'A technical support caller claims your computer has a critical virus and asks you to install AnyDesk or TeamViewer QuickSupport. What should you do?',
'Install it immediately to prevent data corruption',
'Refuse and hang up, because these apps give the caller full remote control of your screen and device',
'Install the app, but only read out the 9-digit code if they show a company ID card',
'Install it and leave the computer unattended while they fix it',
'B', 1),

(5, 'What is the official Indian National Emergency Helpline number for reporting cyber financial fraud immediately to freeze stolen funds?',
'100',
'108',
'1930',
'1091',
'C', 1),

(6, 'Which of the following passwords has the highest security strength against automated brute-force attacks?',
'Password123!',
'Rohan@2023',
'correct-horse-battery-staple-9#Solar',
'1234567890Aa',
'C', 1),

(7, 'You receive a WhatsApp video call from a person in a police uniform claiming an illegal drug parcel was seized in your name and you are under "Digital Arrest". What is the reality?',
'You are legally obligated to stay on video call and transfer verification funds',
'Indian law enforcement agencies do not conduct arrests or trial procedures over WhatsApp/Skype video calls',
'You should immediately transfer your savings to the "RBI security account" they provide',
'You must keep it confidential and not inform your family',
'B', 1),

(8, 'Which of the following URL structures indicates a high likelihood of a phishing website attempting to mimic State Bank of India?',
'https://www.onlinesbi.sbi/portal/login.html',
'https://retail.onlinesbi.sbi/',
'http://onlinesbi.secure-login-verification.xyz/sbi/auth',
'https://www.sbi.co.in',
'C', 1),

(9, 'What is "Juice Jacking"?',
'A scam where fraudsters steal fruit juice delivery orders',
'A cyber attack where malware is loaded or data is copied from a device via a public USB charging port',
'Overcharging mobile phone batteries to cause physical damage',
'A technique to bypass SIM lock PINs using NFC',
'B', 1),

(10, 'In cyber financial fraud, what is meant by the "Golden Hour"?',
'The time of day when cyber police are off duty',
'The initial 1 to 2 hours after a fraudulent transaction when calling 1930 has the highest chance of freezing funds in transit',
'The time it takes for a bank to issue a new debit card',
'The time required to reset your internet banking password',
'B', 1);

-- 5. FAQs (8 Entries)
INSERT INTO faq (faq_id, question, answer, admin_id) VALUES
(1, 'Can someone withdraw money from my bank account just by knowing my UPI ID or mobile number?', 
'No. Simply knowing your mobile number or UPI ID (VPA) allows someone to request or send money to you. However, funds can NEVER leave your account without you explicitly entering your confidential UPI PIN, MPIN, or bank OTP. Never authorize unexpected collect requests on UPI apps.', 1),

(2, 'What is the difference between Phishing, Smishing, and Vishing?',
'All three are social engineering techniques:
- Phishing: Conducted via deceptive emails impersonating trusted brands.
- Smishing: Conducted via SMS text messages containing malicious links or urgent threat alerts.
- Vishing: Conducted via voice phone calls where scammers use impersonation, fear, or urgency to coax confidential information.', 1),

(3, 'What immediate actions should I take if I accidentally entered my banking password on a suspicious link?',
'1. Immediately change your internet banking, UPI, and email passwords from a different, clean device.
2. Contact your bank''s 24x7 toll-free fraud helpline to temporarily freeze your net banking and block linked debit/credit cards.
3. Check your recent transaction history and mini-statement for any unauthorized debits.
4. Scan your device with an updated antivirus or perform a factory reset if an APK was downloaded.', 1),

(4, 'How does the 1930 Cyber Fraud Helpline work to recover stolen money?',
'The 1930 helpline (operated by the Indian Cyber Crime Coordination Centre - I4C) connects directly to the Citizen Financial Cyber Fraud Reporting and Management System (CFCFRMS). When you report a fraud immediately along with transaction UTR/reference numbers, the system sends an instant alert to the receiving bank/wallet to freeze the fraudulent amount in the scammer''s mule account before it can be withdrawn at an ATM.', 1),

(5, 'How can I lock my Aadhaar biometrics to prevent AePS (fingerprint) fraud?',
'1. Download the official "mAadhaar" app or visit https://myaadhaar.uidai.gov.in.
2. Log in using your Aadhaar number and OTP.
3. Navigate to "Lock/Unlock Biometrics".
4. Toggle the lock ON. Once locked, no one can use your fingerprint or iris scan for banking or SIM verification. You can unlock it temporarily for 10 minutes when you physically need it.', 1),

(6, 'Is it safe to store passwords in web browser autofill?',
'While modern browsers encrypt stored passwords, anyone with access to your unlocked computer or phone can view saved passwords in plain text. Furthermore, info-stealer malware specifically targets browser credential vaults. For maximum safety, use a dedicated, open-source password manager (like Bitwarden or KeePass) secured by a master passphrase and 2FA.', 1),

(7, 'How do cybercriminals spoof legitimate phone numbers and caller IDs?',
'Scammers use VoIP (Voice over IP) gateways and specialized caller ID spoofing tools that allow them to transmit any arbitrary phone number to the receiver''s screen, making the call appear as if it originates from your local police station, bank branch, or tax office. Never rely solely on caller ID; hang up and call the official verified number directly.', 1),

(8, 'What should I do if my social media account or WhatsApp is hacked?',
'For WhatsApp: Reinstall WhatsApp, enter your phone number, and verify with the 6-digit SMS code. This immediately logs out the hacker. Enable Two-Step Verification PIN inside WhatsApp settings.
For Social Media: Use the platform''s official account recovery page (e.g. instagram.com/hacked), submit a selfie video verification if prompted, revoke all active sessions, and change your linked email password immediately.', 1);

-- 6. Reporting Guidance (7 Entries)
INSERT INTO reporting_guidance (guidance_id, title, steps, official_link, admin_id) VALUES
(1, 'Emergency Financial Cyber Fraud Protocol (Helpline 1930)', 
'STEP 1: Act within the "Golden Hour" (first 1-2 hours) after fraudulent money transfer.
STEP 2: Call the national toll-free helpline 1930 immediately.
STEP 3: Provide the operator with your Bank Name, Account Number, Transaction Reference/UTR Number, Date & Time, and Suspect Account/UPI ID.
STEP 4: A formal ticket will be logged on the CFCFRMS portal, which triggers automated freeze holds on the beneficiary bank accounts.
STEP 5: Note down the SMS acknowledgment containing your complaint acknowledgement number.', 
'https://cybercrime.gov.in', 1),

(2, 'Filing a Detailed Complaint on National Cyber Crime Portal', 
'STEP 1: Visit the official portal: https://cybercrime.gov.in.
STEP 2: Click on "Report Other Cyber Crime" or "Report Crime Related to Women/Children".
STEP 3: Register / Login with your mobile number and state.
STEP 4: Fill in Incident Details (Category: Financial Fraud, Social Media, Identity Theft, etc.).
STEP 5: Upload mandatory evidence: Screenshots of chats, SMS, bank account statement highlighting the fraudulent debit, email headers, and call logs.
STEP 6: Submit the complaint and download the PDF copy for local police station follow-up.', 
'https://cybercrime.gov.in', 1),

(3, 'Emergency Steps for Stolen Cards & Compromised Net Banking', 
'STEP 1: Immediately dial your bank''s 24x7 emergency card blocking number or use the mobile banking app to toggle "Card Switch Off" / "Disable International & Online Transactions".
STEP 2: Change net banking login password, transaction password, and UPI MPIN.
STEP 3: Request the bank to issue a dispute Chargeback Form for unauthorized credit/debit card transactions within 3 days (under RBI Limited Liability framework).
STEP 4: Obtain a written acknowledgement or complaint ticket number from your bank branch.', 
'https://www.rbi.org.in', 1),

(4, 'Reporting Fake Loan Apps & Harassment to RBI Sachet', 
'STEP 1: Do NOT pay further extortion demands; paying encourages more blackmail.
STEP 2: Take screenshots of threatening messages, morphed photos, call recordings, and app permissions.
STEP 3: File a complaint on RBI''s Sachet portal (https://sachet.rbi.org.in) under "File a Complaint against Unregistered Entities".
STEP 4: Register an FIR at your nearest Cyber Police Station under IPC/BNS extortion and IT Act Section 66E (privacy violation).
STEP 5: Inform your key phone contacts via a broadcast message that your phone was compromised by a rogue app sending fake messages.', 
'https://sachet.rbi.org.in', 1),

(5, 'Action Plan for Social Media Identity Theft & Cloned Accounts', 
'STEP 1: Do not delete the fake profile link; copy the exact profile URL (e.g. instagram.com/fake_profile).
STEP 2: Take full-page screenshots showing the impersonating username, bio, and photos.
STEP 3: Report the profile directly inside the app: Select "Report" -> "It''s pretending to be someone else" -> "Me" or "A friend".
STEP 4: Ask 5-10 friends to report the same account for faster automated takedown.
STEP 5: If the account is extorting money or circulating obscene material, file a report on cybercrime.gov.in.', 
'https://www.instagram.com', 1),

(6, 'Reporting Suspect & Phishing Domains / Numbers to Chakshu Portal', 
'STEP 1: Department of Telecommunications (DoT) operates the Sanchar Saathi "Chakshu" facility.
STEP 2: Visit https://sancharsaathi.gov.in and click on "Chakshu - Report Suspected Fraud Communication".
STEP 3: Choose medium: Call, SMS, or WhatsApp.
STEP 4: Enter the fraudster''s phone number, date/time of communication, category (Sextortion, KYC expiry, Electricity bill threat, Loan offer).
STEP 5: Upload screenshot proof and submit to trigger carrier-level SIM deactivation and IMEI blacklisting.', 
'https://sancharsaathi.gov.in', 1),

(7, 'Evidence Checklist: What to Preserve Before Contacting Police', 
'Before submitting any formal cyber complaint, gather and organize the following digital evidence:
1. Bank Account Statement: PDF statement showing account number, IFSC, and the specific debit entries with UTR numbers.
2. SMS / Email Evidence: Raw email headers (original .eml file) or screenshots of the sender number and complete message text.
3. Chat Logs: Export entire WhatsApp/Telegram chat history without deleting any messages.
4. URLs & APKs: Exact website address or filename of any malicious application downloaded.
5. Call Recordings / Timestamps: Exact incoming phone numbers, call duration, and caller audio if recorded.', 
'https://cybercrime.gov.in', 1);
