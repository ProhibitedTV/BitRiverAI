document.addEventListener('DOMContentLoaded', () => {
    const matrixContainer = document.querySelector('.matrix-bg');

    if (!matrixContainer) {
        console.error("Matrix background container not found!");
        return;
    }

    let width = window.innerWidth;
    let height = window.innerHeight;
    const numChars = 150;

    function createMatrixEffect() {
        for (let i = 0; i < numChars; i++) {
            const span = document.createElement('span');
            span.textContent = Math.random() > 0.5 ? '0' : '1';
            span.style.position = 'absolute';
            span.style.left = `${Math.random() * width}px`;
            span.style.top = `${Math.random() * height}px`;
            span.style.animationDuration = `${Math.random() * 3 + 2}s`;
            span.style.animationDelay = `${Math.random() * 5}s`;
            matrixContainer.appendChild(span);
        }
    }

    createMatrixEffect();

    window.addEventListener('resize', () => {
        width = window.innerWidth;
        height = window.innerHeight;
        while (matrixContainer.firstChild) {
            matrixContainer.removeChild(matrixContainer.firstChild);
        }
        createMatrixEffect();
    });
});
