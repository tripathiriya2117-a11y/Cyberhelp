/**
 * URL Safety Checker & Heuristic Scanner (Client-Side & API)
 */

document.addEventListener('DOMContentLoaded', () => {
    const urlForm = document.getElementById('urlCheckerForm');
    const urlInput = document.getElementById('urlInput');
    const analyzeBtn = document.getElementById('analyzeUrlBtn');
    const resultBox = document.getElementById('urlResultBox');

    if (!urlForm || !urlInput) return;

    urlForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const rawUrl = urlInput.value.trim();
        if (!rawUrl) return;

        // Loading State
        analyzeBtn.disabled = true;
        analyzeBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Scanning...';
        resultBox.classList.add('d-none');

        try {
            const res = await fetch('/api/check-url', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ url: rawUrl })
            });
            const data = await res.json();

            if (!res.ok) {
                alert(data.error || 'Failed to analyze URL');
                return;
            }

            renderResults(data);
        } catch (err) {
            console.error('URL check error:', err);
            alert('Failed to connect to scanner service. Please check your connection.');
        } finally {
            analyzeBtn.disabled = false;
            analyzeBtn.innerHTML = '<i class="bi bi-shield-check me-1"></i> Analyze URL';
        }
    });

    function renderResults(data) {
        resultBox.classList.remove('d-none');
        
        const verdictBadge = document.getElementById('urlVerdictBadge');
        const verdictTitle = document.getElementById('urlVerdictTitle');
        const riskBar = document.getElementById('urlRiskBar');
        const riskScoreText = document.getElementById('urlRiskScoreText');
        const hostDisplay = document.getElementById('urlHostDisplay');
        const recommendationText = document.getElementById('urlRecommendation');
        const flagsContainer = document.getElementById('urlFlagsList');

        verdictBadge.className = `badge bg-${data.badge_class} px-3 py-2 fs-6`;
        verdictBadge.textContent = data.verdict;
        verdictTitle.textContent = `Target Domain: ${data.hostname || 'N/A'}`;
        hostDisplay.textContent = data.url;

        riskBar.style.width = `${data.risk_score}%`;
        riskBar.className = `progress-bar bg-${data.badge_class}`;
        riskScoreText.textContent = `${data.risk_score}/100`;

        recommendationText.textContent = data.recommendation;

        flagsContainer.innerHTML = '';
        if (data.flags && data.flags.length > 0) {
            data.flags.forEach(flag => {
                const item = document.createElement('div');
                item.className = `alert alert-${flag.type} d-flex align-items-start gap-2 py-2 px-3 mb-2 small`;
                item.innerHTML = `
                    <i class="bi bi-exclamation-triangle-fill fs-5 mt-1"></i>
                    <div>
                        <strong>${flag.title}:</strong> ${flag.detail}
                    </div>
                `;
                flagsContainer.appendChild(item);
            });
        } else {
            const safeItem = document.createElement('div');
            safeItem.className = 'alert alert-success d-flex align-items-center gap-2 py-2 px-3 mb-0 small';
            safeItem.innerHTML = `
                <i class="bi bi-check-circle-fill fs-5"></i>
                <div>
                    <strong>No malicious heuristics identified.</strong> The link structure conforms to standard web naming patterns.
                </div>
            `;
            flagsContainer.appendChild(safeItem);
        }

        resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
});
