/**
 * Password Strength Checker & Entropy Calculator (Pure JavaScript)
 */

document.addEventListener('DOMContentLoaded', () => {
    const passwordInput = document.getElementById('pwdInput');
    const toggleBtn = document.getElementById('togglePwdVisibility');
    if (!passwordInput) return;

    const strengthBar = document.getElementById('strengthBar');
    const strengthLabel = document.getElementById('strengthLabel');
    const entropyValue = document.getElementById('entropyValue');
    const crackTimeValue = document.getElementById('crackTimeValue');
    
    const reqLength = document.getElementById('reqLength');
    const reqUpper = document.getElementById('reqUpper');
    const reqLower = document.getElementById('reqLower');
    const reqNumber = document.getElementById('reqNumber');
    const reqSpecial = document.getElementById('reqSpecial');
    const patternWarning = document.getElementById('patternWarning');

    // Toggle Visibility
    if (toggleBtn) {
        toggleBtn.addEventListener('click', () => {
            const isPassword = passwordInput.type === 'password';
            passwordInput.type = isPassword ? 'text' : 'password';
            toggleBtn.innerHTML = isPassword ? '<i class="bi bi-eye-slash"></i>' : '<i class="bi bi-eye"></i>';
        });
    }

    passwordInput.addEventListener('input', () => {
        const pwd = passwordInput.value;
        analyzePassword(pwd);
    });

    function analyzePassword(pwd) {
        if (!pwd) {
            strengthBar.style.width = '0%';
            strengthBar.className = 'strength-meter-progress';
            strengthLabel.textContent = 'Enter a password';
            strengthLabel.className = 'fw-bold text-muted';
            entropyValue.textContent = '0 bits';
            crackTimeValue.textContent = 'Instant';
            resetRequirements();
            patternWarning.classList.add('d-none');
            return;
        }

        // Requirements Analysis
        const hasUpper = /[A-Z]/.test(pwd);
        const hasLower = /[a-z]/.test(pwd);
        const hasNumber = /[0-9]/.test(pwd);
        const hasSpecial = /[^A-Za-z0-9]/.test(pwd);
        const isMinLength = pwd.length >= 12;

        updateRequirementItem(reqLength, isMinLength);
        updateRequirementItem(reqUpper, hasUpper);
        updateRequirementItem(reqLower, hasLower);
        updateRequirementItem(reqNumber, hasNumber);
        updateRequirementItem(reqSpecial, hasSpecial);

        // Character Pool Size (R)
        let poolSize = 0;
        if (hasLower) poolSize += 26;
        if (hasUpper) poolSize += 26;
        if (hasNumber) poolSize += 10;
        if (hasSpecial) poolSize += 33;

        // Entropy Calculation: E = L * log2(R)
        let entropy = 0;
        if (poolSize > 0 && pwd.length > 0) {
            entropy = Math.round(pwd.length * (Math.log(poolSize) / Math.log(2)));
        }

        // Common weak pattern checks
        const commonWeakWords = ['password', '123456', 'admin', 'qwerty', 'welcome', 'iloveyou', 'india', 'pass@123', 'test', 'login'];
        const isCommon = commonWeakWords.some(w => pwd.toLowerCase().includes(w));
        const isRepeating = /(.)\1{3,}/.test(pwd);

        if (isCommon || isRepeating) {
            patternWarning.classList.remove('d-none');
            patternWarning.textContent = isCommon ? '⚠️ Warning: Contains a known dictionary word or common sequence.' : '⚠️ Warning: Contains repeated consecutive characters.';
            entropy = Math.max(10, entropy - 25);
        } else {
            patternWarning.classList.add('d-none');
        }

        entropyValue.textContent = `${entropy} bits`;

        // Estimated Crack Time (Assuming 10^10 hashes/sec for offline brute force)
        const totalCombinations = Math.pow(poolSize, pwd.length);
        const secondsToCrack = totalCombinations / 1e10;
        crackTimeValue.textContent = formatCrackTime(secondsToCrack);

        // Visual Score Rating
        let scorePercent = 0;
        let ratingText = '';
        let colorClass = '';

        if (entropy < 28) {
            scorePercent = 20;
            ratingText = 'Very Weak';
            colorClass = 'bg-danger';
        } else if (entropy < 45) {
            scorePercent = 40;
            ratingText = 'Weak';
            colorClass = 'bg-danger';
        } else if (entropy < 65) {
            scorePercent = 65;
            ratingText = 'Fair / Moderate';
            colorClass = 'bg-warning';
        } else if (entropy < 85) {
            scorePercent = 85;
            ratingText = 'Strong';
            colorClass = 'bg-primary';
        } else {
            scorePercent = 100;
            ratingText = 'Very Strong / Cryptographically Resilient';
            colorClass = 'bg-success';
        }

        strengthBar.style.width = `${scorePercent}%`;
        strengthBar.className = `strength-meter-progress ${colorClass}`;
        strengthLabel.textContent = ratingText;
        strengthLabel.className = `fw-bold ${colorClass.replace('bg-', 'text-')}`;
    }

    function updateRequirementItem(el, isValid) {
        if (!el) return;
        const icon = el.querySelector('i');
        if (isValid) {
            el.className = 'text-success small d-flex align-items-center gap-1 mb-1';
            icon.className = 'bi bi-check-circle-fill';
        } else {
            el.className = 'text-muted small d-flex align-items-center gap-1 mb-1';
            icon.className = 'bi bi-circle';
        }
    }

    function resetRequirements() {
        [reqLength, reqUpper, reqLower, reqNumber, reqSpecial].forEach(el => {
            if (el) {
                el.className = 'text-muted small d-flex align-items-center gap-1 mb-1';
                const icon = el.querySelector('i');
                if (icon) icon.className = 'bi bi-circle';
            }
        });
    }

    function formatCrackTime(seconds) {
        if (seconds < 0.1) return 'Instant (< 0.1 sec)';
        if (seconds < 60) return `${Math.round(seconds)} seconds`;
        if (seconds < 3600) return `${Math.round(seconds / 60)} minutes`;
        if (seconds < 86400) return `${Math.round(seconds / 3600)} hours`;
        if (seconds < 31536000) return `${Math.round(seconds / 86400)} days`;
        if (seconds < 31536000 * 100) return `${Math.round(seconds / 31536000)} years`;
        if (seconds < 31536000 * 1e6) return `${Math.round(seconds / (31536000 * 1e3))} thousand years`;
        return 'Centuries / Billions of Years';
    }
});
