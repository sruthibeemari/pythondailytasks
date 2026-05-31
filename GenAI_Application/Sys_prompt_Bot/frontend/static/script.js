async function sendMessage() {
    const questionInput = document.getElementById("question");
    const question = questionInput.value.trim();

    if (!question) return;

    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `
        <div class="user">${escapeHtml(question)}</div>
    `;
    questionInput.value = "";

    const loadingDiv = document.createElement("div");
    loadingDiv.className = "bot loading";
    loadingDiv.innerHTML = `
        <div class="loading-text">
            Thinking<span class="dot dot1">.</span><span class="dot dot2">.</span><span class="dot dot3">.</span>
        </div>
    `;
    chatBox.appendChild(loadingDiv);
    chatBox.scrollTop = chatBox.scrollHeight;

    try {
        const response = await fetch("http://127.0.0.1:8000/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question })
        });

        const data = await response.json();
        const botReply = formatBotReply(data);

        chatBox.removeChild(loadingDiv);
        chatBox.innerHTML += `
            <div class="bot">
                ${botReply}
            </div>
        `;
        chatBox.scrollTop = chatBox.scrollHeight;
    } catch (error) {
        chatBox.removeChild(loadingDiv);
        chatBox.innerHTML += `
            <div class="bot">
                Unable to connect to backend.
            </div>
        `;
        chatBox.scrollTop = chatBox.scrollHeight;
        console.error(error);
    }
}

function formatBotReply(data) {

    if (data.error) {
        return `
            <div class="error-card">
                <h3>❌ Error</h3>
                <p>${escapeHtml(data.error)}</p>
            </div>
        `;
    }

    let botReply = `<div class="mentor-response">`;

    if (data.answer) {
        botReply += `
            <div class="response-section">
                <h3>📘 Answer</h3>
                <p>${escapeHtml(data.answer)}</p>
            </div>
        `;
    }

    if (
        data.key_points &&
        Array.isArray(data.key_points) &&
        data.key_points.length > 0
    ) {
        botReply += `
            <div class="response-section">
                <h3>📌 Key Points</h3>
                <ul class="points-list">
        `;

        data.key_points.forEach(point => {
            botReply += `
                <li>${escapeHtml(point)}</li>
            `;
        });

        botReply += `
                </ul>
            </div>
        `;
    }

    if (data.example) {
        botReply += `
            <div class="response-section">
                <h3>💻 Example</h3>
                <pre class="code-block">${escapeHtml(data.example)}</pre>
            </div>
        `;
    }

    if (data.next_step) {
        botReply += `
            <div class="response-section">
                <h3>🚀 Next Step</h3>
                <p>${escapeHtml(data.next_step)}</p>
            </div>
        `;
    }

    botReply += `</div>`;

    return botReply;
}

function escapeHtml(text) {
    if (typeof text !== "string") {
        return text;
    }
    return text
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}
