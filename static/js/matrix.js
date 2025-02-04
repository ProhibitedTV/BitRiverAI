/**
 * Initialize the matrix background effect when the DOM content is loaded.
 */
document.addEventListener('DOMContentLoaded', () => {
    const matrixContainer = document.querySelector('.matrix-bg');

    if (!matrixContainer) {
        console.error("Matrix background container not found!");
        return;
    }

    const canvas = document.createElement('canvas');
    matrixContainer.appendChild(canvas);
    const ctx = canvas.getContext('2d');

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const letters = Array(256).join("1").split("");
    const fontSize = 16; // Increased font size for better visibility
    const columns = canvas.width / fontSize;

    /**
     * Draw the matrix effect on the canvas.
     */
    function draw() {
        ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = "#0F0";
        ctx.font = `${fontSize}px monospace`;

        letters.forEach((y, index) => {
            const text = String.fromCharCode(3e4 + Math.random() * 33);
            const x = index * fontSize;
            ctx.fillText(text, x, y);
            letters[index] = y > canvas.height + Math.random() * 1e4 ? 0 : y + fontSize;
        });
    }

    setInterval(draw, 33);

    /**
     * Adjust the canvas size when the window is resized.
     */
    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });
});
