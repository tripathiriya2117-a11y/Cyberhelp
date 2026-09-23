/**
 * CyberHelp General Application JS & Interactive Safety Quiz Engine
 */

document.addEventListener('DOMContentLoaded', () => {
    // ---------------- Quiz Engine ----------------
    const quizForm = document.getElementById('cyberQuizForm');
    const quizSubmitBtn = document.getElementById('submitQuizBtn');
    const quizResultCard = document.getElementById('quizResultSection');

    if (quizForm && quizSubmitBtn) {
        quizForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const formData = new FormData(quizForm);
            const answers = {};
            
            for (let [key, value] of formData.entries()) {
                if (key.startsWith('q_')) {
                    const qId = key.replace('q_', '');
                    answers[qId] = value;
                }
            }

            quizSubmitBtn.disabled = true;
            quizSubmitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Evaluating Score...';

            try {
                const response = await fetch('/api/quiz/submit', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ answers })
                });

                const data = await response.json();
                if (!response.ok) {
                    alert(data.error || 'Failed to submit quiz.');
                    return;
                }

                renderQuizResults(data);
            } catch (err) {
                console.error('Quiz submission error:', err);
                alert('An error occurred submitting the quiz. Please try again.');
            } finally {
                quizSubmitBtn.disabled = false;
                quizSubmitBtn.innerHTML = '<i class="bi bi-send-check me-2"></i> Submit & Check Answers';
            }
        });
    }

    function renderQuizResults(data) {
        if (!quizResultCard) return;

        quizResultCard.classList.remove('d-none');

        const scoreNumber = document.getElementById('quizScoreNumber');
        const scorePercent = document.getElementById('quizScorePercentage');
        const evalText = document.getElementById('quizEvaluationText');
        const scoreProgressBar = document.getElementById('quizScoreProgressBar');
        const breakdownContainer = document.getElementById('quizDetailedBreakdown');

        scoreNumber.textContent = `${data.score} / ${data.total}`;
        scorePercent.textContent = `${data.percentage}%`;
        evalText.textContent = data.evaluation;
        
        scoreProgressBar.style.width = `${data.percentage}%`;
        scoreProgressBar.className = `progress-bar bg-${data.badge}`;

        // Render Question Breakdown
        if (breakdownContainer && data.results) {
            breakdownContainer.innerHTML = '';
            data.results.forEach((item, index) => {
                const itemDiv = document.createElement('div');
                itemDiv.className = `p-3 mb-3 border rounded-3 ${item.is_correct ? 'bg-success-subtle border-success' : 'bg-danger-subtle border-danger'}`;
                
                const userChoiceText = item.user_choice ? `${item.user_choice}: ${item.options[item.user_choice] || ''}` : 'No Answer Selected';
                const correctChoiceText = `${item.correct_option}: ${item.options[item.correct_option] || ''}`;

                itemDiv.innerHTML = `
                    <div class="d-flex align-items-center justify-content-between mb-2">
                        <h6 class="mb-0 fw-bold text-dark">Q${index + 1}: ${item.question_text}</h6>
                        <span class="badge ${item.is_correct ? 'bg-success' : 'bg-danger'}">${item.is_correct ? '✓ Correct (+1)' : '✗ Incorrect (0)'}</span>
                    </div>
                    <div class="small mt-2">
                        <div class="${item.is_correct ? 'text-success fw-bold' : 'text-danger'}">
                            <strong>Your Answer:</strong> ${userChoiceText}
                        </div>
                        ${!item.is_correct ? `
                            <div class="text-success fw-bold mt-1">
                                <strong>Correct Answer:</strong> ${correctChoiceText}
                            </div>
                        ` : ''}
                    </div>
                `;
                breakdownContainer.appendChild(itemDiv);
            });
        }

        quizResultCard.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    // ---------------- Live Filter on Cards ----------------
    const searchCardsInput = document.getElementById('liveSearchCards');
    if (searchCardsInput) {
        searchCardsInput.addEventListener('input', () => {
            const query = searchCardsInput.value.toLowerCase().trim();
            const cards = document.querySelectorAll('.filterable-card');

            cards.forEach(card => {
                const title = card.getAttribute('data-title') || '';
                const desc = card.getAttribute('data-desc') || '';
                const category = card.getAttribute('data-category') || '';
                
                if (title.includes(query) || desc.includes(query) || category.includes(query)) {
                    card.style.display = '';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    }

    // Auto-dismiss Flash Alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
            if (bsAlert) bsAlert.close();
        }, 5000);
    });
});
