/**
 * Add event listener to the generate button to trigger image generation.
 */
document.getElementById('generate-button').addEventListener('click', generateImage);

/**
 * Generate an image based on the provided prompt.
 */
function generateImage() {
    const prompt = document.getElementById('image-prompt').value;
    const imageResult = document.getElementById('image-result');

    if (prompt.trim() === '') return;

    // Send the prompt to the server to generate an image
    fetch('/imagegen', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt }),
    })
        .then(response => response.json())
        .then(data => {
            // Display the generated image
            const img = document.createElement('img');
            img.src = data.image_url;
            img.alt = 'Generated Image';
            img.style.maxWidth = '100%';
            imageResult.innerHTML = '';
            imageResult.appendChild(img);
        })
        .catch(err => {
            console.error('Error:', err);
            // Display an error message
            imageResult.textContent = 'Error: Unable to generate image.';
        });
}