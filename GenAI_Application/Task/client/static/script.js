async function sendMessage() {

    const input = document.getElementById("question");
    const question = input.value.trim();

    if (!question) {
        return;
    }

    const chatBox = document.getElementById("chat-box");

    // User Message
    chatBox.innerHTML += `
        <div class="user-message">
            ${question}
        </div>
    `;

    input.value = "";

    // Loading Message
    const loading = document.createElement("div");
    loading.className = "bot-message loading";
    loading.innerHTML = "🤖 Thinking...";

    chatBox.appendChild(loading);
    chatBox.scrollTop = chatBox.scrollHeight;

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/chat",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    question: question
                })
            }
        );

        const data = await response.json();

        loading.remove();

        let html = `<div class="bot-message">`;

        // Error Message
        if (data.error) {

            html += `
                <p>❌ ${data.error}</p>
            `;

        }

        // Normal Bot Message
        else if (data.message) {

            html += `
                <p>${data.message}</p>
            `;

        }

        // SQL Result Table
        else if (data.columns && data.rows) {

            html += `<h4>📊 Result</h4>`;

            html += `<table>`;

            html += `<tr>`;

            data.columns.forEach(col => {
                html += `<th>${col}</th>`;
            });

            html += `</tr>`;

            data.rows.forEach(row => {

                html += `<tr>`;

                row.forEach(value => {
                    html += `<td>${value}</td>`;
                });

                html += `</tr>`;

            });

            html += `</table>`;

        }

        html += `</div>`;

        chatBox.innerHTML += html;
        chatBox.scrollTop = chatBox.scrollHeight;

    }
    catch (error) {

        loading.remove();

        chatBox.innerHTML += `
            <div class="bot-message">
                ❌ Unable to connect to backend server.
            </div>
        `;

        chatBox.scrollTop = chatBox.scrollHeight;

        console.error("Error:", error);

    }
}

// Enter key support
document.addEventListener("DOMContentLoaded", () => {

    const input = document.getElementById("question");

    if (input) {

        input.addEventListener("keypress", function(event) {

            if (event.key === "Enter") {
                sendMessage();
            }

        });

    }

});