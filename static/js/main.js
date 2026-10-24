/**
 * CyberHelp General Application JS & Interactive Comic Safety Quiz Engine
 */

document.addEventListener('DOMContentLoaded', () => {
    // ---------------- Cyber Squad: Scam Buster Challenge Engine ----------------
    const rawDataEl = document.getElementById('quizRawData');
    if (rawDataEl) {
        initCyberSquadQuizEngine(rawDataEl);
    }

    function initCyberSquadQuizEngine(rawDataEl) {
        let questions = [];
        try {
            questions = JSON.parse(rawDataEl.textContent);
        } catch (e) {
            console.error('Failed to parse quiz dataset:', e);
            return;
        }

        if (!questions || questions.length === 0) return;

        // Squad Operatives
        const operatives = [
            {
                name: 'CAPTAIN SHIELD',
                role: 'Senior Defense Strategist',
                img: '/static/img/illustrations/quiz_captain_shield.svg',
                clues: {
                    1: 'Urgent threats with shortened links are the #1 weapon of phishing fraudsters. Keep calm and verify!',
                    4: 'Screen sharing gives attackers full remote access to your device. Never share session codes!',
                    7: 'Real police officers never conduct interrogations or demand fund transfers over video calls!',
                    default: 'Analyze the source and urgency. When in doubt, disconnect and verify independently!'
                }
            },
            {
                name: 'BUSTER BOT',
                role: 'AI Fraud Protocol Enforcer',
                img: '/static/img/illustrations/quiz_buster_bot.svg',
                clues: {
                    2: 'BEEP! Golden rule alert: Entering your UPI PIN is ONLY for SENDING money, never receiving!',
                    5: 'EMERGENCY PROTOCOL: Memorize 1930! Speed within the Golden Hour freezes stolen funds!',
                    default: 'BEEP BOOP! Scanning heuristics: verify payment protocols and emergency response numbers!'
                }
            },
            {
                name: 'AGENT CIPHER',
                role: 'Threat Intelligence Analyst',
                img: '/static/img/illustrations/quiz_agent_cipher.svg',
                clues: {
                    3: 'Look at multi-factor verification as a second digital lock on your personal vault door.',
                    6: 'Length and entropy beat common dictionary patterns every time. Think pass-phrases!',
                    8: 'Inspect the root domain carefully right before the first slash. Look past subdomain tricks!',
                    default: 'Decouple the lure from technical reality. Check domain names and cryptographic seals!'
                }
            }
        ];

        // Educational Explanations per question ID
        const explanations = {
            1: {
                correct: 'Spot on! Legitimate banks never demand urgent KYC via shortened bit.ly links or threaten immediate 2-hour account suspension. Always verify via official banking apps.',
                wrong: 'Alert! Clicking shortened links or sharing Aadhaar/bank numbers with SMS senders leads directly to credential theft and fraudulent account draining.'
            },
            2: {
                correct: 'BEEP BOOP! Correct! Scanning a QR code and entering your UPI PIN ALWAYS DEDUCTS money from your bank account! You NEVER enter a PIN to receive funds!',
                wrong: 'Golden Rule violation: A UPI PIN is exclusively used for authorizing payments OUT of your bank account. Entering your PIN transfers money to the scammer!'
            },
            3: {
                correct: 'Exactly! 2FA acts as a secondary security perimeter. Even if hackers breach your password through data leaks, they cannot enter without the second factor!',
                wrong: 'Negative. 2FA provides defense-in-depth authentication. It stops unauthorized logins even when passwords leak across other websites.'
            },
            4: {
                correct: 'Excellent instincts! Remote desktop apps grant 100% full screen access and mouse control. Fraudsters use them to watch you log in and steal OTPs in real time!',
                wrong: 'Danger! Legitimate technical support or banks will NEVER ask you to install AnyDesk or share 9-digit session codes. This gives them total control of your device!'
            },
            5: {
                correct: 'Affirmative! 1930 is the National Cyber Crime Emergency Helpline! Calling 1930 within the "Golden Hour" triggers instantaneous inter-bank transaction freezing!',
                wrong: 'Incorrect. 100 is police, 108 is ambulance, but 1930 is the dedicated National Cyber Crime Financial Fraud Helpline operated under MHA and I4C!'
            },
            6: {
                correct: 'Outstanding cryptanalysis! "correct-horse-battery-staple-9#Solar" is a long pass-phrase with high entropy, taking automated brute-force supercomputers centuries to crack!',
                wrong: 'Negative. Common predictable patterns like "Password123!", names with years, or digit sequences are cracked within milliseconds by dictionary attack tools.'
            },
            7: {
                correct: 'SPOT ON! Indian law enforcement, CBI, and courts NEVER conduct trials, warrants, or "Digital Arrests" over Skype or WhatsApp video calls. It is 100% extortion!',
                wrong: 'NEVER comply! "Digital Arrest" is a total psychological hoax invented by cyber syndicates. No agency can legally arrest or demand money transfers over video calls.'
            },
            8: {
                correct: 'Target identified! "http://onlinesbi.secure-login-verification.xyz/..." is a classic spoof domain where ".xyz" is the actual top-level domain, and "onlinesbi" is merely a fake subdomain, unencrypted via HTTP!',
                wrong: 'Incorrect. "sbi" and "sbi.co.in" are official legitimate State Bank of India domains. Look closely at the actual domain before the first slash!'
            },
            9: {
                correct: 'Correct! Juice Jacking is an attack where public USB charging stations are modified to siphon private data or inject malware into connected mobile devices.',
                wrong: 'Juice Jacking is a physical hardware exploit where compromised public USB charging cables or kiosks steal data or install spyware.'
            },
            10: {
                correct: 'Spot on! The "Golden Hour" is the critical initial 1 to 2 hour window following online fraud when calling 1930 gives banks the highest chance to freeze stolen funds.',
                wrong: 'In cybercrime, the "Golden Hour" refers to the immediate 1-2 hours after financial fraud when rapid reporting to 1930 can halt money leaving the banking network.'
            }
        };

        // Engine State
        let currentIndex = 0;
        let score = 0;
        let correctCount = 0;
        let userAnswers = {};
        let isAnswered = false;

        // UI Elements
        const missionCounter = document.getElementById('quizMissionCounter');
        const liveScore = document.getElementById('quizLiveScore');
        const progressBar = document.getElementById('quizProgressBar');
        const operativeImg = document.getElementById('quizOperativeImg');
        const operativeName = document.getElementById('quizOperativeName');
        const operativeClue = document.getElementById('quizOperativeClue');
        const questionText = document.getElementById('quizQuestionText');
        const choicesContainer = document.getElementById('quizChoicesContainer');
        const feedbackBanner = document.getElementById('quizFeedbackBanner');
        const feedbackBadge = document.getElementById('feedbackBadge');
        const feedbackPts = document.getElementById('feedbackPts');
        const feedbackExplanation = document.getElementById('feedbackExplanation');
        const nextBtn = document.getElementById('quizNextBtn');
        const finishBtn = document.getElementById('quizFinishBtn');
        const activeMission = document.getElementById('quizActiveMission');
        const victoryScreen = document.getElementById('quizVictoryScreen');

        function renderQuestion() {
            if (currentIndex >= questions.length) {
                submitQuiz();
                return;
            }

            const q = questions[currentIndex];
            isAnswered = false;

            // Update Progress & Counters
            const total = questions.length;
            if (missionCounter) {
                const caseNum = String(currentIndex + 1).padStart(2, '0');
                const totalNum = String(total).padStart(2, '0');
                missionCounter.textContent = `CASE FILE ${caseNum} / ${totalNum}`;
            }

            if (progressBar) {
                const pct = Math.round(((currentIndex + 1) / total) * 100);
                progressBar.style.width = `${pct}%`;
            }

            // Operative assignment (rotates through operatives)
            const op = operatives[currentIndex % operatives.length];
            if (operativeImg) operativeImg.src = op.img;
            if (operativeName) operativeName.textContent = op.name;
            if (operativeClue) {
                const clue = (op.clues && op.clues[q.id]) || op.clues.default;
                operativeClue.textContent = `"${clue}"`;
            }

            // Question Text
            if (questionText) {
                questionText.textContent = q.text;
            }

            // Render Choices
            if (choicesContainer) {
                choicesContainer.innerHTML = '';
                const opts = ['A', 'B', 'C', 'D'];
                opts.forEach(letter => {
                    const text = q.options[letter] || '';
                    if (!text) return;

                    const card = document.createElement('div');
                    card.className = 'quiz-choice-card';
                    card.setAttribute('role', 'button');
                    card.setAttribute('tabindex', '0');
                    card.setAttribute('data-opt', letter);

                    card.innerHTML = `
                        <div class="choice-letter-badge">${letter}</div>
                        <div class="choice-text-content">${text}</div>
                        <i class="bi choice-status-icon ms-auto fs-5"></i>
                    `;

                    // Event listener
                    card.addEventListener('click', () => handleSelectOption(letter, card, q));
                    card.addEventListener('keydown', (e) => {
                        if (e.key === 'Enter' || e.key === ' ') {
                            e.preventDefault();
                            handleSelectOption(letter, card, q);
                        }
                    });

                    choicesContainer.appendChild(card);
                });
            }

            // Reset Feedback Banner and Buttons
            if (feedbackBanner) feedbackBanner.classList.add('d-none');
            if (nextBtn) nextBtn.classList.add('d-none');
            if (finishBtn) finishBtn.classList.add('d-none');
        }

        function handleSelectOption(selectedOpt, selectedCard, q) {
            if (isAnswered) return;
            isAnswered = true;

            const isCorrect = (selectedOpt.toUpperCase() === q.correct.toUpperCase());
            userAnswers[String(q.id)] = selectedOpt;

            // Lock all choices
            const allCards = choicesContainer.querySelectorAll('.quiz-choice-card');
            allCards.forEach(c => {
                c.classList.add('locked');
                const opt = c.getAttribute('data-opt');
                if (opt.toUpperCase() === q.correct.toUpperCase()) {
                    c.classList.add('correct-ans');
                    const icon = c.querySelector('.choice-status-icon');
                    if (icon) icon.className = 'bi bi-check-circle-fill text-success ms-auto fs-5';
                }
            });

            if (isCorrect) {
                score += 100;
                correctCount += 1;
                selectedCard.classList.add('selected');
                showFeedback(true, q);
            } else {
                selectedCard.classList.add('selected', 'wrong-ans');
                const icon = selectedCard.querySelector('.choice-status-icon');
                if (icon) icon.className = 'bi bi-x-circle-fill text-danger ms-auto fs-5';
                showFeedback(false, q);
            }

            if (liveScore) {
                liveScore.innerHTML = `<i class="bi bi-lightning-charge-fill me-1"></i>SCORE: ${score} PTS`;
            }

            // Show appropriate navigation button
            const total = questions.length;
            if (currentIndex < total - 1) {
                if (nextBtn) {
                    nextBtn.classList.remove('d-none');
                    nextBtn.focus();
                }
            } else {
                if (finishBtn) {
                    finishBtn.classList.remove('d-none');
                    finishBtn.focus();
                }
            }
        }

        function showFeedback(isCorrect, q) {
            if (!feedbackBanner) return;

            const explanationData = explanations[q.id] || {
                correct: 'Mission accomplished! You correctly identified the secure defense protocol for this threat scenario.',
                wrong: 'Threat detected! That choice exposes your credentials or funds to risk. Remember the golden cyber defense rule.'
            };

            feedbackBanner.classList.remove('d-none', 'feedback-success', 'feedback-danger');

            if (isCorrect) {
                feedbackBanner.classList.add('feedback-success');
                if (feedbackBadge) {
                    feedbackBadge.className = 'feedback-badge bg-success text-white border-dark';
                    feedbackBadge.innerHTML = '<i class="bi bi-check-circle-fill"></i> CORRECT PROTOCOL';
                }
                if (feedbackPts) {
                    feedbackPts.className = 'badge bg-success text-white font-monospace border border-dark';
                    feedbackPts.textContent = '+100 PTS';
                }
                if (feedbackExplanation) {
                    feedbackExplanation.textContent = explanationData.correct;
                }
            } else {
                feedbackBanner.classList.add('feedback-danger');
                if (feedbackBadge) {
                    feedbackBadge.className = 'feedback-badge bg-danger text-white border-dark';
                    feedbackBadge.innerHTML = '<i class="bi bi-shield-slash-fill"></i> THREAT DETECTED';
                }
                if (feedbackPts) {
                    feedbackPts.className = 'badge bg-danger text-white font-monospace border border-dark';
                    feedbackPts.textContent = '+0 PTS';
                }
                if (feedbackExplanation) {
                    feedbackExplanation.textContent = explanationData.wrong;
                }
            }
        }

        // Advance to next question
        if (nextBtn) {
            nextBtn.addEventListener('click', () => {
                if (currentIndex < questions.length - 1) {
                    currentIndex++;
                    renderQuestion();
                }
            });
        }

        // Finish mission and submit answers
        if (finishBtn) {
            finishBtn.addEventListener('click', () => {
                submitQuiz();
            });
        }

        // Global Keyboard Navigation (1-4, A-D, Enter)
        document.addEventListener('keydown', (e) => {
            // Ignore if active element is an input or textarea
            const tag = document.activeElement ? document.activeElement.tagName.toLowerCase() : '';
            if (tag === 'input' || tag === 'textarea' || tag === 'select') return;

            // Only run if active mission is visible
            if (!activeMission || activeMission.classList.contains('d-none')) return;

            const key = e.key.toUpperCase();

            if (!isAnswered) {
                let chosenLetter = null;
                if (key === '1' || key === 'A') chosenLetter = 'A';
                else if (key === '2' || key === 'B') chosenLetter = 'B';
                else if (key === '3' || key === 'C') chosenLetter = 'C';
                else if (key === '4' || key === 'D') chosenLetter = 'D';

                if (chosenLetter && choicesContainer) {
                    const card = choicesContainer.querySelector(`[data-opt="${chosenLetter}"]`);
                    if (card) {
                        e.preventDefault();
                        handleSelectOption(chosenLetter, card, questions[currentIndex]);
                    }
                }
            } else {
                if (e.key === 'Enter') {
                    e.preventDefault();
                    if (nextBtn && !nextBtn.classList.contains('d-none')) {
                        nextBtn.click();
                    } else if (finishBtn && !finishBtn.classList.contains('d-none')) {
                        finishBtn.click();
                    }
                }
            }
        });

        // Submit quiz results to backend API
        async function submitQuiz() {
            if (finishBtn) {
                finishBtn.disabled = true;
                finishBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span> TRANSMITTING INTEL...';
            }

            try {
                const response = await fetch('/api/quiz/submit', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ answers: userAnswers })
                });

                const data = await response.json();
                if (!response.ok) {
                    alert(data.error || 'Failed to submit quiz.');
                    return;
                }

                renderVictoryScreen(data);
            } catch (err) {
                console.error('Quiz submission error:', err);
                alert('An error occurred submitting the quiz. Please try again.');
            } finally {
                if (finishBtn) {
                    finishBtn.disabled = false;
                    finishBtn.innerHTML = 'TRANSMIT DOSSIER <i class="bi bi-send-check-fill ms-1"></i>';
                }
            }
        }

        function renderVictoryScreen(data) {
            if (!victoryScreen || !activeMission) return;

            activeMission.classList.add('d-none');
            victoryScreen.classList.remove('d-none');

            // Rank Title assignment
            const rankBanner = document.getElementById('quizRankBanner');
            const scoreNum = document.getElementById('quizFinalScoreNumber');
            const scorePct = document.getElementById('quizFinalScorePercent');
            const progBar = document.getElementById('quizFinalProgressBar');
            const evalText = document.getElementById('quizFinalEvaluationText');
            const breakdown = document.getElementById('quizDetailedBreakdown');

            const pct = data.percentage;
            let rankTitle = 'RECRUIT IN TRAINING';
            let rankColor = '#dc2626';

            if (pct >= 90) {
                rankTitle = 'SUPREME CYBER GUARDIAN';
                rankColor = '#16a34a';
            } else if (pct >= 80) {
                rankTitle = 'SENIOR THREAT HUNTER';
                rankColor = '#0284c7';
            } else if (pct >= 60) {
                rankTitle = 'CYBER SQUAD CADET';
                rankColor = '#ca8a04';
            }

            if (rankBanner) {
                rankBanner.textContent = rankTitle;
                rankBanner.style.borderColor = rankColor;
            }

            if (scoreNum) scoreNum.textContent = `${data.score} / ${data.total}`;
            if (scorePct) scorePct.textContent = `${pct}% THREAT ELIMINATION`;
            if (progBar) {
                progBar.style.width = `${pct}%`;
                progBar.className = `progress-bar bg-${data.badge}`;
            }
            if (evalText) evalText.textContent = data.evaluation;

            // Render breakdown
            if (breakdown && data.results) {
                breakdown.innerHTML = '';
                data.results.forEach((item, index) => {
                    const row = document.createElement('div');
                    row.className = `scam-sequence-step mb-3 ${item.is_correct ? 'border-success' : 'border-danger'}`;
                    row.style.background = item.is_correct ? '#f0fdf4' : '#fef2f2';

                    const userChoiceText = item.user_choice ? `${item.user_choice}: ${item.options[item.user_choice] || ''}` : 'No Choice';
                    const correctChoiceText = `${item.correct_option}: ${item.options[item.correct_option] || ''}`;

                    row.innerHTML = `
                        <div class="d-flex align-items-center justify-content-between mb-2">
                            <span class="badge ${item.is_correct ? 'bg-success' : 'bg-danger'} font-comic fs-6">
                                ${item.is_correct ? '✓ CASE SOLVED (+100 PTS)' : '✗ SECURITY BREACH (0 PTS)'}
                            </span>
                            <span class="badge bg-dark text-white font-monospace">CASE #${String(index + 1).padStart(2, '0')}</span>
                        </div>
                        <h6 class="fw-bold text-dark mb-2">${item.question_text}</h6>
                        <div class="small">
                            <div class="${item.is_correct ? 'text-success fw-bold' : 'text-danger fw-semibold'}">
                                <strong>Your Decision:</strong> ${userChoiceText}
                            </div>
                            ${!item.is_correct ? `
                                <div class="text-success fw-bold mt-1">
                                    <strong>Safe Protocol:</strong> ${correctChoiceText}
                                </div>
                            ` : ''}
                        </div>
                    `;
                    breakdown.appendChild(row);
                });
            }

            victoryScreen.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }

        // Start mission engine
        renderQuestion();
    }

    // ---------------- Live Filter on Scam & Awareness Cards ----------------
    const searchCardsInput = document.getElementById('liveSearchCards');
    if (searchCardsInput) {
        searchCardsInput.addEventListener('input', () => {
            const query = searchCardsInput.value.toLowerCase().trim();
            const cards = document.querySelectorAll('.filterable-card');
            let visibleCount = 0;

            cards.forEach(card => {
                const title = card.getAttribute('data-title') || '';
                const desc = card.getAttribute('data-desc') || '';
                const category = card.getAttribute('data-category') || '';
                
                if (title.includes(query) || desc.includes(query) || category.includes(query)) {
                    card.style.display = '';
                    visibleCount++;
                } else {
                    card.style.display = 'none';
                }
            });

            // Handle dynamic empty state for client-side search
            let emptyState = document.getElementById('scamsDynamicEmptyState');
            if (visibleCount === 0 && query.length > 0) {
                if (!emptyState) {
                    emptyState = document.createElement('div');
                    emptyState.id = 'scamsDynamicEmptyState';
                    emptyState.className = 'col-12 text-center py-5';
                    emptyState.innerHTML = `
                        <div class="p-5 border border-3 border-dark rounded-4 bg-light shadow" style="max-width: 550px; margin: 0 auto;">
                            <i class="bi bi-search fs-1 text-danger"></i>
                            <h3 class="comic-title text-dark mt-3">NO CRIMES MATCH THIS SEARCH!</h3>
                            <p class="text-muted">No documented case files match &ldquo;${query}&rdquo;.</p>
                            <button type="button" class="btn-comic-danger mt-2" onclick="document.getElementById('liveSearchCards').value=''; document.getElementById('liveSearchCards').dispatchEvent(new Event('input'));">
                                Clear Search Filter
                            </button>
                        </div>
                    `;
                    const grid = document.getElementById('scamsGrid');
                    if (grid) grid.appendChild(emptyState);
                } else {
                    emptyState.style.display = '';
                }
            } else if (emptyState) {
                emptyState.style.display = 'none';
            }
        });
    }

    // ---------------- Live Filter on FAQ Dialogue Panels ----------------
    const faqSearchInput = document.getElementById('faqSearchInput');
    if (faqSearchInput) {
        faqSearchInput.addEventListener('input', () => {
            const query = faqSearchInput.value.toLowerCase().trim();
            const faqItems = document.querySelectorAll('.faq-panel-item');
            const noResultsEl = document.getElementById('faqNoResults');
            let visibleFaqs = 0;

            faqItems.forEach(item => {
                const question = item.getAttribute('data-question') || '';
                const answer = item.getAttribute('data-answer') || '';

                if (question.includes(query) || answer.includes(query)) {
                    item.style.display = '';
                    visibleFaqs++;
                } else {
                    item.style.display = 'none';
                }
            });

            if (noResultsEl) {
                if (visibleFaqs === 0 && query.length > 0) {
                    noResultsEl.classList.remove('d-none');
                } else {
                    noResultsEl.classList.add('d-none');
                }
            }
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
