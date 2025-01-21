function sendMessage() {
    const model = document.getElementById('model-select').value;
    const userInput = document.getElementById('user-input').value;
    const chatLog = document.getElementById('chat-log');
    const thinkingIndicator = document.getElementById('thinking-indicator');

    if (userInput.trim() === '') return;

    const userMessage = document.createElement('div');
    userMessage.textContent = `You: ${userInput}`;
    userMessage.classList.add('chat-message');
    chatLog.appendChild(userMessage);

    thinkingIndicator.style.display = 'block';

    fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ model, prompt: userInput }),
    })
        .then(response => response.json())
        .then(data => {
            const aiMessage = document.createElement('div');
            aiMessage.textContent = `AI: ${data.response}`;
            aiMessage.classList.add('chat-message');
            chatLog.appendChild(aiMessage);

            chatLog.scrollTop = chatLog.scrollHeight;
            document.getElementById('user-input').value = '';
        })
        .catch(err => {
            console.error('Error:', err);
            const errorMessage = document.createElement('div');
            errorMessage.textContent = 'Error: Unable to get response from AI.';
            errorMessage.classList.add('chat-message', 'error-message');
            chatLog.appendChild(errorMessage);
        })
        .finally(() => {
            thinkingIndicator.style.display = 'none';
        });
}

document.getElementById('send-button').addEventListener('click', sendMessage);
document.getElementById('user-input').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});
