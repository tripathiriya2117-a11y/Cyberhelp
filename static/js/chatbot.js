/**
 * CyberHelp AI Chatbot Module (Powered by Gemini API & Offline Safety Engine)
 */

document.addEventListener('DOMContentLoaded', () => {
    const chatBody = document.getElementById('chatBody');
    const chatInput = document.getElementById('chatInput');
    const sendBtn = document.getElementById('sendChatBtn');
    const promptChips = document.querySelectorAll('.prompt-chip');

    if (!chatBody || !chatInput) return;

    // Quick prompt chip click
    promptChips.forEach(chip => {
        chip.addEventListener('click', () => {
            chatInput.value = chip.getAttribute('data-prompt') || chip.textContent.trim();
            sendMessage();
        });
    });

    sendBtn.addEventListener('click', sendMessage);
    chatInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });

    async function sendMessage() {
        const message = chatInput.value.trim();
        if (!message) return;

        // Append User Message
        appendMessage('user', message);
        chatInput.value = '';
        chatInput.focus();

        // Append Loading / Typing indicator
        const typingId = appendTypingIndicator();
        chatBody.scrollTop = chatBody.scrollHeight;

        try {
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    message: message
                })
            });

            const data = await response.json();
            removeTypingIndicator(typingId);

            if (response.ok && data.reply) {
                appendMessage('bot', data.reply, data.source);
            } else {
                appendMessage('bot', data.error || 'Sorry, I encountered an issue processing your request. Please try again.', 'Error');
            }
        } catch (err) {
            removeTypingIndicator(typingId);
            appendMessage('bot', 'Network error. Could not connect to AI safety engine.', 'Error');
        }

        chatBody.scrollTop = chatBody.scrollHeight;
    }

    function appendMessage(role, text, source) {
        const bubble = document.createElement('div');
        bubble.className = 'chat-bubble ' + role;

        let formattedText = formatMarkdown(text);
        
        if (role === 'bot') {
            bubble.innerHTML = `
                <div class="d-flex align-items-center justify-content-between mb-1 pb-1 border-bottom border-light">
                    <span class="fw-bold small text-primary"><i class="bi bi-shield-lock-fill me-1"></i> CyberHelp Advisor</span>
                    ${source ? '<span class="badge bg-light text-secondary border small" style="font-size: 0.68rem;">${source}</span>' : ''}
                </div>
                <div class="chat-text-content">${formattedText}</div>
            `;
        } else {
            bubble.textContent = text;
        }

        chatBody.appendChild(bubble);
        chatBody.scrollTop = chatBody.scrollHeight;
    }

    function appendTypingIndicator() {
        const id = 'typing-' + Date.now();
        const typingEl = document.createElement('div');
        typingEl.id = id;
        typingEl.className = 'chat-bubble bot py-2 px-3';
        typingEl.innerHTML = `
            <div class="d-flex align-items-center gap-2 text-muted small">
                <div class="spinner-grow spinner-grow-sm text-primary" role="status"></div>
                <span>Analyzing threat & consulting cyber safety database...</span>
            </div>
        `;
        chatBody.appendChild(typingEl);
        return id;
    }

    function removeTypingIndicator(id) {
        const el = document.getElementById(id);
        if (el) el.remove();
    }

            function formatMarkdown(md) {
        if (!md) return '';
        // Escape HTML - use proper HTML entities
        let escaped = md
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;');

        // Bold
        escaped = escaped.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
        // Italic
        escaped = escaped.replace(/\*(.*?)\*/g, '<em>$1</em>');
        // Markdown Links
        escaped = escaped.replace(/\[([^\]]+)\]\((https?:\/\/[^)]+)\)/g, '<a href="$2" target="_blank" class="text-primary fw-semibold">$1 <i class="bi bi-box-arrow-up-right small"></i></a>');
        // New lines to br
        escaped = escaped.replace(/
/g, '<br>');
        return escaped;
    }
});
