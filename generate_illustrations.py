"""
Generates crisp, original, comic-book style vector SVG illustrations
for CyberHelp Awareness Hub, Scam Library, and Interactive Quiz.
"""
import os

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'img', 'illustrations')
os.makedirs(OUTPUT_DIR, exist_ok=True)

COMMON_DEFS = """
    <defs>
        <pattern id="halftone-dot" x="0" y="0" width="12" height="12" patternUnits="userSpaceOnUse">
            <circle cx="2" cy="2" r="1.5" fill="#0f172a" opacity="0.12"/>
        </pattern>
        <pattern id="halftone-red" x="0" y="0" width="12" height="12" patternUnits="userSpaceOnUse">
            <circle cx="2" cy="2" r="1.5" fill="#dc2626" opacity="0.15"/>
        </pattern>
        <pattern id="halftone-blue" x="0" y="0" width="12" height="12" patternUnits="userSpaceOnUse">
            <circle cx="2" cy="2" r="1.5" fill="#0284c7" opacity="0.15"/>
        </pattern>
        <pattern id="hazard-stripe" width="20" height="20" patternTransform="rotate(45 0 0)" patternUnits="userSpaceOnUse">
            <line x1="0" y1="0" x2="0" y2="20" stroke="#facc15" stroke-width="10" />
            <line x1="10" y1="0" x2="10" y2="20" stroke="#0f172a" stroke-width="10" />
        </pattern>
        <filter id="comic-shadow" x="-5%" y="-5%" width="115%" height="115%">
            <feDropShadow dx="3" dy="3" stdDeviation="0" flood-color="#0f172a" flood-opacity="1"/>
        </filter>
    </defs>
"""

ILLUSTRATIONS = {
    # ----------------- AWARENESS HUB ILLUSTRATIONS -----------------
    "awareness_phishing.svg": f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 220" width="100%" height="100%">
    {COMMON_DEFS}
    <rect width="400" height="220" fill="#f8fafc" rx="10"/>
    <rect width="400" height="220" fill="url(#halftone-dot)" rx="10"/>
    <rect x="8" y="8" width="384" height="204" fill="none" stroke="#0f172a" stroke-width="3" rx="8"/>
    
    <!-- Action Burst Backdrop -->
    <polygon points="200,20 225,55 270,30 260,75 305,80 275,115 310,145 265,150 275,195 230,175 200,210 170,175 125,195 135,150 90,145 125,115 95,80 140,75 130,30 175,55" fill="#fef08a" stroke="#0f172a" stroke-width="2.5" opacity="0.8"/>
    
    <!-- Phishing Hook Line -->
    <path d="M 120 10 Q 180 80 190 110" fill="none" stroke="#0f172a" stroke-width="3" stroke-dasharray="4,4"/>
    <path d="M 190 110 Q 195 140 180 145 Q 165 145 165 130" fill="none" stroke="#dc2626" stroke-width="4"/>
    <polygon points="165,130 160,138 172,135" fill="#dc2626"/>

    <!-- Fake Email Envelope Bait -->
    <g transform="translate(175, 75)" filter="url(#comic-shadow)">
        <rect x="0" y="0" width="130" height="75" fill="#ffffff" stroke="#0f172a" stroke-width="3" rx="6"/>
        <polyline points="0,0 65,45 130,0" fill="none" stroke="#0f172a" stroke-width="2.5"/>
        <rect x="15" y="48" width="100" height="16" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5" rx="3"/>
        <text x="20" y="60" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold" fill="#dc2626">paypa1-update.xyz</text>
    </g>

    <!-- Shield Intercepting -->
    <g transform="translate(50, 60)" filter="url(#comic-shadow)">
        <path d="M 45 5 L 80 18 C 80 65 45 85 45 85 C 45 85 10 65 10 18 Z" fill="#0284c7" stroke="#0f172a" stroke-width="3"/>
        <path d="M 45 12 L 72 23 C 72 60 45 76 45 76 C 45 76 18 60 18 23 Z" fill="#38bdf8"/>
        <polyline points="32,45 42,55 58,35" fill="none" stroke="#ffffff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
    </g>

    <!-- Comic Speech Bubble -->
    <g transform="translate(240, 25)" filter="url(#comic-shadow)">
        <path d="M 0 0 L 120 0 Q 130 0 130 10 L 130 35 Q 130 45 120 45 L 30 45 L 15 58 L 20 45 L 10 45 Q 0 45 0 35 Z" fill="#ffffff" stroke="#0f172a" stroke-width="2.5"/>
        <text x="65" y="27" font-family="'Bangers', cursive" font-size="16" fill="#dc2626" text-anchor="middle" letter-spacing="1">FAKE LINK TRAP!</text>
    </g>
    
    <text x="20" y="200" font-family="'Bangers', cursive" font-size="16" fill="#0f172a" letter-spacing="1">PHISHING &amp; SMISHING DEFENSE</text>
</svg>""",

    "awareness_otp_fraud.svg": f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 220" width="100%" height="100%">
    {COMMON_DEFS}
    <rect width="400" height="220" fill="#f8fafc" rx="10"/>
    <rect width="400" height="220" fill="url(#halftone-red)" rx="10"/>
    <rect x="8" y="8" width="384" height="204" fill="none" stroke="#0f172a" stroke-width="3" rx="8"/>

    <!-- Smartphone Graphic -->
    <g transform="translate(60, 25)" filter="url(#comic-shadow)">
        <rect x="0" y="0" width="110" height="165" fill="#1e293b" stroke="#0f172a" stroke-width="3" rx="14"/>
        <rect x="6" y="16" width="98" height="130" fill="#ffffff" rx="4"/>
        <!-- SMS Bubble -->
        <rect x="12" y="30" width="86" height="50" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5" rx="5"/>
        <text x="18" y="45" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold" fill="#0369a1">BANK ALERT:</text>
        <text x="18" y="60" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="800" fill="#dc2626">OTP: 739-204</text>
        <text x="18" y="72" font-family="'Plus Jakarta Sans', sans-serif" font-size="7" fill="#64748b">Never share with anyone.</text>
        <circle cx="55" cy="154" r="5" fill="#475569"/>
    </g>

    <!-- Thief Hand / Impostor Calling -->
    <g transform="translate(230, 35)">
        <!-- Shadowy Caller Silhouette -->
        <circle cx="90" cy="50" r="30" fill="#334155" stroke="#0f172a" stroke-width="3"/>
        <path d="M 50 120 C 50 85 80 85 90 85 C 100 85 130 85 130 120" fill="#1e293b" stroke="#0f172a" stroke-width="3"/>
        <rect x="75" y="40" width="40" height="8" fill="#111" rx="2" transform="rotate(-15 75 40)"/>
        <!-- Dialogue Demand -->
        <g transform="translate(-40, -10)" filter="url(#comic-shadow)">
            <path d="M 0 0 L 130 0 Q 140 0 140 10 L 140 38 Q 140 48 130 48 L 70 48 L 60 58 L 65 48 L 10 48 Q 0 48 0 38 Z" fill="#fee2e2" stroke="#dc2626" stroke-width="2.5"/>
            <text x="70" y="28" font-family="'Bangers', cursive" font-size="15" fill="#dc2626" text-anchor="middle">"READ ME YOUR OTP!"</text>
        </g>
    </g>

    <!-- Giant Hero Padlock Slam -->
    <g transform="translate(150, 75)" filter="url(#comic-shadow)">
        <path d="M 20 35 L 20 20 C 20 8 45 8 45 20 L 45 35" fill="none" stroke="#facc15" stroke-width="7" stroke-linecap="round"/>
        <rect x="5" y="32" width="55" height="50" fill="#dc2626" stroke="#0f172a" stroke-width="3" rx="8"/>
        <circle cx="32" cy="52" r="6" fill="#facc15"/>
        <polygon points="30,52 34,52 36,65 28,65" fill="#facc15"/>
    </g>

    <!-- Comic Action Stamp -->
    <g transform="translate(180, 150) rotate(-4)">
        <rect x="0" y="0" width="180" height="30" fill="#fef08a" stroke="#0f172a" stroke-width="2.5" rx="5" filter="url(#comic-shadow)"/>
        <text x="90" y="21" font-family="'Bangers', cursive" font-size="15" fill="#0f172a" text-anchor="middle" letter-spacing="1">NO BANK ASKS FOR OTP!</text>
    </g>
</svg>""",

    "awareness_qr_scams.svg": f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 220" width="100%" height="100%">
    {COMMON_DEFS}
    <rect width="400" height="220" fill="#f8fafc" rx="10"/>
    <rect width="400" height="220" fill="url(#halftone-dot)" rx="10"/>
    <rect x="8" y="8" width="384" height="204" fill="none" stroke="#0f172a" stroke-width="3" rx="8"/>

    <!-- Stylized QR Code Board -->
    <g transform="translate(45, 30)" filter="url(#comic-shadow)">
        <rect x="0" y="0" width="135" height="135" fill="#ffffff" stroke="#0f172a" stroke-width="3" rx="10"/>
        <!-- QR Corner Markers -->
        <rect x="15" y="15" width="30" height="30" fill="#0f172a" rx="4"/>
        <rect x="20" y="20" width="20" height="20" fill="#ffffff" rx="2"/>
        <rect x="24" y="24" width="12" height="12" fill="#0f172a"/>

        <rect x="90" y="15" width="30" height="30" fill="#0f172a" rx="4"/>
        <rect x="95" y="20" width="20" height="20" fill="#ffffff" rx="2"/>
        <rect x="99" y="24" width="12" height="12" fill="#0f172a"/>

        <rect x="15" y="90" width="30" height="30" fill="#0f172a" rx="4"/>
        <rect x="20" y="95" width="20" height="20" fill="#ffffff" rx="2"/>
        <rect x="24" y="99" width="12" height="12" fill="#0f172a"/>

        <!-- Mini QR Bits -->
        <rect x="55" y="20" width="12" height="12" fill="#0f172a"/>
        <rect x="70" y="35" width="10" height="10" fill="#0f172a"/>
        <rect x="55" y="55" width="25" height="25" fill="#dc2626"/>
        <text x="67" y="72" font-family="'Bangers', cursive" font-size="15" fill="#ffffff" text-anchor="middle">₹</text>
        <rect x="90" y="60" width="15" height="15" fill="#0f172a"/>
        <rect x="55" y="95" width="20" height="15" fill="#0f172a"/>
        <rect x="85" y="90" width="25" height="20" fill="#0f172a"/>
    </g>

    <!-- Red Debit Arrows Flying Away -->
    <g transform="translate(195, 45)">
        <path d="M 10 70 Q 50 10 110 30" fill="none" stroke="#dc2626" stroke-width="4" stroke-dasharray="6,4"/>
        <polygon points="115,31 100,22 105,37" fill="#dc2626"/>
        <!-- Flying Money Note -->
        <g transform="translate(80, 20) rotate(-15)" filter="url(#comic-shadow)">
            <rect x="0" y="0" width="65" height="34" fill="#86efac" stroke="#0f172a" stroke-width="2" rx="4"/>
            <circle cx="32" cy="17" r="9" fill="#22c55e"/>
            <text x="32" y="22" font-family="'Bangers', cursive" font-size="13" fill="#ffffff" text-anchor="middle">₹ 5000</text>
        </g>
    </g>

    <!-- Speech Dialogue Banner -->
    <g transform="translate(180, 110)" filter="url(#comic-shadow)">
        <path d="M 0 0 L 195 0 Q 205 0 205 10 L 205 50 Q 205 60 195 60 L 40 60 L 25 72 L 30 60 L 10 60 Q 0 60 0 50 Z" fill="#fef08a" stroke="#0f172a" stroke-width="2.5"/>
        <text x="100" y="26" font-family="'Bangers', cursive" font-size="16" fill="#dc2626" text-anchor="middle">SCANNING PAYS OUT MONEY!</text>
        <text x="100" y="47" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="800" fill="#0f172a" text-anchor="middle">You never scan QR to RECEIVE.</text>
    </g>
    
    <text x="25" y="195" font-family="'Bangers', cursive" font-size="16" fill="#0f172a">QR CODE PAYMENT FRAUD PATTERN</text>
</svg>""",

    "awareness_sim_swap.svg": f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 220" width="100%" height="100%">
    {COMMON_DEFS}
    <rect width="400" height="220" fill="#f8fafc" rx="10"/>
    <rect width="400" height="220" fill="url(#halftone-blue)" rx="10"/>
    <rect x="8" y="8" width="384" height="204" fill="none" stroke="#0f172a" stroke-width="3" rx="8"/>

    <!-- Cellular Tower -->
    <g transform="translate(40, 30)">
        <line x1="40" y1="140" x2="60" y2="20" stroke="#0f172a" stroke-width="3"/>
        <line x1="80" y1="140" x2="60" y2="20" stroke="#0f172a" stroke-width="3"/>
        <line x1="45" y1="110" x2="75" y2="110" stroke="#0f172a" stroke-width="2.5"/>
        <line x1="50" y1="75" x2="70" y2="75" stroke="#0f172a" stroke-width="2.5"/>
        <line x1="55" y1="45" x2="65" y2="45" stroke="#0f172a" stroke-width="2"/>
        <line x1="45" y1="140" x2="75" y2="110" stroke="#0f172a" stroke-width="1.5"/>
        <line x1="75" y1="140" x2="45" y2="110" stroke="#0f172a" stroke-width="1.5"/>
        <!-- Signal Waves Crossing out -->
        <path d="M 60 10 A 15 15 0 0 1 80 20" fill="none" stroke="#dc2626" stroke-width="3"/>
        <path d="M 60 0 A 25 25 0 0 1 95 20" fill="none" stroke="#dc2626" stroke-width="3"/>
        <line x1="70" y1="0" x2="90" y2="25" stroke="#dc2626" stroke-width="3.5"/>
    </g>

    <!-- Victim Phone showing NO SERVICE -->
    <g transform="translate(145, 35)" filter="url(#comic-shadow)">
        <rect x="0" y="0" width="95" height="145" fill="#ffffff" stroke="#0f172a" stroke-width="3" rx="12"/>
        <rect x="8" y="16" width="79" height="110" fill="#f1f5f9" rx="4"/>
        <!-- Red Alert Screen -->
        <rect x="14" y="35" width="67" height="60" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5" rx="6"/>
        <text x="47" y="55" font-family="'Bangers', cursive" font-size="14" fill="#dc2626" text-anchor="middle">NO SERVICE</text>
        <path d="M 35 68 L 59 68" stroke="#dc2626" stroke-width="2.5"/>
        <text x="47" y="82" font-family="'Plus Jakarta Sans', sans-serif" font-size="7" font-weight="bold" fill="#64748b" text-anchor="middle">SIGNAL CUT</text>
    </g>

    <!-- Swapped SIM Card in Fraudster Hand -->
    <g transform="translate(265, 45)" filter="url(#comic-shadow)">
        <!-- SIM Card Shape -->
        <path d="M 15 0 L 75 0 L 95 20 L 95 120 L 15 120 Z" fill="#facc15" stroke="#0f172a" stroke-width="3"/>
        <!-- Gold Chip -->
        <rect x="35" y="45" width="40" height="40" fill="#fef08a" stroke="#ca8a04" stroke-width="2" rx="4"/>
        <line x1="35" y1="65" x2="75" y2="65" stroke="#ca8a04" stroke-width="1.5"/>
        <line x1="55" y1="45" x2="55" y2="85" stroke="#ca8a04" stroke-width="1.5"/>
        <text x="55" y="105" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="middle">4G / 5G</text>
    </g>

    <!-- Comic POW Burst -->
    <g transform="translate(240, 20) rotate(10)" filter="url(#comic-shadow)">
        <polygon points="40,5 55,20 75,10 70,30 90,40 70,50 80,70 60,65 50,85 40,65 20,70 30,50 10,40 30,30 25,10 45,20" fill="#dc2626" stroke="#0f172a" stroke-width="2"/>
        <text x="50" y="48" font-family="'Bangers', cursive" font-size="13" fill="#ffffff" text-anchor="middle">SWAPPED!</text>
    </g>
    
    <text x="25" y="198" font-family="'Bangers', cursive" font-size="15" fill="#0f172a">SIM SWAP &amp; SIGNAL HIJACKING DEFENSE</text>
</svg>""",

    "awareness_aadhaar.svg": f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 220" width="100%" height="100%">
    {COMMON_DEFS}
    <rect width="400" height="220" fill="#f8fafc" rx="10"/>
    <rect width="400" height="220" fill="url(#halftone-dot)" rx="10"/>
    <rect x="8" y="8" width="384" height="204" fill="none" stroke="#0f172a" stroke-width="3" rx="8"/>

    <!-- Vault Safe Door -->
    <g transform="translate(60, 25)" filter="url(#comic-shadow)">
        <circle cx="85" cy="80" r="75" fill="#334155" stroke="#0f172a" stroke-width="3.5"/>
        <circle cx="85" cy="80" r="62" fill="#1e293b" stroke="#0f172a" stroke-width="2.5"/>
        <circle cx="85" cy="80" r="48" fill="#0284c7" stroke="#0f172a" stroke-width="2"/>
        
        <!-- Fingerprint Silhouette inside Vault -->
        <g transform="translate(65, 60)" stroke="#f8fafc" stroke-width="2.5" fill="none" stroke-linecap="round">
            <path d="M 20 8 Q 20 0 10 0 Q 0 0 0 8 Q 0 20 5 26 Q 10 32 10 40"/>
            <path d="M 26 12 Q 26 -4 10 -4 Q -6 -4 -6 12 Q -6 26 0 34"/>
            <path d="M 32 16 Q 32 -9 10 -9 Q -12 -9 -12 16 Q -12 30 -6 38"/>
            <path d="M 14 16 Q 14 6 10 6 Q 6 6 6 16 Q 6 26 10 32"/>
        </g>
        <!-- Vault Locking Spokes -->
        <rect x="80" y="8" width="10" height="15" fill="#facc15" stroke="#0f172a" stroke-width="1.5"/>
        <rect x="80" y="137" width="10" height="15" fill="#facc15" stroke="#0f172a" stroke-width="1.5"/>
        <rect x="13" y="75" width="15" height="10" fill="#facc15" stroke="#0f172a" stroke-width="1.5"/>
        <rect x="142" y="75" width="15" height="10" fill="#facc15" stroke="#0f172a" stroke-width="1.5"/>
    </g>

    <!-- Key & mAadhaar Shield -->
    <g transform="translate(245, 45)" filter="url(#comic-shadow)">
        <rect x="0" y="0" width="115" height="120" fill="#ffffff" stroke="#0f172a" stroke-width="3" rx="10"/>
        <!-- mAadhaar Header -->
        <rect x="0" y="0" width="115" height="32" fill="#0284c7" rx="9 9 0 0"/>
        <text x="58" y="22" font-family="'Bangers', cursive" font-size="14" fill="#ffffff" text-anchor="middle" letter-spacing="1">mAadhaar LOCK</text>
        <!-- Biometric Status -->
        <circle cx="58" cy="60" r="18" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
        <polyline points="48,60 55,67 68,53" fill="none" stroke="#16a34a" stroke-width="3.5" stroke-linecap="round"/>
        <text x="58" y="93" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" font-weight="bold" fill="#15803d" text-anchor="middle">BIOMETRICS LOCKED</text>
        <text x="58" y="107" font-family="'Plus Jakarta Sans', sans-serif" font-size="7" fill="#64748b" text-anchor="middle">Prevents AePS Fraud</text>
    </g>
    
    <text x="25" y="198" font-family="'Bangers', cursive" font-size="15" fill="#0f172a">LOCK BIOMETRICS VIA myaadhaar.uidai.gov.in</text>
</svg>""",

    "awareness_social_media.svg": f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 220" width="100%" height="100%">
    {COMMON_DEFS}
    <rect width="400" height="220" fill="#f8fafc" rx="10"/>
    <rect width="400" height="220" fill="url(#halftone-dot)" rx="10"/>
    <rect x="8" y="8" width="384" height="204" fill="none" stroke="#0f172a" stroke-width="3" rx="8"/>

    <!-- Left Authentic Profile Card -->
    <g transform="translate(35, 30)" filter="url(#comic-shadow)">
        <rect x="0" y="0" width="145" height="135" fill="#ffffff" stroke="#0f172a" stroke-width="2.5" rx="8"/>
        <circle cx="72" cy="45" r="24" fill="#38bdf8" stroke="#0f172a" stroke-width="2"/>
        <circle cx="72" cy="40" r="10" fill="#ffffff"/>
        <path d="M 55 60 C 55 52 89 52 89 60" fill="#ffffff"/>
        <!-- Verified Badge -->
        <circle cx="90" cy="55" r="7" fill="#0284c7"/>
        <polyline points="87,55 89,58 94,53" fill="none" stroke="#fff" stroke-width="1.5"/>
        <text x="72" y="85" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Rohan Sharma</text>
        <text x="72" y="100" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" fill="#64748b" text-anchor="middle">@rohan_official</text>
        <rect x="25" y="110" width="95" height="16" fill="#dcfce7" stroke="#16a34a" stroke-width="1" rx="4"/>
        <text x="72" y="122" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold" fill="#15803d" text-anchor="middle">REAL FRIEND</text>
    </g>

    <!-- VS Comic Badge -->
    <g transform="translate(180, 75)" filter="url(#comic-shadow)">
        <circle cx="20" cy="20" r="18" fill="#facc15" stroke="#0f172a" stroke-width="2.5"/>
        <text x="20" y="26" font-family="'Bangers', cursive" font-size="16" fill="#0f172a" text-anchor="middle">VS</text>
    </g>

    <!-- Right Cloned Profile Impostor -->
    <g transform="translate(220, 30)" filter="url(#comic-shadow)">
        <rect x="0" y="0" width="145" height="135" fill="#fff1f2" stroke="#dc2626" stroke-width="2.5" rx="8"/>
        <!-- Masked Avatar -->
        <circle cx="72" cy="45" r="24" fill="#f87171" stroke="#0f172a" stroke-width="2"/>
        <!-- Hacker Mask -->
        <rect x="58" y="38" width="28" height="10" fill="#0f172a" rx="3"/>
        <circle cx="65" cy="43" r="2.5" fill="#ffffff"/>
        <circle cx="79" cy="43" r="2.5" fill="#ffffff"/>
        <text x="72" y="85" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold" fill="#991b1b" text-anchor="middle">Rohan Sharma</text>
        <text x="72" y="100" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" fill="#dc2626" text-anchor="middle">@rohan_officia1 (CLONE)</text>
        <rect x="20" y="110" width="105" height="16" fill="#fee2e2" stroke="#dc2626" stroke-width="1" rx="4"/>
        <text x="72" y="122" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5" font-weight="bold" fill="#dc2626" text-anchor="middle">"SEND ₹5000 URGENT!"</text>
    </g>
    
    <text x="25" y="198" font-family="'Bangers', cursive" font-size="15" fill="#0f172a">CLONED PROFILE &amp; SOCIAL MEDIA IMPERSONATION</text>
</svg>""",

    "awareness_public_wifi.svg": f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 220" width="100%" height="100%">
    {COMMON_DEFS}
    <rect width="400" height="220" fill="#f8fafc" rx="10"/>
    <rect width="400" height="220" fill="url(#halftone-dot)" rx="10"/>
    <rect x="8" y="8" width="384" height="204" fill="none" stroke="#0f172a" stroke-width="3" rx="8"/>

    <!-- Coffee Cup in Cafe -->
    <g transform="translate(45, 60)" filter="url(#comic-shadow)">
        <ellipse cx="40" cy="80" rx="35" ry="10" fill="#cbd5e1"/>
        <path d="M 15 25 L 65 25 L 58 75 Q 40 85 22 75 Z" fill="#ffffff" stroke="#0f172a" stroke-width="2.5"/>
        <path d="M 60 35 C 75 35 75 55 60 55" fill="none" stroke="#0f172a" stroke-width="3"/>
        <path d="M 30 15 Q 35 5 30 -5" fill="none" stroke="#94a3b8" stroke-width="2"/>
        <path d="M 45 15 Q 50 5 45 -5" fill="none" stroke="#94a3b8" stroke-width="2"/>
    </g>

    <!-- Evil Twin Rogue Router -->
    <g transform="translate(150, 40)" filter="url(#comic-shadow)">
        <rect x="0" y="55" width="105" height="40" fill="#1e293b" stroke="#0f172a" stroke-width="3" rx="6"/>
        <!-- Antennas -->
        <line x1="20" y1="55" x2="10" y2="20" stroke="#0f172a" stroke-width="3.5" stroke-linecap="round"/>
        <line x1="85" y1="55" x2="95" y2="20" stroke="#0f172a" stroke-width="3.5" stroke-linecap="round"/>
        <!-- Blinking Skull / Threat Lights -->
        <circle cx="25" cy="75" r="4" fill="#22c55e"/>
        <circle cx="40" cy="75" r="4" fill="#eab308"/>
        <circle cx="55" cy="75" r="4" fill="#dc2626"/>
        <text x="80" y="80" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#ffffff">EVIL</text>
        
        <!-- Malicious Wave Sniffer -->
        <path d="M 52 15 A 18 18 0 0 1 80 25" fill="none" stroke="#dc2626" stroke-width="3"/>
        <path d="M 52 5 A 30 30 0 0 1 95 20" fill="none" stroke="#dc2626" stroke-width="3"/>
    </g>

    <!-- VPN Shield Defending -->
    <g transform="translate(275, 45)" filter="url(#comic-shadow)">
        <path d="M 45 5 L 80 18 C 80 75 45 95 45 95 C 45 95 10 75 10 18 Z" fill="#0284c7" stroke="#0f172a" stroke-width="3"/>
        <text x="45" y="45" font-family="'Bangers', cursive" font-size="18" fill="#facc15" text-anchor="middle">VPN</text>
        <text x="45" y="65" font-family="'Bangers', cursive" font-size="13" fill="#ffffff" text-anchor="middle">ACTIVE</text>
        <circle cx="45" cy="80" r="5" fill="#22c55e"/>
    </g>
    
    <text x="25" y="198" font-family="'Bangers', cursive" font-size="15" fill="#0f172a">PUBLIC WI-FI &amp; "EVIL TWIN" SNOOPING THREATS</text>
</svg>""",

    "awareness_ai_voice_clone.svg": f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 220" width="100%" height="100%">
    {COMMON_DEFS}
    <rect width="400" height="220" fill="#f8fafc" rx="10"/>
    <rect width="400" height="220" fill="url(#halftone-dot)" rx="10"/>
    <rect x="8" y="8" width="384" height="204" fill="none" stroke="#0f172a" stroke-width="3" rx="8"/>

    <!-- AI Voice Waveform Display -->
    <g transform="translate(40, 45)" filter="url(#comic-shadow)">
        <rect x="0" y="0" width="150" height="95" fill="#0f172a" stroke="#0f172a" stroke-width="3" rx="8"/>
        <!-- Digital Voice Bars -->
        <rect x="20" y="35" width="8" height="25" fill="#38bdf8" rx="2"/>
        <rect x="35" y="20" width="8" height="55" fill="#38bdf8" rx="2"/>
        <rect x="50" y="10" width="8" height="75" fill="#facc15" rx="2"/>
        <rect x="65" y="25" width="8" height="45" fill="#38bdf8" rx="2"/>
        <rect x="80" y="15" width="8" height="65" fill="#dc2626" rx="2"/>
        <rect x="95" y="30" width="8" height="35" fill="#38bdf8" rx="2"/>
        <rect x="110" y="40" width="8" height="15" fill="#38bdf8" rx="2"/>
        <text x="75" y="88" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" fill="#94a3b8" text-anchor="middle">AI VOICE CLONE: 98%</text>
    </g>

    <!-- Scammer Speech Bubble with cloned voice -->
    <g transform="translate(210, 30)" filter="url(#comic-shadow)">
        <path d="M 0 0 L 160 0 Q 170 0 170 10 L 170 45 Q 170 55 160 55 L 40 55 L 25 70 L 30 55 L 10 55 Q 0 55 0 45 Z" fill="#fee2e2" stroke="#dc2626" stroke-width="2.5"/>
        <text x="85" y="24" font-family="'Bangers', cursive" font-size="14" fill="#dc2626" text-anchor="middle">"MOM! I'M ARRESTED!"</text>
        <text x="85" y="42" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="middle">(Cloned in 3 Seconds!)</text>
    </g>

    <!-- Detective Safe Word Countermeasure -->
    <g transform="translate(210, 105)" filter="url(#comic-shadow)">
        <rect x="0" y="0" width="165" height="48" fill="#dcfce7" stroke="#16a34a" stroke-width="2.5" rx="8"/>
        <text x="82" y="22" font-family="'Bangers', cursive" font-size="13" fill="#15803d" text-anchor="middle">HERO COUNTERMEASURE:</text>
        <text x="82" y="38" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="middle">Ask Secret "Family Safe Word"</text>
    </g>
    
    <text x="25" y="198" font-family="'Bangers', cursive" font-size="15" fill="#0f172a">DEEPFAKE &amp; AI VOICE EMERGENCY DEFENSE</text>
</svg>""",

    "awareness_fake_antivirus.svg": f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 220" width="100%" height="100%">
    {COMMON_DEFS}
    <rect width="400" height="220" fill="#f8fafc" rx="10"/>
    <rect width="400" height="220" fill="url(#halftone-red)" rx="10"/>
    <rect x="8" y="8" width="384" height="204" fill="none" stroke="#0f172a" stroke-width="3" rx="8"/>

    <!-- Screaming Computer Monitor -->
    <g transform="translate(60, 25)" filter="url(#comic-shadow)">
        <rect x="0" y="0" width="180" height="120" fill="#0f172a" stroke="#0f172a" stroke-width="3" rx="8"/>
        <rect x="8" y="8" width="164" height="104" fill="#dc2626"/>
        <rect x="75" y="120" width="30" height="20" fill="#334155" stroke="#0f172a" stroke-width="2"/>
        <rect x="55" y="138" width="70" height="8" fill="#334155" stroke="#0f172a" stroke-width="2" rx="3"/>

        <!-- Popup Warning on Screen -->
        <rect x="18" y="18" width="144" height="84" fill="#ffffff" stroke="#0f172a" stroke-width="2" rx="4"/>
        <rect x="18" y="18" width="144" height="20" fill="#facc15" rx="4 4 0 0"/>
        <text x="90" y="33" font-family="'Bangers', cursive" font-size="12" fill="#0f172a" text-anchor="middle">⚠️ CRITICAL VIRUS DETECTED!</text>
        <text x="90" y="55" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold" fill="#dc2626" text-anchor="middle">5 TROJANS FOUND</text>
        <rect x="35" y="65" width="110" height="16" fill="#dc2626" rx="3"/>
        <text x="90" y="77" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">CALL: 1800-FAKE-HELP</text>
    </g>

    <!-- Comic Action Hand closing tab -->
    <g transform="translate(265, 45)" filter="url(#comic-shadow)">
        <rect x="0" y="0" width="110" height="85" fill="#ffffff" stroke="#0f172a" stroke-width="2.5" rx="8"/>
        <text x="55" y="24" font-family="'Bangers', cursive" font-size="14" fill="#0f172a" text-anchor="middle">SAFE ESCAPE:</text>
        <rect x="15" y="34" width="80" height="34" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5" rx="4"/>
        <text x="55" y="48" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#dc2626" text-anchor="middle">Ctrl+Shift+Esc</text>
        <text x="55" y="61" font-family="'Plus Jakarta Sans', sans-serif" font-size="7" font-weight="bold" fill="#64748b" text-anchor="middle">Kill Browser Tab</text>
    </g>
    
    <text x="25" y="198" font-family="'Bangers', cursive" font-size="15" fill="#0f172a">FAKE BROWSER ALERT &amp; POPUP COUNTERMEASURES</text>
</svg>""",

    "awareness_digital_arrest.svg": f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 220" width="100%" height="100%">
    {COMMON_DEFS}
    <rect width="400" height="220" fill="#f8fafc" rx="10"/>
    <rect width="400" height="220" fill="url(#halftone-red)" rx="10"/>
    <rect x="8" y="8" width="384" height="204" fill="none" stroke="#0f172a" stroke-width="3" rx="8"/>

    <!-- Video Call Window with Fake Cop -->
    <g transform="translate(45, 25)" filter="url(#comic-shadow)">
        <rect x="0" y="0" width="190" height="135" fill="#ffffff" stroke="#0f172a" stroke-width="3" rx="8"/>
        <!-- Window Bar -->
        <rect x="0" y="0" width="190" height="22" fill="#1e293b" rx="6 6 0 0"/>
        <circle cx="12" cy="11" r="4" fill="#ef4444"/>
        <circle cx="24" cy="11" r="4" fill="#f59e0b"/>
        <circle cx="36" cy="11" r="4" fill="#10b981"/>
        <text x="110" y="15" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold" fill="#ffffff">Skype Video Call &bull; LIVE</text>
        
        <!-- Fake Cop in Uniform -->
        <rect x="8" y="28" width="174" height="100" fill="#f1f5f9"/>
        <circle cx="95" cy="65" r="22" fill="#f59e0b" stroke="#0f172a" stroke-width="2"/>
        <rect x="75" y="50" width="40" height="12" fill="#1e293b" rx="3"/>
        <path d="M 60 115 C 60 90 80 85 95 85 C 110 85 130 90 130 115" fill="#854d0e" stroke="#0f172a" stroke-width="2"/>
        <polygon points="95,85 91,100 99,100" fill="#facc15"/>
    </g>

    <!-- Giant Rejection Stamp -->
    <g transform="translate(210, 50) rotate(-6)" filter="url(#comic-shadow)">
        <rect x="0" y="0" width="165" height="75" fill="#fee2e2" stroke="#dc2626" stroke-width="3" stroke-dasharray="6,4" rx="8"/>
        <text x="82" y="32" font-family="'Bangers', cursive" font-size="20" fill="#dc2626" text-anchor="middle" letter-spacing="1">100% FAKE!</text>
        <text x="82" y="52" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="800" fill="#0f172a" text-anchor="middle">NO "DIGITAL ARREST"</text>
        <text x="82" y="65" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5" fill="#64748b" text-anchor="middle">Police Never Trial on Skype</text>
    </g>
    
    <text x="25" y="198" font-family="'Bangers', cursive" font-size="15" fill="#0f172a">DIGITAL ARREST &amp; LAW ENFORCEMENT EXTORTION SCAMS</text>
</svg>""",

    # ----------------- SCAM LIBRARY ILLUSTRATIONS -----------------
    "scam_telegram_job.svg": f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 200" width="100%" height="100%">
    {COMMON_DEFS}
    <rect width="360" height="200" fill="#f8fafc" rx="8"/>
    <rect width="360" height="200" fill="url(#halftone-dot)" rx="8"/>
    <rect x="6" y="6" width="348" height="188" fill="none" stroke="#0f172a" stroke-width="2.5" rx="6"/>

    <!-- Telegram Channel Mockup -->
    <g transform="translate(35, 25)" filter="url(#comic-shadow)">
        <rect x="0" y="0" width="140" height="125" fill="#ffffff" stroke="#0f172a" stroke-width="2.5" rx="8"/>
        <rect x="0" y="0" width="140" height="26" fill="#0284c7" rx="6 6 0 0"/>
        <text x="70" y="18" font-family="'Bangers', cursive" font-size="12" fill="#ffffff" text-anchor="middle">VIP PREPAID TASKS</text>
        <!-- Task 1 payout -->
        <rect x="10" y="34" width="120" height="22" fill="#dcfce7" stroke="#16a34a" stroke-width="1" rx="4"/>
        <text x="70" y="48" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5" font-weight="bold" fill="#15803d" text-anchor="middle">Like 3 Vids = +₹450 Paid!</text>
        <!-- Task Trap -->
        <rect x="10" y="62" width="120" height="48" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5" rx="4"/>
        <text x="70" y="78" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold" fill="#dc2626" text-anchor="middle">VIP LEVEL 5:</text>
        <text x="70" y="94" font-family="'Bangers', cursive" font-size="11" fill="#991b1b" text-anchor="middle">DEPOSIT ₹50,000</text>
    </g>

    <!-- Trap Pit & Flytrap -->
    <g transform="translate(200, 35)">
        <polygon points="50,15 70,30 95,15 85,45 110,60 80,75 85,105 60,85 35,105 40,75 10,60 35,45 25,15" fill="#dc2626" stroke="#0f172a" stroke-width="2"/>
        <text x="60" y="66" font-family="'Bangers', cursive" font-size="16" fill="#ffffff" text-anchor="middle">TRAP!</text>
    </g>
    
    <text x="20" y="178" font-family="'Bangers', cursive" font-size="14" fill="#0f172a">PART-TIME TASK &amp; TELEGRAM JOB FRAUD</text>
</svg>""",

    "scam_loan_app.svg": f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 200" width="100%" height="100%">
    {COMMON_DEFS}
    <rect width="360" height="200" fill="#f8fafc" rx="8"/>
    <rect width="360" height="200" fill="url(#halftone-red)" rx="8"/>
    <rect x="6" y="6" width="348" height="188" fill="none" stroke="#0f172a" stroke-width="2.5" rx="6"/>

    <!-- Shady Phone App Screen -->
    <g transform="translate(40, 25)" filter="url(#comic-shadow)">
        <rect x="0" y="0" width="100" height="135" fill="#1e293b" stroke="#0f172a" stroke-width="2.5" rx="10"/>
        <rect x="6" y="12" width="88" height="110" fill="#ffffff" rx="4"/>
        <text x="50" y="30" font-family="'Bangers', cursive" font-size="12" fill="#0284c7" text-anchor="middle">QUICK ₹10,000</text>
        <text x="50" y="42" font-family="'Plus Jakarta Sans', sans-serif" font-size="7" fill="#64748b" text-anchor="middle">0 Docs Required!</text>
        
        <!-- Invasive Permission Warning -->
        <rect x="12" y="52" width="76" height="60" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5" rx="4"/>
        <text x="50" y="68" font-family="'Plus Jakarta Sans', sans-serif" font-size="7" font-weight="bold" fill="#dc2626" text-anchor="middle">STEALING DATA:</text>
        <text x="50" y="80" font-family="'Plus Jakarta Sans', sans-serif" font-size="7" fill="#475569" text-anchor="middle">✓ All Contacts</text>
        <text x="50" y="92" font-family="'Plus Jakarta Sans', sans-serif" font-size="7" fill="#475569" text-anchor="middle">✓ Photo Gallery</text>
        <text x="50" y="104" font-family="'Plus Jakarta Sans', sans-serif" font-size="7" fill="#475569" text-anchor="middle">✓ Camera / Mic</text>
    </g>

    <!-- Blackmail Skull -->
    <g transform="translate(175, 30)" filter="url(#comic-shadow)">
        <rect x="0" y="0" width="135" height="120" fill="#fee2e2" stroke="#dc2626" stroke-width="2.5" rx="8"/>
        <text x="67" y="30" font-family="'Bangers', cursive" font-size="16" fill="#991b1b" text-anchor="middle">EXTORTION RACKET</text>
        <text x="67" y="50" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">Recovery Agents Morph</text>
        <text x="67" y="65" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">Victim Photos to Blackmail</text>
        <rect x="15" y="80" width="105" height="25" fill="#dc2626" rx="4"/>
        <text x="67" y="97" font-family="'Bangers', cursive" font-size="12" fill="#ffffff" text-anchor="middle">NEVER PAY RANSOM!</text>
    </g>
    
    <text x="20" y="180" font-family="'Bangers', cursive" font-size="14" fill="#0f172a">INSTANT FAKE LOAN APP EXTORTION</text>
</svg>""",

    "scam_electricity_bill.svg": f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 200" width="100%" height="100%">
    {COMMON_DEFS}
    <rect width="360" height="200" fill="#f8fafc" rx="8"/>
    <rect width="360" height="200" fill="url(#halftone-dot)" rx="8"/>
    <rect x="6" y="6" width="348" height="188" fill="none" stroke="#0f172a" stroke-width="2.5" rx="6"/>

    <!-- Urgent Threat SMS Card -->
    <g transform="translate(30, 25)" filter="url(#comic-shadow)">
        <rect x="0" y="0" width="170" height="125" fill="#fee2e2" stroke="#dc2626" stroke-width="2.5" rx="8"/>
        <rect x="0" y="0" width="170" height="24" fill="#dc2626" rx="6 6 0 0"/>
        <text x="85" y="17" font-family="'Bangers', cursive" font-size="12" fill="#ffffff" text-anchor="middle">⚡ ELECTRICITY POWER THREAT</text>
        <text x="12" y="42" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold" fill="#991b1b">Dear Consumer,</text>
        <text x="12" y="58" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" fill="#1e293b">Your power will be cut tonight at</text>
        <text x="12" y="73" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#dc2626">9:30 PM due to unpaid bill.</text>
        <text x="12" y="90" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" fill="#1e293b">Immediately call officer at</text>
        <text x="12" y="105" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#0284c7">98XXXXXX (PERSONAL NUMBER)</text>
    </g>

    <!-- Clock ticking down -->
    <g transform="translate(230, 35)" filter="url(#comic-shadow)">
        <circle cx="50" cy="50" r="42" fill="#facc15" stroke="#0f172a" stroke-width="3"/>
        <line x1="50" y1="50" x2="50" y2="25" stroke="#0f172a" stroke-width="4" stroke-linecap="round"/>
        <line x1="50" y1="50" x2="72" y2="50" stroke="#dc2626" stroke-width="3.5" stroke-linecap="round"/>
        <text x="50" y="75" font-family="'Bangers', cursive" font-size="13" fill="#dc2626" text-anchor="middle">URGENCY HOAX!</text>
    </g>
    
    <text x="20" y="180" font-family="'Bangers', cursive" font-size="14" fill="#0f172a">ELECTRICITY BILL POWER CUT SMS THREAT</text>
</svg>""",

    "scam_courier_drugs.svg": f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 200" width="100%" height="100%">
    {COMMON_DEFS}
    <rect width="360" height="200" fill="#f8fafc" rx="8"/>
    <rect width="360" height="200" fill="url(#halftone-dot)" rx="8"/>
    <rect x="6" y="6" width="348" height="188" fill="none" stroke="#0f172a" stroke-width="2.5" rx="6"/>

    <!-- Courier Box -->
    <g transform="translate(35, 30)" filter="url(#comic-shadow)">
        <polygon points="20,40 70,10 130,30 80,60" fill="#d97706" stroke="#0f172a" stroke-width="2.5"/>
        <polygon points="20,40 80,60 80,120 20,100" fill="#b45309" stroke="#0f172a" stroke-width="2.5"/>
        <polygon points="80,60 130,30 130,90 80,120" fill="#92400e" stroke="#0f172a" stroke-width="2.5"/>
        <rect x="35" y="70" width="35" height="20" fill="#ffffff" stroke="#0f172a" stroke-width="1.5" rx="2"/>
        <text x="52" y="83" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" fill="#dc2626" text-anchor="middle">MDMA?</text>
    </g>

    <!-- Fake Police Warning Call -->
    <g transform="translate(190, 25)" filter="url(#comic-shadow)">
        <rect x="0" y="0" width="135" height="125" fill="#fee2e2" stroke="#dc2626" stroke-width="2.5" rx="8"/>
        <text x="67" y="25" font-family="'Bangers', cursive" font-size="14" fill="#dc2626" text-anchor="middle">FAKE NARCOTICS FIR</text>
        <text x="67" y="45" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">"Parcel Seized with Drugs"</text>
        <text x="67" y="60" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" fill="#475569" text-anchor="middle">Transferred to Fake Police</text>
        <text x="67" y="75" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold" fill="#991b1b" text-anchor="middle">Demands RBI Fund Escrow</text>
        <rect x="15" y="88" width="105" height="24" fill="#0f172a" rx="4"/>
        <text x="67" y="104" font-family="'Bangers', cursive" font-size="11" fill="#facc15" text-anchor="middle">CALL POLICE 1930</text>
    </g>
    
    <text x="20" y="180" font-family="'Bangers', cursive" font-size="14" fill="#0f172a">COURIER PARCEL &amp; CUSTOMS POLICE EXTORTION</text>
</svg>""",

    "scam_lottery_kbc.svg": f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 200" width="100%" height="100%">
    {COMMON_DEFS}
    <rect width="360" height="200" fill="#f8fafc" rx="8"/>
    <rect width="360" height="200" fill="url(#halftone-dot)" rx="8"/>
    <rect x="6" y="6" width="348" height="188" fill="none" stroke="#0f172a" stroke-width="2.5" rx="6"/>

    <!-- WhatsApp Lottery Certificate -->
    <g transform="translate(35, 25)" filter="url(#comic-shadow)">
        <rect x="0" y="0" width="155" height="125" fill="#fef9c3" stroke="#ca8a04" stroke-width="2.5" rx="8"/>
        <rect x="0" y="0" width="155" height="24" fill="#22c55e" rx="6 6 0 0"/>
        <text x="77" y="17" font-family="'Bangers', cursive" font-size="13" fill="#ffffff" text-anchor="middle">WHATSAPP LUCKY DRAW</text>
        <text x="77" y="45" font-family="'Bangers', cursive" font-size="18" fill="#ca8a04" text-anchor="middle">WON ₹25 LAKHS!</text>
        <text x="77" y="65" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" fill="#0f172a" text-anchor="middle">"KBC All India SIM Lottery"</text>
        <!-- Fee Demand Trap -->
        <rect x="15" y="78" width="125" height="35" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5" rx="4"/>
        <text x="77" y="93" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5" font-weight="bold" fill="#dc2626" text-anchor="middle">TRAP: Pay ₹25,000 GST</text>
        <text x="77" y="105" font-family="'Plus Jakarta Sans', sans-serif" font-size="7" fill="#64748b" text-anchor="middle">Charges into Mule Account</text>
    </g>

    <!-- Comic Red Stamp -->
    <g transform="translate(210, 45) rotate(-10)" filter="url(#comic-shadow)">
        <rect x="0" y="0" width="120" height="60" fill="#fee2e2" stroke="#dc2626" stroke-width="3" stroke-dasharray="4,3" rx="6"/>
        <text x="60" y="28" font-family="'Bangers', cursive" font-size="18" fill="#dc2626" text-anchor="middle">100% FRAUD</text>
        <text x="60" y="47" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">No SIM Lotteries Exist</text>
    </g>
    
    <text x="20" y="180" font-family="'Bangers', cursive" font-size="14" fill="#0f172a">KBC WHATSAPP LOTTERY &amp; LUCKY DRAW SCAM</text>
</svg>""",

    "scam_remote_access.svg": f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 200" width="100%" height="100%">
    {COMMON_DEFS}
    <rect width="360" height="200" fill="#f8fafc" rx="8"/>
    <rect width="360" height="200" fill="url(#halftone-dot)" rx="8"/>
    <rect x="6" y="6" width="348" height="188" fill="none" stroke="#0f172a" stroke-width="2.5" rx="6"/>

    <!-- Screen with 9-digit code -->
    <g transform="translate(35, 25)" filter="url(#comic-shadow)">
        <rect x="0" y="0" width="130" height="125" fill="#ffffff" stroke="#0f172a" stroke-width="2.5" rx="8"/>
        <rect x="0" y="0" width="130" height="24" fill="#dc2626" rx="6 6 0 0"/>
        <text x="65" y="17" font-family="'Bangers', cursive" font-size="12" fill="#ffffff" text-anchor="middle">AnyDesk / TeamViewer</text>
        <text x="65" y="45" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">Remote Screen Code:</text>
        <rect x="15" y="52" width="100" height="25" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5" rx="4"/>
        <text x="65" y="69" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" fill="#dc2626" text-anchor="middle">839-102-485</text>
        <text x="65" y="95" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5" fill="#64748b" text-anchor="middle">Sharing grants 100%</text>
        <text x="65" y="108" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5" font-weight="bold" fill="#dc2626" text-anchor="middle">Control of Your Bank!</text>
    </g>

    <!-- Puppet Strings Graphic -->
    <g transform="translate(195, 30)">
        <path d="M 60 10 L 20 60" stroke="#0f172a" stroke-width="2" stroke-dasharray="3,3"/>
        <path d="M 60 10 L 60 70" stroke="#0f172a" stroke-width="2" stroke-dasharray="3,3"/>
        <path d="M 60 10 L 100 60" stroke="#0f172a" stroke-width="2" stroke-dasharray="3,3"/>
        <rect x="25" y="65" width="90" height="45" fill="#facc15" stroke="#0f172a" stroke-width="2.5" rx="6" filter="url(#comic-shadow)"/>
        <text x="70" y="85" font-family="'Bangers', cursive" font-size="13" fill="#0f172a" text-anchor="middle">PUPPET MASTER</text>
        <text x="70" y="100" font-family="'Plus Jakarta Sans', sans-serif" font-size="7" font-weight="bold" fill="#991b1b" text-anchor="middle">Never Share Screen Codes</text>
    </g>
    
    <text x="20" y="180" font-family="'Bangers', cursive" font-size="14" fill="#0f172a">REMOTE ACCESS DESKTOP SHARING FRAUD</text>
</svg>""",

    "scam_search_poisoning.svg": f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 200" width="100%" height="100%">
    {COMMON_DEFS}
    <rect width="360" height="200" fill="#f8fafc" rx="8"/>
    <rect width="360" height="200" fill="url(#halftone-dot)" rx="8"/>
    <rect x="6" y="6" width="348" height="188" fill="none" stroke="#0f172a" stroke-width="2.5" rx="6"/>

    <!-- Search Engine Mockup -->
    <g transform="translate(25, 25)" filter="url(#comic-shadow)">
        <rect x="0" y="0" width="300" height="125" fill="#ffffff" stroke="#0f172a" stroke-width="2.5" rx="8"/>
        <!-- Search Input Bar -->
        <rect x="15" y="12" width="270" height="25" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" rx="12"/>
        <text x="30" y="28" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" fill="#0f172a">🔍 Bank Customer Care Toll Free</text>
        
        <!-- Malicious Top Search Result -->
        <rect x="15" y="45" width="270" height="68" fill="#fee2e2" stroke="#dc2626" stroke-width="2" rx="6"/>
        <text x="25" y="62" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold" fill="#dc2626">Ad &bull; https://fake-bank-helpline-mumbai.com</text>
        <text x="25" y="78" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold" fill="#1e293b">24x7 Customer Helpline Support</text>
        <text x="25" y="98" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" fill="#dc2626">Call: 9820-XX-XXXX (SPOOFED MULE NUMBER)</text>
    </g>
    
    <text x="20" y="180" font-family="'Bangers', cursive" font-size="14" fill="#0f172a">SEARCH ENGINE POISONING &amp; FAKE CUSTOMER CARE</text>
</svg>""",

    "scam_romance_gift.svg": f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 200" width="100%" height="100%">
    {COMMON_DEFS}
    <rect width="360" height="200" fill="#f8fafc" rx="8"/>
    <rect width="360" height="200" fill="url(#halftone-dot)" rx="8"/>
    <rect x="6" y="6" width="348" height="188" fill="none" stroke="#0f172a" stroke-width="2.5" rx="6"/>

    <!-- Gift Box with Customs Clearance Trap -->
    <g transform="translate(35, 25)" filter="url(#comic-shadow)">
        <rect x="0" y="0" width="135" height="125" fill="#fdf2f8" stroke="#db2777" stroke-width="2.5" rx="8"/>
        <!-- Gift Box -->
        <rect x="25" y="30" width="85" height="55" fill="#f472b6" stroke="#0f172a" stroke-width="2" rx="4"/>
        <line x1="67" y1="30" x2="67" y2="85" stroke="#facc15" stroke-width="8"/>
        <line x1="25" y1="57" x2="110" y2="57" stroke="#facc15" stroke-width="8"/>
        <circle cx="67" cy="27" r="10" fill="#facc15" stroke="#0f172a" stroke-width="1.5"/>
        <text x="67" y="103" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold" fill="#be185d" text-anchor="middle">"SENT LUXURY IPHONE"</text>
    </g>

    <!-- Fake Customs Call -->
    <g transform="translate(195, 30)" filter="url(#comic-shadow)">
        <rect x="0" y="0" width="135" height="115" fill="#fee2e2" stroke="#dc2626" stroke-width="2.5" rx="8"/>
        <text x="67" y="25" font-family="'Bangers', cursive" font-size="14" fill="#dc2626" text-anchor="middle">DELHI AIRPORT CUSTOMS</text>
        <text x="67" y="45" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" fill="#0f172a" text-anchor="middle">"Gift intercepted!"</text>
        <text x="67" y="60" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold" fill="#991b1b" text-anchor="middle">Pay ₹75,000 Anti-Money</text>
        <text x="67" y="73" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold" fill="#991b1b" text-anchor="middle">Laundering Fee</text>
        <rect x="15" y="85" width="105" height="20" fill="#dc2626" rx="3"/>
        <text x="67" y="99" font-family="'Bangers', cursive" font-size="11" fill="#ffffff" text-anchor="middle">NEVER PAY FEES</text>
    </g>
    
    <text x="20" y="180" font-family="'Bangers', cursive" font-size="14" fill="#0f172a">MATRIMONIAL &amp; ROMANCE GIFT CUSTOMS EXTORTION</text>
</svg>""",

    "scam_amazon_review.svg": f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 200" width="100%" height="100%">
    {COMMON_DEFS}
    <rect width="360" height="200" fill="#f8fafc" rx="8"/>
    <rect width="360" height="200" fill="url(#halftone-dot)" rx="8"/>
    <rect x="6" y="6" width="348" height="188" fill="none" stroke="#0f172a" stroke-width="2.5" rx="6"/>

    <!-- 30 Orders Combo Trap -->
    <g transform="translate(35, 25)" filter="url(#comic-shadow)">
        <rect x="0" y="0" width="140" height="125" fill="#ffffff" stroke="#0f172a" stroke-width="2.5" rx="8"/>
        <rect x="0" y="0" width="140" height="24" fill="#f59e0b" rx="6 6 0 0"/>
        <text x="70" y="17" font-family="'Bangers', cursive" font-size="12" fill="#0f172a" text-anchor="middle">PRODUCT BOOST TASKS</text>
        <text x="70" y="45" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">Task 14 of 30 Complete</text>
        
        <!-- Negative Balance Trap -->
        <rect x="12" y="55" width="116" height="55" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5" rx="4"/>
        <text x="70" y="72" font-family="'Bangers', cursive" font-size="12" fill="#dc2626" text-anchor="middle">COMBO ORDER HIT!</text>
        <text x="70" y="87" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold" fill="#991b1b" text-anchor="middle">Balance: -₹45,000</text>
        <text x="70" y="100" font-family="'Plus Jakarta Sans', sans-serif" font-size="7" fill="#64748b" text-anchor="middle">Deposit to unlock principal</text>
    </g>

    <!-- Trap Stamp -->
    <g transform="translate(200, 45) rotate(-5)" filter="url(#comic-shadow)">
        <rect x="0" y="0" width="130" height="70" fill="#fef08a" stroke="#0f172a" stroke-width="3" rx="8"/>
        <text x="65" y="32" font-family="'Bangers', cursive" font-size="16" fill="#dc2626" text-anchor="middle">SUNK COST TRAP!</text>
        <text x="65" y="52" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">Deposits Never Return</text>
    </g>
    
    <text x="20" y="180" font-family="'Bangers', cursive" font-size="14" fill="#0f172a">E-COMMERCE ORDER RATING &amp; COMBO TASK TRAP</text>
</svg>""",

    "scam_pig_butchering.svg": f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 200" width="100%" height="100%">
    {COMMON_DEFS}
    <rect width="360" height="200" fill="#f8fafc" rx="8"/>
    <rect width="360" height="200" fill="url(#halftone-dot)" rx="8"/>
    <rect x="6" y="6" width="348" height="188" fill="none" stroke="#0f172a" stroke-width="2.5" rx="6"/>

    <!-- Manipulated Crypto Graph -->
    <g transform="translate(30, 25)" filter="url(#comic-shadow)">
        <rect x="0" y="0" width="150" height="125" fill="#0f172a" stroke="#0f172a" stroke-width="2.5" rx="8"/>
        <!-- Fake Spiking Graph -->
        <polyline points="15,95 45,85 75,70 100,30 135,15" fill="none" stroke="#22c55e" stroke-width="3.5"/>
        <polygon points="15,95 45,85 75,70 100,30 135,15 135,110 15,110" fill="#22c55e" opacity="0.15"/>
        <text x="75" y="105" font-family="'Bangers', cursive" font-size="14" fill="#22c55e" text-anchor="middle">+500% FAKE PROFIT</text>
    </g>

    <!-- Withdrawal Freeze Lock -->
    <g transform="translate(200, 30)" filter="url(#comic-shadow)">
        <rect x="0" y="0" width="130" height="115" fill="#fee2e2" stroke="#dc2626" stroke-width="2.5" rx="8"/>
        <text x="65" y="28" font-family="'Bangers', cursive" font-size="15" fill="#dc2626" text-anchor="middle">FROZEN WITHDRAWAL</text>
        <text x="65" y="50" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">Demands 20% Tax Deposit</text>
        <text x="65" y="65" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" fill="#475569" text-anchor="middle">Before Any Funds Release</text>
        <rect x="15" y="78" width="100" height="25" fill="#dc2626" rx="4"/>
        <text x="65" y="95" font-family="'Bangers', cursive" font-size="12" fill="#ffffff" text-anchor="middle">FUNDS ARE GONE</text>
    </g>
    
    <text x="20" y="180" font-family="'Bangers', cursive" font-size="14" fill="#0f172a">CRYPTO / FOREX PIG BUTCHERING INVESTMENT FRAUD</text>
</svg>""",

    # ----------------- QUIZ SQUAD CHARACTERS & TROPHY -----------------
    "quiz_captain_shield.svg": f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="100%" height="100%">
    {COMMON_DEFS}
    <circle cx="80" cy="80" r="75" fill="#e0f2fe" stroke="#0f172a" stroke-width="3.5"/>
    <circle cx="80" cy="80" r="75" fill="url(#halftone-blue)"/>
    
    <!-- Hero Cap / Helmet -->
    <circle cx="80" cy="65" r="38" fill="#fcd34d" stroke="#0f172a" stroke-width="3"/>
    <path d="M 45 60 C 45 35 115 35 115 60 Z" fill="#0284c7" stroke="#0f172a" stroke-width="3"/>
    
    <!-- Hero Mask & Eyes -->
    <rect x="52" y="54" width="56" height="16" fill="#0f172a" rx="4"/>
    <ellipse cx="66" cy="62" rx="6" ry="4" fill="#ffffff"/>
    <ellipse cx="94" cy="62" rx="6" ry="4" fill="#ffffff"/>
    <!-- Confident Smile -->
    <path d="M 70 82 Q 80 92 90 82" fill="none" stroke="#0f172a" stroke-width="3" stroke-linecap="round"/>
    
    <!-- Hero Suit / Torso -->
    <path d="M 38 150 C 38 115 60 100 80 100 C 100 100 122 115 122 150 Z" fill="#0284c7" stroke="#0f172a" stroke-width="3.5"/>
    <!-- Chest Shield Emblem -->
    <path d="M 80 108 L 94 116 C 94 135 80 142 80 142 C 80 142 66 135 66 116 Z" fill="#facc15" stroke="#0f172a" stroke-width="2"/>
    <text x="80" y="130" font-family="'Bangers', cursive" font-size="12" fill="#0f172a" text-anchor="middle">S</text>
</svg>""",

    "quiz_agent_cipher.svg": f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="100%" height="100%">
    {COMMON_DEFS}
    <circle cx="80" cy="80" r="75" fill="#fef08a" stroke="#0f172a" stroke-width="3.5"/>
    <circle cx="80" cy="80" r="75" fill="url(#halftone-dot)"/>
    
    <!-- Head -->
    <circle cx="80" cy="65" r="36" fill="#fed7aa" stroke="#0f172a" stroke-width="3"/>
    <!-- Detective Beret / Hair -->
    <path d="M 45 55 C 45 28 115 28 120 52 C 105 45 60 48 45 55 Z" fill="#1e293b" stroke="#0f172a" stroke-width="3"/>
    <circle cx="80" cy="28" r="4" fill="#dc2626"/>
    
    <!-- Cyber Visor / High-tech Glasses -->
    <rect x="50" y="52" width="60" height="18" fill="#38bdf8" stroke="#0f172a" stroke-width="2.5" rx="4"/>
    <line x1="50" y1="61" x2="110" y2="61" stroke="#ffffff" stroke-width="2"/>
    <path d="M 72 82 Q 80 88 88 82" fill="none" stroke="#0f172a" stroke-width="3" stroke-linecap="round"/>
    
    <!-- Forensic Coat / Trench -->
    <path d="M 38 150 C 38 115 60 102 80 102 C 100 102 122 115 122 150 Z" fill="#475569" stroke="#0f172a" stroke-width="3.5"/>
    <polygon points="80,102 72,125 88,125" fill="#facc15" stroke="#0f172a" stroke-width="2"/>
</svg>""",

    "quiz_buster_bot.svg": f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="100%" height="100%">
    {COMMON_DEFS}
    <circle cx="80" cy="80" r="75" fill="#dcfce7" stroke="#0f172a" stroke-width="3.5"/>
    <circle cx="80" cy="80" r="75" fill="url(#halftone-dot)"/>
    
    <!-- Robot Antenna -->
    <line x1="80" y1="35" x2="80" y2="20" stroke="#0f172a" stroke-width="3.5" stroke-linecap="round"/>
    <circle cx="80" cy="18" r="6" fill="#ef4444" stroke="#0f172a" stroke-width="2"/>
    
    <!-- Robot Head Block -->
    <rect x="42" y="35" width="76" height="60" fill="#38bdf8" stroke="#0f172a" stroke-width="3.5" rx="12"/>
    <!-- Screen Face -->
    <rect x="52" y="45" width="56" height="40" fill="#0f172a" rx="6"/>
    <!-- Expressive Digital Eyes ^_^ -->
    <path d="M 60 66 Q 66 56 72 66" fill="none" stroke="#22c55e" stroke-width="3" stroke-linecap="round"/>
    <path d="M 88 66 Q 94 56 100 66" fill="none" stroke="#22c55e" stroke-width="3" stroke-linecap="round"/>
    
    <!-- Robot Body -->
    <rect x="52" y="102" width="56" height="48" fill="#0284c7" stroke="#0f172a" stroke-width="3" rx="8"/>
    <!-- Power Meter -->
    <circle cx="80" cy="120" r="8" fill="#facc15" stroke="#0f172a" stroke-width="2"/>
</svg>""",

    "quiz_trophy_guardian.svg": f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
    {COMMON_DEFS}
    <!-- Comic Action Burst Behind Trophy -->
    <polygon points="100,10 115,40 145,25 140,55 175,60 155,85 180,110 150,118 155,150 125,138 100,165 75,138 45,150 50,118 20,110 45,85 25,60 60,55 55,25 85,40" fill="#fef08a" stroke="#0f172a" stroke-width="2.5"/>

    <!-- Golden Trophy Cup & Shield -->
    <path d="M 55 45 L 145 45 L 135 110 C 135 135 100 145 100 145 C 100 145 65 135 65 110 Z" fill="#facc15" stroke="#0f172a" stroke-width="3.5" filter="url(#comic-shadow)"/>
    <!-- Handles -->
    <path d="M 55 55 C 30 55 30 90 58 95" fill="none" stroke="#0f172a" stroke-width="4"/>
    <path d="M 145 55 C 170 55 170 90 142 95" fill="none" stroke="#0f172a" stroke-width="4"/>
    
    <!-- Star on Trophy -->
    <polygon points="100,65 106,80 122,80 109,90 114,105 100,95 86,105 91,90 78,80 94,80" fill="#dc2626" stroke="#0f172a" stroke-width="1.5"/>
    
    <!-- Trophy Base -->
    <rect x="75" y="145" width="50" height="15" fill="#334155" stroke="#0f172a" stroke-width="3" rx="2"/>
    <rect x="60" y="160" width="80" height="22" fill="#0f172a" rx="4"/>
    <text x="100" y="176" font-family="'Bangers', cursive" font-size="12" fill="#facc15" text-anchor="middle" letter-spacing="1">GUARDIAN</text>
</svg>"""
}

def generate():
    print(f"Generating {len(ILLUSTRATIONS)} comic SVG illustrations into {OUTPUT_DIR}...")
    for filename, content in ILLUSTRATIONS.items():
        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content.strip())
        print(f"  [CREATED] {filename}")
    print("All illustrations successfully generated!")

if __name__ == '__main__':
    generate()
