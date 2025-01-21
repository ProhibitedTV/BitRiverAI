/**
 * Add event listener to the generate poetry button to trigger poetry generation.
 */
document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('generate-poetry-button').addEventListener('click', generatePoetry);
});

/**
 * Generate poetry based on the selected model and provided inputs.
 */
function generatePoetry() {
    const model = document.getElementById('model-select').value;
    const style = document.getElementById('poetry-style').value;
    const theme = document.getElementById('theme').value;
    const keywords = document.getElementById('keywords').value;
    const tone = document.getElementById('tone').value;
    const length = document.getElementById('length').value;
    const poetryResult = document.getElementById('poetry-result');
    const thinkingIndicator = document.getElementById('thinking-indicator');

    if (theme.trim() === '' && keywords.trim() === '') {
        poetryResult.textContent = 'Please enter a theme or keywords.';
        return;
    }

    const prompt = `Write a ${style} about ${theme} with a ${tone} tone. Include the following keywords: ${keywords}. The poem should be ${length}.`;

    // Show the thinking indicator
    thinkingIndicator.style.display = 'block';
    poetryResult.textContent = ''; // Clear previous result

    console.log('Sending request to generate poetry:', { model, prompt });

    // Send the prompt to the server to generate poetry
    fetch('/generate-poetry', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ model, prompt }),
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Received response:', data);
            // Display the generated poetry
            poetryResult.textContent = data.poetry;
        })
        .catch(err => {
            console.error('Error:', err);
            // Display an error message
            poetryResult.textContent = 'Error: Unable to generate poetry.';
        })
        .finally(() => {
            // Hide the thinking indicator
            thinkingIndicator.style.display = 'none';
        });
}
