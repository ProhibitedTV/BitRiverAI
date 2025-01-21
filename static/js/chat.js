/**
 * Send a message to the AI model and display the response.
 */
function sendMessage() {
    const model = document.getElementById('model-select').value;
    const userInput = document.getElementById('user-input').value;
    const chatLog = document.getElementById('chat-log');
    const thinkingIndicator = document.getElementById('thinking-indicator');

    if (userInput.trim() === '') return;

    // Display the user's message in the chat log
    const userMessage = document.createElement('div');
    userMessage.textContent = `You: ${userInput}`;
    userMessage.classList.add('chat-message');
    chatLog.appendChild(userMessage);

    // Show the thinking indicator
    thinkingIndicator.style.display = 'block';

    // Send the user's message to the server
    fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ model, prompt: userInput }),
    })
        .then(response => response.json())
        .then(data => {
            // Display the AI's response in the chat log
            const aiMessage = document.createElement('div');
            aiMessage.textContent = `AI: ${data.response}`;
            aiMessage.classList.add('chat-message');
            chatLog.appendChild(aiMessage);

            // Scroll to the bottom of the chat log
            chatLog.scrollTop = chatLog.scrollHeight;
            document.getElementById('user-input').value = '';
        })
        .catch(err => {
            console.error('Error:', err);
            // Display an error message in the chat log
            const errorMessage = document.createElement('div');
            errorMessage.textContent = 'Error: Unable to get response from AI.';
            errorMessage.classList.add('chat-message', 'error-message');
            chatLog.appendChild(errorMessage);
        })
        .finally(() => {
            // Hide the thinking indicator
            thinkingIndicator.style.display = 'none';
        });
}

// Add event listener to the send button
document.getElementById('send-button').addEventListener('click', sendMessage);

// Add event listener to the user input field to send message on Enter key press
document.getElementById('user-input').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});
