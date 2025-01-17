function sendMessage() {
    const model = document.getElementById('model-select').value;
    const userInput = document.getElementById('user-input').value;
    const chatLog = document.getElementById('chat-log');

    fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ model, prompt: userInput }),
    })
        .then(response => response.json())
        .then(data => {
            const userMessage = document.createElement('div');
            userMessage.textContent = `You: ${userInput}`;
            userMessage.classList.add('chat-message');
            chatLog.appendChild(userMessage);

            const aiMessage = document.createElement('div');
            aiMessage.textContent = `AI: ${data.response}`;
            aiMessage.classList.add('chat-message');
            chatLog.appendChild(aiMessage);

            chatLog.scrollTop = chatLog.scrollHeight;
            document.getElementById('user-input').value = '';
        })
        .catch(err => console.error('Error:', err));
}
