document.addEventListener('DOMContentLoaded', () => {
    const chatLog = document.getElementById('chat-log');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');
    const modelSelect = document.getElementById('model-select');
    const currentModel = document.getElementById('current-model');

    // Set the current model in the header
    currentModel.textContent = modelSelect.value;

    // Update model display when a new model is selected
    modelSelect.addEventListener('change', () => {
        currentModel.textContent = modelSelect.value;
    });

    // Handle send button click
    sendButton.addEventListener('click', sendMessage);

    // Handle message sending
    function sendMessage() {
        const message = userInput.value.trim();
        const model = modelSelect.value;

        if (message) {
            // Add user message to chat log
            addMessage('user', message);

            // Clear input
            userInput.value = '';

            // Fetch bot response
            fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ model, prompt: message }),
            })
                .then((response) => response.json())
                .then((data) => {
                    addMessage('bot', data.response);
                })
                .catch((error) => {
                    addMessage('bot', 'Error: Unable to fetch response.');
                    console.error(error);
                });
        }
    }

    // Add a message to the chat log
    function addMessage(sender, text) {
        const messageElement = document.createElement('div');
        messageElement.className = `chat-message ${sender}`;
        messageElement.textContent = text;
        chatLog.appendChild(messageElement);
        chatLog.scrollTop = chatLog.scrollHeight; // Scroll to the bottom
    }
});
