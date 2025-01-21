document.getElementById('generate-button').addEventListener('click', generateImage);

function generateImage() {
    const prompt = document.getElementById('image-prompt').value;
    const imageResult = document.getElementById('image-result');

    if (prompt.trim() === '') return;

    fetch('/imagegen', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt }),
    })
        .then(response => response.json())
        .then(data => {
            const img = document.createElement('img');
            img.src = data.image_url;
            img.alt = 'Generated Image';
            img.style.maxWidth = '100%';
            imageResult.innerHTML = '';
            imageResult.appendChild(img);
        })
        .catch(err => {
            console.error('Error:', err);
            imageResult.textContent = 'Error: Unable to generate image.';
        });
}
