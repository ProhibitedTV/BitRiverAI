document.addEventListener('DOMContentLoaded', () => {
    // Select the matrix background container
    const matrix = document.querySelector('.matrix-bg');

    // Get the dimensions of the window
    const width = window.innerWidth;
    const height = window.innerHeight;

    // Number of falling characters to generate
    const numChars = 150;

    // Generate matrix characters
    for (let i = 0; i < numChars; i++) {
        const span = document.createElement('span'); // Create a span element
        span.textContent = Math.random() > 0.5 ? '0' : '1'; // Randomly choose between '0' and '1'

        // Position the span randomly on the x-axis and set its animation properties
        span.style.left = Math.random() * width + 'px';
        span.style.top = Math.random() * height + 'px';
        span.style.animationDuration = Math.random() * 3 + 2 + 's'; // Random fall speed
        span.style.animationDelay = Math.random() * 5 + 's'; // Random start delay

        // Append the span to the matrix background container
        matrix.appendChild(span);
    }

    // Re-generate matrix characters on window resize for responsiveness
    window.addEventListener('resize', () => {
        while (matrix.firstChild) {
            matrix.removeChild(matrix.firstChild);
        }

        const newWidth = window.innerWidth;
        const newHeight = window.innerHeight;

        for (let i = 0; i < numChars; i++) {
            const span = document.createElement('span');
            span.textContent = Math.random() > 0.5 ? '0' : '1';
            span.style.left = Math.random() * newWidth + 'px';
            span.style.top = Math.random() * newHeight + 'px';
            span.style.animationDuration = Math.random() * 3 + 2 + 's';
            span.style.animationDelay = Math.random() * 5 + 's';
            matrix.appendChild(span);
        }
    });
});
